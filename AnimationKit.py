class anKit:
  #def __init__(self):
  #  pass
  import os.path
  from os import path
  #video tools
  def video_sortFrames(sourceframes, destframes):  #takes frames from input folder, moves to init_frame_storage
    dir_check(sourceframes)
    dir_make(destframes)
    %cd $sourceframes
    print("Copying frames to "+destframes+" for processing...")
    !find -maxdepth 1 -name '*.png' -print0 | xargs -0 cp -t $destframes
    %cd $destframes
    #!find -maxdepth 1 -name '*.png' -print0 | xargs -0 'mv "$0" "${0##*_}"' 
    #!find . -type f -name "*_*.png" -execdir bash -c 'mv "$0" "${0##*_}"' {} \;  #removes anything not numbers
    !find . -type f -name "*.png" -execdir bash -c 'mv "$0" "${0##*_}"' {} \;  #removes anything not numbers
    #print("Padding filenames in "+destframes+".")
    !rename 's/\d+/sprintf("%05d",$&)/e' *  #adds padding to numbers
    print("Finished copying frames to "+destframes+".")
  def video_splitFrames(sourcefile, destframes):
    file_check(sourcefile)
    dir_make(destframes)
    !ffmpeg -y -r 1 -i $sourcefile -r 1 $destframes/frame%05d.png
  def frames2video(sourceframes,fps,outputmp4):
    dir_check(sourceframes)
    %cd $sourceframes
    #!ffmpeg -framerate $fps -pattern_type glob -i '*.png' -y $outputmp4
    !ffmpeg -framerate $fps -pattern_type glob -i '*.png' -vcodec hevc_nvenc -y $outputmp4

  def video_runUpscale(esrgan,mpath,scale,input,output):
    dir_check(input)
    dir_make(output)
    %cd $esrgan
    #print(mpath)
    !python inference_realesrgan.py --model_path $mpath --netscale $scale --input $input --output $output
    #%cd $output
    #!find . -type f -name "*_*.png" -execdir bash -c 'mv "$0" "${0##*_}"' {} \;  #removes anything not numbers from filename - needed for rife-frame
    #dir_numberizeFiles(output,'.png')  def video_compress(input,effects,quality,output):  #needs portable
    #!ffmpeg -y -i $input $visual_effects -c:v hevc_nvenc -rc vbr -cq $constant_quality -qmin $constant_quality -qmax $constant_quality -b:v 0 $target_output_fullpath
  def RIFE_video(fps,exp,input,scale,output):
    %cd /content/Practical-RIFE
    !python3 /content/Practical-RIFE/inference_video.py --fps=$fps --exp=$exp --video=$input --scale $scale --output=$output
  def RIFE_frames(fps,exp,input,scale,output):  #not currently working right
    %cd /content/Practical-RIFE
    input = input + '/'
    !python3 /content/Practical-RIFE/inference_video.py --fps=$fps --exp=$exp --img=$input --scale $scale --output=$output
  def detect_fps(input): #needs portable
    import re
    fps_ffprobe = !ffprobe -v error -select_streams v -of default=noprint_wrappers=1:nokey=1 -show_entries stream=avg_frame_rate $input
    fps_unfinished = [str(i) for i in fps_ffprobe] # Converting integers into strings
    fps_unfinishedTwo = str("".join(fps_unfinished)) # Join the string values into one string
    numbers = re.findall('[0-9]+', fps_unfinishedTwo)
    newNum = numbers[0:1]
    strings = [str(integer) for integer in newNum]
    a_string = "".join(strings)
    fps = int(a_string)
    #print("Detected FPS is",fps)
    return fps
  def detect_duration(input):  #needs portable
    import re
    duration_ffprobe = !ffprobe -v error -select_streams v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 $input
    duration_unfinished = [str(i) for i in duration_ffprobe] # Converting integers into strings
    duration_unfinishedTwo = str("".join(duration_unfinished)) # Join the string values into one string
    numbers = re.findall('[0-9]+', duration_unfinishedTwo)
    newNum = numbers[0:1]
    strings = [str(integer) for integer in newNum]
    a_string = "".join(strings)
    duration = int(a_string)
    #print("Detected duration INTEGER (in seconds) is",duration)
    return duration
  def exp_calc(measured_duration,target_length_seconds): #needs portable
    import numpy as np
    a = measured_fps * measured_duration
    b = target_fps * target_length_seconds
    c = b / a
    l = np.log(c) / np.log(2)
    print("Un-rounded --exp is",l)
    x = round(l)
    if x < 1:
      x = 1
    print("Rounding up to an --exp of ",x)
    return x
  #installation for Colab (untested on other platforms)
  #
  #
  def install_ESRGAN():
    print("Installing libraries for Real-ESRGAN upscaling.")
    !git clone https://github.com/xinntao/Real-ESRGAN.git &> /dev/null
    %cd Real-ESRGAN
    !pip -q install basicsr
    !pip -q install facexlib
    !pip -q install gfpgan
    !pip -q install -r requirements.txt   &> /dev/null
    !python setup.py develop              &> /dev/null
    !wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth -P experiments/pretrained_models              &> /dev/null
    !wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth -P experiments/pretrained_models   &> /dev/null
    !wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth -P experiments/pretrained_models              &> /dev/null
    print("Finished Installing libraries for Real-ESRGAN upscaling.")
    #
  def install_RIFE():
    %cd /content/
    print("Installing libraries for RIFE motion smoothing.")
    !git clone https://github.com/hzwer/Practical-RIFE Practical-RIFE &> /dev/null
    !gdown --id 1O5KfS3KzZCY3imeCr2LCsntLhutKuAqj &> /dev/null
    #%cd /content/Practical-RIFE
    !7z e RIFE_trained_model_v3.8.zip &> /dev/null
    #!7z e /content/Practical-RIFE/RIFE_trained_model_v3.8.zip
    #!7z e /content/RIFE_trained_model_v3.8.zip
    !mkdir /content/Practical-RIFE/train_log  &> /dev/null
    !mv *.py /content/Practical-RIFE/train_log/ &> /dev/null
    !mv *.pkl /content/Practical-RIFE/train_log/  &> /dev/null
    %cd /content/Practical-RIFE/
    !gdown --id 1i3xlKb7ax7Y70khcTcuePi6E7crO_dFc   &> /dev/null  #useless - mp4 demo 
    !pip3 install -r requirements.txt &> /dev/null
    print("Finsihed Installing libraries for RIFE motion smoothing.")
    #  
    %cd /content/
  def depcrecated_installOldRIFE():
    print("Installing libraries for RIFE motion smoothing.")
    !git clone https://github.com/hzwer/arXiv2020-RIFE RIFE
    !gdown --id 1wsQIhHZ3Eg4_AfCXItFKqqyDMB4NS0Yd
    !7z e RIFE_trained_model_HDv2.zip
    !mkdir /content/RIFE/train_log
    !mv *.pkl /content/RIFE/train_log/
    %cd /content/RIFE/
    !gdown --id 1i3xlKb7ax7Y70khcTcuePi6E7crO_dFc
    !pip3 install -r requirements.txt
    print("Done.")
    print("Finsihed Installing libraries for RIFE motion smoothing.")
  %cd /content/
  
  def install_3dinpainting(): #untested as a function
    !pip3 install torch==1.4.0+cu100 torchvision==0.5.0+cu100 -f https://download.pytorch.org/whl/torch_stable.html
    !pip3 install opencv-python==4.2.0.32
    !pip3 install vispy==0.6.4
    !pip3 install moviepy==1.0.2
    !pip3 install transforms3d==0.3.1
    !pip3 install networkx==2.3
    !sudo apt install sed
    %cd /content/
    !git clone https://github.com/sadnow/3d-photo-inpainting.git
    %cd 3d-photo-inpainting
    !sh download.sh
    !sed -i 's/offscreen_rendering: True/offscreen_rendering: False/g' argument.yml

  def run_3dinpainting(): #untested as a function
    !mkdir image
    !mkdir video
    %cd image
    from google.colab import files
    uploaded = files.upload()
    for fn in uploaded.keys():
      print('User uploaded file "{name}" with length {length} bytes'.format(
          name=fn, length=len(uploaded[fn])))
    %cd ..
    !python main.py --config argument.yml
###


###############################################################