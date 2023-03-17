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

<h1 align="center">Speech Analyzer</h3>

  <p align="center">
    An AI-supported app that analyzes public speaking videos to provide feedback on various parameters like eye contact, facial expression, emotional tone, and sentiment analysis.
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
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#building-the-project">Building the project</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Do you ever feel nervous or anxious about public speaking? If so, you're certainly not alone. Many people struggle with social anxiety, which can make speaking in front of others a daunting task. But the good news is that with practice, anyone can improve their speaking skills and overcome their fears.

That's where Speech Analyzer comes in. As the developer of the application, I have built a powerful AI-supported app that can analyze your video speeches and provide detailed feedback on various parameters like eye contact, facial expression, emotional tone, and sentiment analysis. By using this app, users can identify areas for improvement and practice delivering more effective and engaging speeches over time. With the help of cutting-edge AI technology, users can take their public speaking skills to the next level and achieve greater success and confidence in all areas of life.

The app allows you to analyze your speech with different parameters. It provides feedback on:

    How much eye contact you make with the camera
    Your facial expression
    The emotions conveyed by your words
    The overall sentiment of your speech

This app is particularly useful for those looking to practice public speaking and improve their performance with AI-generated feedback.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

    Flask for front end
    Gradio for deploying model API in Hugging Face
    Hugging Face and FastAI for model training and importing
    OpenCV for isolating the face


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To use the app, you will need a video of the speech you want to analyze. Make sure it is in mp4 format. If it is not in mp4, you can use any online video converter like [this](https://cloudconvert.com/mp4-converter) to convert it to mp4.

    Visit the Speech Analyzer website.
    Choose the video you want to upload
    Click on "Submit" and wait for the analysis to complete.
    Once the analysis is complete, you will see the results displayed on the screen.

That's it! It's that easy to use the Speech Analyzer app. Give it a try and see how it can help you improve your public speaking skills.
NOTE: It takes a bit of time to analyze videos along with uploading the file as a lot of work is done in the backend. Since the servers are in free tier it takes a while to get the resources allocated to the app so you may have to wait a while to get the response.

<!-- USAGE EXAMPLES -->
## Usage

Go to the [Live Demo](https://speech-analyzer.onrender.com/) and upload a video. Wait a few minutes and you'll get the result like below
![Speech Analyzer](https://user-images.githubusercontent.com/52294804/225854370-15a9e74b-4f44-4e2a-9d71-bbe28a24b310.png)

Here are some examples of how you can use the Speech Analyzer app:

    Practice speeches for school or work
    Prepare for a job interview
    Improve your presentation skills
    Boost your confidence when speaking in public

Whatever your goals may be, Speech Analyzer can help you achieve them with AI-generated feedback and analysis.

Please note that the current version of the app only supports video files in mp4 format.

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

Distributed under the MIT License. See `LICENSE` for more information.

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
