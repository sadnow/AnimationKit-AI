ALPHA 2.5: Frostbite Revival (Released 12/23/21)

Changelog:

    [ UI ] Chained design. All steps link to one another! Use the master override toggles to skip processes.
    [ Upscaling ] GFPGAN face-enhance toggle (embedded in Real-ESRGAN)
    [ Interpolation ] Practical-RIFE implementation; 4.0 model
    [ File mgmt ] Compatibility with padded filenames, File overwrite protection, verification of completion
    [ Misc ] Forked essential dependencies for long-term backwards compatibility; if needed.

*This updates brings AnKit back to a functioning state. Upcoming updates will make use of recent prerequisite updates and coinciding AI advances. *

---

# AnimationKit - AI Upscaling & Interpolation using Real-ESRGAN+RIFE
*Your all-in-one post-processing tool.*

*Early Alpha Google Colab Notebook*

1. [AnimationKit Colab Notebook](https://github.com/sadnow/RIFE-Google-Colab-Simplified/blob/main/AnimationKit_Rife_RealESRGAN_Upscaling_Interpolation.ipynb) for Real-ESRGAN <a href="https://colab.research.google.com/github/sadnow/AnimationKit-AI_Upscaling-Interpolation_RIFE-RealESRGAN/blob/main/AnimationKit_Rife_RealESRGAN_Upscaling_Interpolation.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="google colab logo"></a>.


Features Real-ESRGAN video upscaling, RIFE interpolation/motion smoothing, and FFMPEG hevc_nvenc (h265) compression

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

Prior Changelog (Incomplete)

#ALPHA 2: Released 9/4/21
Feature additions
- :🔻: Deflickering [Depcrecated]
- :white_check_mark: Upscaling from individual frames (P2)
- :white_check_mark: Target length (in seconds) for RIFE interpolation - Replaces old length_multiplier option
