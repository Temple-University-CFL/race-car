[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/ANI717/race-car">
    <img src="readme/temple.png" alt="Logo" width="100" height="100">
  </a>

  <h1 align="center">Temple Race-car Project - Deep Learning Repository</h1>

  <h4 align="center">
    We are developing an End-to-end Learning Architecture for Autonomous Driving with Regression Model Approach
  </h4>
</p>


[![Temple Race Car - Prediction on Captured Video (Youtube)](http://img.youtube.com/vi/yulaIIDh_K0/0.jpg)](http://www.youtube.com/watch?v=yulaIIDh_K0 "Temple Race Car - Prediction on Captured Video (Youtube)")
.
### Temple Race Car - Prediction on Captured Video (Youtube)



## Environment SetUp (Windows)
* Install Anaconda (64 Bit, Python 3.7 version or higher)
```
https://www.anaconda.com/products/individual
```
* Install OpenCV and Torch modules with Anaconda prompt.
```
pip install opencv-contrib-python
conda install pytorch -c pytorch
conda install torchvision -c pytorch
```

## Software Repository
### Driver Softwares
* av_create_dataset.py
```
Creates CSV files contaning list of image directory paths for training, development and testiong sessions.
```
* av_refine_dataset.py
```
Removes unwanted images with false annotation and refine dataset visually.
```
* av_train_test.py
```
Driver software to run training and testing sessions
```
* av_prediction_test.py
```
Driver software to test prediction visually
```


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ANI717/race-car.svg?style=flat-square
[contributors-url]: https://github.com/ANI717/race-car/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ANI717/race-car.svg?style=flat-square
[forks-url]: https://github.com/ANI717/race-car/network/members
[stars-shield]: https://img.shields.io/github/stars/ANI717/race-car.svg?style=flat-square
[stars-url]: https://github.com/ANI717/race-car/stargazers
[issues-shield]: https://img.shields.io/github/issues/ANI717/race-car.svg?style=flat-square
[issues-url]: https://github.com/ANI717/race-car/issues
[license-shield]: https://img.shields.io/github/license/ANI717/race-car.svg?style=flat-square
[license-url]: https://github.com/ANI717/race-car/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/ani717
[product-screenshot]: images/screenshot.png
