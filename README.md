<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
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



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/hieuhn09/IELTS-Writing-Checker">
    <img src="images/logo.png" alt="Logo" width="400" height="400">
  </a>

<h1 align="center">IELTS Writing Checker</h1>

  <p align="center">
    Automated IELTS essay grading
    <br />
    <a href="https://github.com/hieuhn09/IELTS-Writing-Checker"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/hieuhn09/IELTS-Writing-Checker">View Demo</a>
    ·
    <a href="https://github.com/hieuhn09/IELTS-Writing-Checker/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/hieuhn09/IELTS-Writing-Checker/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#introduction">Introduction</a>
    <li><a href="#features">Features</a>
    <li><a href="#report-and-demo-video">Report and demo video</a>
    <li><a href="#user-scenarios">User Scenarios</a></li>
    <li><a href="#user-stories">User Stories</a></li>
    <li><a href="#built-with">Built With</a></li>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Introduction

[![Product Name Screen Shot][product-screenshot]](<img src="images/screenshot.png" alt="Logo">)

This web application is developed to automatically grade and review IELTS Task 2 writing. Utilizing the Gemini API, the application evaluates essays based on specific IELTS criteria and provides automatic scoring. In addition to grading, the application offers detailed feedback on each aspect of the IELTS writing criteria, helping users improve specific areas of their writing. It also supports users in enhancing their arguments, suggesting improvements in vocabulary and grammar to further refine their essays. This comprehensive tool is designed to assist IELTS candidates in achieving higher scores by providing thorough and constructive feedback.

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `hieuhn09`, `IELTS-Writing-Checker`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `IELTS Writing Checker`, `project_description`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Features:
- **Submission**: 
    *  Users can submit their essays in text format through the text input box.
    * The essay will be automatically graded, and users will be immediately redirected to the results page.
- **Account Creation and Essay Storage**: 
    * Users can create an account to save and track the results of their essay submissions.\
    * Users can review their essay scores, delete their essay history, and set their essays as public or private.
- **Feedback on Essays**: 
    * The application provides detailed feedback on each essay, highlighting strengths and areas for improvement.
    * Users receive constructive criticism to enhance their writing skills and improve future submissions.
- **Referencing Essays**: 
    * Users can browse and reference essays that other users have set as public.
    * This feature allows users to learn from others' writing and gain insights into different writing styles and approaches.
- **Random Prompt Selection**:
    * The application offers a feature to generate a random writing prompt for users.
    * Users have the option to change the prompt if they wish to choose a different topic.

