Dev Note 12/22/21: This app will be undergoing long-needed improvements and bug-fixes throughout the next few weeks. Future advances in upscaling and interpolation will be considerd as the dev catches up on testing. Thanks for all the interest!

# AnimationKit - AI Upscaling & Interpolation using Real-ESRGAN+RIFE

*Early Alpha Google Colab Notebook*

1. [AnimationKit Colab Notebook](https://github.com/sadnow/RIFE-Google-Colab-Simplified/blob/main/AnimationKit_Rife_RealESRGAN_Upscaling_Interpolation.ipynb) for Real-ESRGAN <a href="https://colab.research.google.com/github/sadnow/AnimationKit-AI_Upscaling-Interpolation_RIFE-RealESRGAN/blob/main/AnimationKit_Rife_RealESRGAN_Upscaling_Interpolation.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="google colab logo"></a>.


Features Real-ESRGAN video upscaling, RIFE interpolation/motion smoothing, (improvised) deflickering, and FFMPEG hevc_nvenc (h265) compactor

#ALPHA 2: Released 9/4/21

Feature additions

- :white_check_mark: Deflickering (P3)
- :white_check_mark: Upscaling from individual frames (P2)
- :white_check_mark: Target length (in seconds) for RIFE interpolation - Replaces old length_multiplier option

Credits: Motion smoothing conceived from "Zoom animation processing and motion interpolation" added by https://twitter.com/unltd_dream_co. This part of the script uses [RIFE real-time video interpolation](https://github.com/hzwer/arXiv2020-RIFE) to smooth out the resulting video. 

Upscaling uses Real-ESRGAN (https://github.com/xinntao/Real-ESRGAN). A demo notebook for static images can be found here: https://colab.research.google.com/drive/1k2Zod6kSHEvraybHl50Lys0LerhyTMCo?usp=sharing. The demo was based on the following paper: of our paper [''Real-ESRGAN: Training Real-World Blind Super-Resolution with Pure Synthetic Data''](https://arxiv.org/abs/2107.10833).

<img src="https://raw.githubusercontent.com/xinntao/Real-ESRGAN/master/assets/teaser.jpg" width="100%">

#Alpha 1 release: All major bugs have (hopefully) been patched. New functions will be released in the testing branch until debugged.

Feature additions & bugfixes:

- :white_check_mark: Anime model for realesrgan
- :white_check_mark: 2x model
- :white_check_mark: target output path
- :white_check_mark: omission of outscaling (note, may need to check defaults in inference.py)
- :white_check_mark: target fps no longer causes duplicates prior to ffmpeg end-phase (prevents upscaler from wasting gpu cycles on duplicate frames; major speed increase)
- :white_check_mark: notebook set to high memory - necessary for RIFE

---

Planned additions:
- [ ] More deflicker options (am and pm deflicker flags may be optimal)
- [ ] --skip option for RIFE
- [ ] --tiles option for RIFE/Real-ESRGAN (?)
- [ ] face detection for real-esrgan
- [ ] h264 option (for people with older rigs)
- [ ] Preview video option for people who don't want to download the full video yet

---

Difficulties (may take longer to figure out)
- [ ] target output path for RIFE
- [ ] target duration for RIFE (need to understand how exp works, then I'll just have it divide)

Feel free to report bugs!


