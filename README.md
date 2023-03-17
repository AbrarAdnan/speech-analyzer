<a name="readme-top"></a>


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

<h3 align="center">Speech Analyzer</h3>

  <p align="center">
    An AI supported app that can analyze your speech videos.
    <br />
    <a href="https://speech-analyzer.onrender.com/">View Demo</a>
    ·
    <a href="https://github.com/AbrarAdnan/speech-analyzer/issues">Report Bug</a>
    ·
    <a href="https://github.com/AbrarAdnan/speech-analyzer/issues">Request Feature</a>
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
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#building-the-model">Building the project</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Do you ever feel nervous or anxious about public speaking? If so, you're certainly not alone. Many people struggle with social anxiety, which can make speaking in front of others a daunting task. But the good news is that with practice, anyone can improve their speaking skills and overcome their fears.

That's where Speech Analyzer comes in. This powerful AI-supported app can analyze your video speeches and provide detailed feedback on various parameters like eye contact, facial expression, emotional tone, and sentiment analysis. By using this app, you can identify areas for improvement and practice delivering more effective and engaging speeches over time. With the help of cutting-edge AI technology, you can take your public speaking skills to the next level and achieve greater success and confidence in all areas of your life.

You can analyze your speech with different parameters.
It'll say 
1. How much you made eye contact with the camera.
2. What your face expression was
3. What emotions your words contained
4. Sentiment of your speech between positive and negative.

This is useful to practice public speaking and you can judge how your performance is with an AI.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
Flask for front end <br>
Gradio for deploying model API in huggingface <br>
huggingface and FAST AI for training and importing model <br>
opencv for isolating the face <br>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Firstly get a video you want to analyze and make sure it's in mp4 format. If it's not in mp4 format you can convert it [Here](https://cloudconvert.com/mp4-converter). Make sure the video has proper lighting and visiblility without any distractions and noise so that it can be analyzed more accurately.



<!-- USAGE EXAMPLES -->
## Usage

Go to the [Live Demo](https://speech-analyzer.onrender.com/) and upload a video. Wait a few minutes and you'll get the result like below
![Speech Analyzer](https://user-images.githubusercontent.com/52294804/225854370-15a9e74b-4f44-4e2a-9d71-bbe28a24b310.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Building the project
The codes used for this are given in the notebook folder along with the comments for their use cases.
Data prep was used to collect data and prepare them for model training.
The data were collecetd from different youtube videos and the [labelled faces in the wild dataset](https://www.kaggle.com/datasets/atulanandjha/lfwpeople).
Training was used to train the model. We used resnet 18 because it's small in size and fast. Since we had small dataset and only two labels to choose from our model was performing good.
To get the emotions from the facial expressions we used [deepface](https://github.com/serengil/deepface)
Tor getting the transcripts we used [whisper-tiny](https://huggingface.co/openai/whisper-tiny) model
For getting emotions from text transcript we used [emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) model from huggingface
For getting the sentiments from the transcript we used [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) model
More complex model needs more datasets else they'd overfit. The model was fine-tuned with 2000+ images with 76% accuracy in 6 epochs



<!-- ROADMAP -->
## Future work and limitations

1. The eye contact model is not accurate enough as the dataset is not much abundant.
2. The rest of the analysis parameters were used with pretrained models because the dataset and computational power to make those models is not available.
3. Grammer analysis can be a good addition.
4. Since it's hosted on a free platform the output is slow and the video takes frames every few second for eye contact detection to make it faster. This might affect eye contact accuracy.

See the [open issues](https://github.com/AbrarAdnan/speech-analyzer/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Abrar Faiaz Adnan - [Linkedin](https://www.linkedin.com/in/abrar-faiaz/)

Project Link: [https://github.com/AbrarAdnan/speech-analyzer](https://github.com/AbrarAdnan/speech-analyzer)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AbrarAdnan/speech-analyzer.svg?style=for-the-badge
[contributors-url]: https://github.com/AbrarAdnan/speech-analyzer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AbrarAdnan/speech-analyzer.svg?style=for-the-badge
[forks-url]: https://github.com/AbrarAdnan/speech-analyzer/network/members
[stars-shield]: https://img.shields.io/github/stars/AbrarAdnan/speech-analyzer.svg?style=for-the-badge
[stars-url]: https://github.com/AbrarAdnan/speech-analyzer/stargazers
[issues-shield]: https://img.shields.io/github/issues/AbrarAdnan/speech-analyzer.svg?style=for-the-badge
[issues-url]: https://github.com/AbrarAdnan/speech-analyzer/issues
[license-shield]: https://img.shields.io/github/license/AbrarAdnan/speech-analyzer.svg?style=for-the-badge
[license-url]: https://github.com/AbrarAdnan/speech-analyzer/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/abrar-faiaz/
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