### Report and demo video:
[Group91-IWC-Drive](https://drive.google.com/drive/folders/1YgZCqFx44DWOMdophT5vXYoi794CH7MB?usp=drive_link)

### Running the Application
#### Without Docker
1. Clone the repository
```
git clone
```
2. Install the required packages
```
pip install -r requirements.txt
```
3. Navigate to the project directory
```
cd ielts_checker
```
4. Run the Django server
```
python manage.py runserver
```
The application should now be running at http://localhost:8000.
#### With Docker
1. Install [Docker](https://www.docker.com/get-started) if you haven't already.

2. Clone the repository:
```
git clone
```
3. Build the Docker image
```
docker build -t ielts_checker .
```
4. Run the Docker container
```
docker run -p 8000:8000 ielts_checker
```



### User Scenarios:
#### 1. Long's scenario : College student preparing for IELTS test
Long, an aspiring IELTS test-taker dedicated to achieving a high band score in the Writing section, seeks an efficient and dependable tool to refine his writing abilities and receive constructive feedback on his essays. With this goal in mind, Long anticipates a seamless experience with the website. He expects to easily create a user account, providing basic information such as name, email, and password, followed by a confirmation email to verify his account upon successful registration.

Once logged in, Long envisions a straightforward process for essay submission, allowing him to either copy and paste his essay content or upload a text file directly on the website. With his essay submitted, Long eagerly awaits the automatic grading process, relying on the ChatGPT API to assess his writing against IELTS standards accurately and efficiently. He anticipates receiving detailed feedback highlighting both the strengths and areas for improvement in his writing, accompanied by specific suggestions for enhancing vocabulary, grammar, coherence, and overall essay structure.

In addition to receiving feedback on individual essays, Long desires the ability to track his progress over time through a personalized dashboard. He envisions accessing key metrics such as the number of essays submitted, average scores, and trends in his writing performance, allowing him to monitor his improvement and identify areas requiring further attention. By meeting these expectations, the website will empower Long to enhance his writing skills effectively, providing valuable support on his journey to success in the IELTS exam.

#### 2. Ms.Trang's scenario : Using the website for quickly grading her students
Ms. Trang, a dedicated IELTS teacher with a commitment to her students' success, seeks a streamlined solution for efficiently grading their writing assignments. As an educator juggling various responsibilities, Ms. Trang envisions leveraging a user-friendly website tailored to her needs. She anticipates a seamless account creation process, allowing her to register as a teacher effortlessly and gain access to a dedicated dashboard designed for grading purposes.

Upon logging in, Ms. Trang expects to navigate to the essay grading section of the website, where she can conveniently view and assess her students' submitted essays. With a clear interface displaying essential details such as student names, submission dates, and essay topics, she aims to efficiently review each essay, provide personalized feedback, and assign grades accordingly. Leveraging the ChatGPT API for automatic grading assistance, Ms. Trang values the preliminary evaluations provided while also retaining the flexibility to apply her expertise and insights in refining the feedback and grades.

Furthermore, Ms. Trang seeks the capability to generate comprehensive reports summarizing her students' performance over time. These reports will empower her to track progress, identify areas of improvement, and tailor her teaching approach to meet the unique needs of each student effectively. By fulfilling Ms. Trang's expectations for efficiency, flexibility, and insightful feedback, the website serves as an invaluable tool in her mission to support her students' growth and success in the IELTS exam.

### User Stories
From the scenarios above, we have user stories:
1. For Long's Scenario:
- As a dedicated IELTS test-taker, I want to create a user account easily, so that I can access the website's features and track my progress effectively.
- As a proactive learner, I want the ability to submit my essays for evaluation, so that I can receive feedback on my writing and improve my skills.
- As a busy individual, I want the essay submission process to be straightforward, so that I can save time and focus on my preparation.
- As a goal-oriented test-taker, I want the essays to be automatically graded against IELTS standards, so that I can receive objective assessments of my performance.
- As a learner striving for improvement, I want detailed feedback on my essays, so that I can identify areas of strength and areas for improvement in my writing.

2. For Ms. Trang's Scenario:
- As an IELTS teacher, I want to create a teacher account easily, so that I can access the grading features and support my students effectively.
- As an educator managing multiple tasks, I want a streamlined process for grading essays, so that I can efficiently assess my students' work without unnecessary complexity.
- As a teacher aiming for accuracy, I want the option to adjust automated grades based on my expertise, so that I can provide precise feedback to my students.
- As a facilitator of student growth, I want to provide detailed feedback on essays, so that I can help my students understand their strengths and areas for improvement.
- As an educator monitoring progress, I want the ability to generate reports summarizing students' performance, so that I can track their progress over time and adapt my teaching strategies accordingly.



### Built With

* [![Django][Django-badge]][Django-url]
* [![Docker][Docker-badge]][Docker-url]
* [![HTML][HTML-badge]][HTML-url]
* ![Angular][CSS-badge]
* ![Java Script][Java Script-badge]
* [![Github][Github-badge]][Github-url]
* [![Git][Git-badge]][Git-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Installation:
1. Clone this repo
2. Install the required packages by running ```pip install -r requirements.txt.```
3. cd  into ```ielts_checker```
4. Run server: ```python manage.py runserver```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

See `CONTRIBUTING.md` for more information.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Hieu Nguyen - 22022510@vnu.edu.vn

Project Link: [https://github.com/hieuhn09/IELTS-Writing-Checker](https://github.com/hieuhn09/IELTS-Writing-Checker)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/hieuhn09/IELTS-Writing-Checker.svg?style=for-the-badge
[contributors-url]: https://github.com/hieuhn09/IELTS-Writing-Checker/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/hieuhn09/IELTS-Writing-Checker?style=for-the-badge
[forks-url]: https://github.com/hieuhn09/IELTS-Writing-Checker/forks
[stars-shield]: https://img.shields.io/github/stars/hieuhn09/IELTS-Writing-Checker.svg?style=for-the-badge
[stars-url]: https://github.com/hieuhn09/IELTS-Writing-Checker/stargazers
[issues-shield]: https://img.shields.io/github/issues/hieuhn09/IELTS-Writing-Checker.svg?style=for-the-badge
[issues-url]: https://github.com/hieuhn09/IELTS-Writing-Checker/issues
[license-shield]: https://img.shields.io/github/license/hieuhn09/IELTS-Writing-Checker.svg?style=for-the-badge
[license-url]: https://github.com/hieuhn09/IELTS-Writing-Checker/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Django-badge]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[Docker-badge]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[HTML-badge]: https://img.shields.io/badge/HTML-E44D26?style=for-the-badge&logo=html&logoColor=white
[HTML-url]: https://html.com/
[CSS-badge]: https://img.shields.io/badge/CSS-264DE4?style=for-the-badge&logo=css&logoColor=white
[Java Script-badge]: https://img.shields.io/badge/JAVA%20SCRIPT-F0DB4F?style=for-the-badge&logo=javascript&logoColor=white
[Github-badge]: https://img.shields.io/badge/GITHUB-151013?style=for-the-badge&logo=github&logoColor=white
[Github-url]: https://github.com/
[Git-badge]: https://img.shields.io/badge/GIT-F1502F?style=for-the-badge&logo=git&logoColor=white
[Git-url]: https://git-scm.com/