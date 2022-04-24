<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/corbinr40/RTCC">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">RTCC</h3>

  <p align="center">
    RTCC, or *Real Time Communication Captions*, is a piece of software that converts voice to text in a visual output, as an aid to individuals who are hard of hearing. The plan is to deliver this via a piece of hardware in the form of glasses with a heads up display. However a fallback of this would be an app that fulfils this. The system will work by using facial detection to track who is talking to place the converted audio appropriately.
    <br />
    <a href="https://github.com/corbinr40/RTCC"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/corbinr40/RTCC">View Demo</a>
    ·
    <a href="https://github.com/corbinr40/RTCC/issues">Report Bug</a>
    ·
    <a href="https://github.com/corbinr40/RTCC/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!--[![Product Name Screen Shot][product-screenshot]](https://example.com)-->

RTCC is broken down into 4 main areas: audio, visual, UI, and hardware. The audio component focuses on taking audio in from the user, processing it and then outputting, along with handeling audio commands for system processes. The visual component will use a camera to look for a face, detect where it is and pass the data onto the UI. The UI handles all of the aspects which the user sees and interacts with. Finally, the hardware component is making sure all of the software works efficiently and cohesive with one another.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python 3.10](https://www.python.org/)
* [OpenCV](https://opencv.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
There are a few dependencies for running this software. The software has been created for the *Raspberry Pi Zero W 2* but can also run on *Windows* and *Mac*.
### Hardware (tested)
- [Raspberry Pi Zero W 2]()
- [Adafruit I2S Microphone]()
- [Raspberry Pi Camera]()
- [Battery Pack Device]()

### Software

#### Operating System (tested)
- [Raspian OS]()
- [MacOSX]()
- [Windows 10]()
#### Required Modules
##### All
- [faulthandler]()
- [pstats]()
- [tkinter]()
- [datetime]()
- [time]()
- [platform]()
- [multiprocessing]()
- [numpy]()
- [OpenCV - Python](https://pypi.org/project/opencv-python/)
- [threading]()
- [speech recognition]()
- [pyjokes]()
- [re]()
- [configparser]()
##### Raspian Specific
- [smbus]()

### Prerequisites

#### All
These all require `pip` to be installed
```shell
    pip3 install numpy
    pip3 install opencv-python
    pip3 install pyjokes
```

#### Raspian (specific)
To get SpeechRecognition installed, PyAudio is required and installed though apt-get.
```sh
PyAudio:

  sudo apt-get install python-dev
  sudo apt-get install portaudio19-dev
  sudo pip install pyaudio

Speech Recognition:

  pip3 install SpeechRecognition
```

#### MacOS (specific)
To get SpeechRecognition installed, PyAudio (pip) is required and PortAudio ([Homebrew]()).
```sh
PortAudio:

  brew install portaudio

PyAudio:

  pip3 install pyaudio

Speech Recognition:

  pip3 install SpeechRecognition
```

#### Windows (specific)
To get SpeechRecognition installed, [PipWin]() is required to install pyaudio.
```powershell
PipWin:

  pip install pipwin

PyAudio:

  pipwin install pyaudio

Speech Recognition:

  pip install SpeechRecognition
```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/corbinr40/rtcc.git
   ```
2. Make sure all required modules are installed
3. Run the `main.py` file
   ```sh
   python3 main.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The program is intended for use with voice commands, but does have them bound to keys for debugging/use without microphone

### Voice commands
All voice commands require the **wake word** to activate.

As default, the wake word is "***glass***"

All commands follow the format of:
```
    <wake word> <command>
```

Example:
```
    glass activate face detection
```
#### List of commands
* **face detection** - Activate/Deactivate face detection
* **voice detection** - Activate/Deactivate voice detection
* **settings** - Show settings
* **commands** - Show command list
* **shut down** - Close program
* **set font colour red** - Set font colour to Red
* **set font colour green** - Set font colour to Green
* **set font colour blue** - Set font colour to Blue
* **set font colour white** - Set font colour to White
* **increase font size** - Increase font size
* **decrease font size** - Decrease font size

### Key combines
**All are case-sensitive**
#### System Wide
* <kbd>o</kbd> - Activate/Deactivate face detection
* <kbd>p</kbd> - Activate/Deactivate voice detection
* <kbd>s</kbd> - Show settings
* <kbd>c</kbd> - Show command list
* <kbd>escape</kbd> - Close program

#### Settings only
* <kbd>P</kbd> - Set font colour to Red
* <kbd>O</kbd> - Set font colour to Green
* <kbd>I</kbd> - Set font colour to Blue
* <kbd>U</kbd> - Set font colour to White
* <kbd>+</kbd> - Increase font size
* <kbd>-</kbd> - Decrease font size

<p align="right">(<a href="#top">back to top</a>)</p>

## Program Breakdown
### Face Detection and Training Model
### Audio Component
### GUI Interface

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/corbinr40/rtcc/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@corbinr40](https://twitter.com/corbinr40) - corbinr40@live.com

Project Link: [https://github.com/corbinr40/rtcc](https://github.com/corbinr40/rtcc)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/corbinr40/rtcc.svg?style=for-the-badge
[contributors-url]: https://github.com/corbinr40/rtcc/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/corbinr40/rtcc.svg?style=for-the-badge
[forks-url]: https://github.com/corbinr40/rtcc/network/members
[stars-shield]: https://img.shields.io/github/stars/corbinr40/rtcc.svg?style=for-the-badge
[stars-url]: https://github.com/corbinr40/rtcc/stargazers
[issues-shield]: https://img.shields.io/github/issues/corbinr40/rtcc.svg?style=for-the-badge
[issues-url]: https://github.com/corbinr40/rtcc/issues
[license-shield]: https://img.shields.io/github/license/corbinr40/rtcc.svg?style=for-the-badge
[license-url]: https://github.com/corbinr40/rtcc/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/corbinrichardson
<!--[product-screenshot]: images/screenshot.png-->
