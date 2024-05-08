# IELTS Writing Checker
### Members: 

-Nguyễn Nam Dương - 22022512\
-Dương Minh Đức - 22022606\
-Hoàng Đăng Khoa - 22022548\
-Nguyễn Công Hiếu - 22022512\
-Long Trí Thái Sơn - 22022653

### Introduction:
This web application is developed to automatically grade Task 2 writing of the IELTS exam. The application will assess essays based on certain criteria and provide automatic scoring using ChatGPT API.

### User scenarios:
####1. Long's scenario : College student preparing for IELTS test
Long, an aspiring IELTS test-taker dedicated to achieving a high band score in the Writing section, seeks an efficient and dependable tool to refine his writing abilities and receive constructive feedback on his essays. With this goal in mind, Long anticipates a seamless experience with the website. He expects to easily create a user account, providing basic information such as name, email, and password, followed by a confirmation email to verify his account upon successful registration.

Once logged in, Long envisions a straightforward process for essay submission, allowing him to either copy and paste his essay content or upload a text file directly on the website. With his essay submitted, Long eagerly awaits the automatic grading process, relying on the ChatGPT API to assess his writing against IELTS standards accurately and efficiently. He anticipates receiving detailed feedback highlighting both the strengths and areas for improvement in his writing, accompanied by specific suggestions for enhancing vocabulary, grammar, coherence, and overall essay structure.

In addition to receiving feedback on individual essays, Long desires the ability to track his progress over time through a personalized dashboard. He envisions accessing key metrics such as the number of essays submitted, average scores, and trends in his writing performance, allowing him to monitor his improvement and identify areas requiring further attention. By meeting these expectations, the website will empower Long to enhance his writing skills effectively, providing valuable support on his journey to success in the IELTS exam.

####2. Ms.Trang's scenario : Using the website for quickly grading her students
Ms. Trang, a dedicated IELTS teacher with a commitment to her students' success, seeks a streamlined solution for efficiently grading their writing assignments. As an educator juggling various responsibilities, Ms. Trang envisions leveraging a user-friendly website tailored to her needs. She anticipates a seamless account creation process, allowing her to register as a teacher effortlessly and gain access to a dedicated dashboard designed for grading purposes.

Upon logging in, Ms. Trang expects to navigate to the essay grading section of the website, where she can conveniently view and assess her students' submitted essays. With a clear interface displaying essential details such as student names, submission dates, and essay topics, she aims to efficiently review each essay, provide personalized feedback, and assign grades accordingly. Leveraging the ChatGPT API for automatic grading assistance, Ms. Trang values the preliminary evaluations provided while also retaining the flexibility to apply her expertise and insights in refining the feedback and grades.

Furthermore, Ms. Trang seeks the capability to generate comprehensive reports summarizing her students' performance over time. These reports will empower her to track progress, identify areas of improvement, and tailor her teaching approach to meet the unique needs of each student effectively. By fulfilling Ms. Trang's expectations for efficiency, flexibility, and insightful feedback, the website serves as an invaluable tool in her mission to support her students' growth and success in the IELTS exam.

### User stories
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

### Features:
- **User Accounts**: Users can creat account, save and track their progress over time.
- **Submit Essays**: Users can submit their essays for grading.
- **Automatic Grading**: The application uses the ChatGPT API to automatically grade the essays based on IELTS standards.
- **Detailed Feedback**: Provide detailed feedback on each essay, highlighting areas of strength and areas for improvement.

### Installation:
1. Clone this repo
2. Install the required packages by running ```pip install -r requirements.txt.```
3. cd  into ```ielts_checker```
4. Run server: ```python manage.py runserver```

### Tech Stack:
- Framework: Django
- Deployment: Docker, Microsoft Azure
- Frontend: HTML, CSS, JavaScript
- Version Control: Git, GitHub
