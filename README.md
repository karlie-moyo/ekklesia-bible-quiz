# Ekklesia Bible Quiz

![WhatsApp Image 2023-09-24 at 10 50 40](https://github.com/Karlie-crypto/ekklesia-bible-quiz/assets/110098940/2fcc195b-1905-44d9-bd65-fa28ab3721b4)

The Bible Quiz Web App is an engaging and educational project designed to test and enhance your knowledge of the Bible. This web application provides a platform for users to explore the scriptures, challenge themselves, and deepen their understanding of this timeless text through interactive quizzes. Whether you are a seasoned theologian or a curious beginner, this app offers an opportunity to learn, grow, and connect with others who share your interest in the Bible. Enjoy!!! https://ekklesia.karliemoyo.tech

| TASK | FILE NAME                                                                 | DESCRIPTION                                                    |
| ---- | -------------------------------------------------------------------- | --------------------------------------------------------------------|
|  🗂️   | [Models📁](./models)                                                   |  This models folder contains classes that define the structure and relationships of the app’s data using SQLAlchemy. These models represent different entities, such as Question, with attributes and methods for managing data. They interact with the database and handle data operations like creating, updating, and retrieving records. Each model typically includes relationships to other models, data validation, and utility methods for formatting data.⚙️    |                                             
|  🗂️   | [Frontend📁](./frontend)                                               | The frontend folder contains a React app with pages and components for the Bible Quiz app. It handles routing between the Home page, Start page, Quiz component, and Leaderboards. The app includes a Toast for notifications and a background image for design, creating an interactive and visually appealing user experience. |                                                              
|  🗂️   | [Api📁](./api)                                                         | The api folder contains a Flask-based RESTful API for the Bible Quiz app, with routes for handling requests, error handling (e.g., 400, 404, 500), and status checks. It sets up app configurations, supports CORS, and manages user authentication via context setup.🔁        |
|  ␜   | [Api Documentation](./API_DOCUMENTATION.md)                       |  The Bible Quiz Web App is an interactive platform that allows users to test and enhance their Bible knowledge through quizzes, user creation, and answer submissions, with feedback and scores provided.  |
|  ␜   | [Bible Quiz Service](./bible_quiz.service)                           | The bible_quiz.service file sets up the Bible Quiz API to run with Gunicorn, logs output and errors to specific files, and starts after the network is ready. It runs as the ubuntu user on port 5000. |
|  ␜   | [App ](./app.py/)                                       | This script imports the Flask app from api.v1.app and runs it on the specified host and port, using environment variables for the port and debug mode. It ensures the app loads environment variables and starts in debug mode if specified.    | 
| ␜    | [Questions](./questions/)                                                                          | The questions file contains a list of quiz questions along with possible answers. Each question has a unique ID, text, and associated answers, with each answer having its own ID and text. The data also includes a count of the total number of questions (e.g., 20 questions) to be used in the quiz.|
|   ␜  | [Setup DB Sql](./setup_db.sql/)                                                                |  The script sets up a MySQL database for the Bible Quiz app by creating the bible_quiz_db database, a user (bible_quiz_root) with a password, and granting the user full privileges on the database. It also grants the user read access to the performance_schema and flushes privileges to apply changes.          |
| ␜    | [Extract Questions](./extract_questions.py/)                                                                       | This script processes quiz questions and answers from a text file (questions.txt). It reads the file, extracts the question and answer text, and saves them to the database. The script distinguishes correct answers by checking for an asterisk (*) and assigns them accordingly. Every fifth line represents a question, while the others are answers associated with the previous question.      |
| ␜   | [Tmp](./tmp/)                                                                       | The response provides the result of a quiz attempt with three questions. Each question has multiple answers, one of which is marked as correct. The user's selected answer for each question is recorded, along with the correct answer. The user scored 2 out of 3. The message indicates that the questions were graded successfully.|
|  ␜    | [Environment](./.env)                                                       |The file contains environment variables for the Bible Quiz web application, including database credentials, API settings, authentication details, and SMTP configuration for email notifications.➿                       |
|   ␜   | [Fab File](./fabfile.py/)                                             | This script automates the deployment of a socket application to a remote server by archiving the project, transferring it, installing dependencies, and managing the socket service (start, stop, restart). ☑️✔️                                |
|    ␜  | [Captain Definition](./captain-definition/)                                     | This configuration specifies the schema version as 2 and defines the path to the Dockerfile as ./Dockerfile ☑️✔️
|  ␜    | [Dump Sql](./dump.sql)                                               | This MySQL dump file sets up the smm_db database with two tables: smtp_configs (storing SMTP server settings) and users (storing user details). It defines table structures, foreign key constraints, and inserts sample data into both tables.    |
|   ␜   | [Requirements Txt](./requirements.txt)                               | This is a list of Python dependencies used for web development, security, database management, and concurrency. Key libraries include Flask, SQLAlchemy, Gunicorn, bcrypt, cryptography, and Redis, along with other packages for API documentation, database migrations, and environment configuration.       |
|  ␜    | [Gunicorn Config](./gunicorn.conf.py/)                                       | This configuration sets up a Gunicorn server to run on port 5000 with 1 worker. It logs access and error messages to standard output (denoted by -).                             |
| ␜     | [Docker File](./Dockerfile/)                                                  | This Dockerfile uses the official Python 3.12.3 image, sets the working directory to /app, installs dependencies from requirements.txt, installs wkhtmltopdf, copies the application code, exposes port 5000, and starts the application using Gunicorn with a specified configuration.|
|   ␜  | [.gitignore](./.gitignore)                                                | Your task, Figure it out yourself!!!😂😂😂 |

```markdown
### How to Install and Run Eklessia Bible Quiz

1. **Clone the repository:**
   First, clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   cd eklessia-bible-quiz
   ```

2. **Install dependencies:**
   Ensure that you have [Node.js](https://nodejs.org/) installed. Then, install the required dependencies by running:
   ```bash
   npm install
   ```

3. **Start the development server:**
   To run the app locally in development mode, use the following command:
   ```bash
   npm run dev
   ```

4. **Access the quiz:**
   Open your browser and visit `http://localhost:3000` to start the Bible quiz.

   ### AUTHOR:
<details>
    <summary>KARLIE MOYO</summary>
    <ul>
        <li>
            <a href="https://github.com/karlie-moyo">Github</a>
        </li>
        <li>
            <a href="https://www.linkedin.com/in/karlie-moyo/">Linked-In</a>
        </li>
        <li>
            <a href="https://karlieemoyo@gmail.com">e-mail</a>
        </li>
    </ul>
</details>

---


---

### Acknowledgements  :pray:
___
All of the work in this project was conducted as part of the UoS-SE program's curriculum and requirement.
