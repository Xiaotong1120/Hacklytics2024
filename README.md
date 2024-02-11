# Math to the Point -- 4 Math
This is the repo for Hacklytics2024 4 Math group.
Math to the Point is an innovative AI-based platform designed to enhance the mathematical learning experience. By converting handwritten equations into string format in real-time, this tool bridges the gap between traditional learning methods and digital convenience. It also offers personalized feedback, ensuring that learners understand their strengths and areas for improvement.

## Features:
* Human Handwriting Interpretation: Utilizes advanced OCR (Optical Character Recognition) technology to accurately interpret handwritten numbers and symbols, converting them into string format. The tool integrates APIs like Google Cloud Vision to ensure high accuracy.

* ChatGPT Implementation: Employs AI to analyze answers for correctness and alignment with mathematical principles. If the solution deviates, the tool offers constructive feedback, guiding users toward the correct approach and enhancing their problem-solving skills.

* Creative Prompt Generation: Adapts learning strategies by continuously analyzing user input and performance, enabling personalized learning experiences. This dynamic approach ensures that each user receives tailored suggestions to overcome their unique challenges.

* User Customization and Feedback: Features user-specific customization options such as difficulty levels, preferred topics, and a feedback mechanism. Users can verify OCR results, contributing to a more accurate learning tool.(to be developed)

* Comprehensive Learning History: Maintains a detailed record of each user's progress, including attempted questions and feedback received. This data helps in curating a more focused learning path.(to be developed)

## About the Repository
* Jupyter Notebooks: The repository features well-documented Jupyter notebooks that showcase the data processing and algorithmic logic underpinning Math to the Point.

* User Interface: We've implemented an intuitive interface using Gradio, which is accessible via the app.py file. This interface is the gateway for users to interact with the Math to the Point platform, offering a user-friendly and efficient labeling experience.

* Dependency Specifications: We have included a requirements.txt file that enumerates all the dependencies essential for setting up the environment. This list ensures that anyone can replicate our development setup with minimal effort.

* Containerization Support: Our repository is equipped with a .devcontainer directory, containing all the configuration files necessary to build a Docker container. This allows anyone evaluating the project to create a consistent environment without the need to install any additional packages on their system.

## Installation Requirement (Dependencies)
To install the required dependencies, execute the following command:

``` sh
pip install -r requirements.txt
```

## Usage
* Make sure Docker Desktop is launched and configured in your local environment.
* All Jupyter notebooks within the `nbs` folder can be re-execute to test the functionality.
* Gradio UI can be opened by simply running the `app.py` file in the VSCode terminal.

## Contact
For any questions or feedback regarding ai-assisted-coding-Ember, please contact Xiaotong 'Brandon' Ma at xiaotong.ma@vanderbilt.edu.

We appreciate your interest in our project and welcome your feedback!

## Developed by:
* Ethan Yee
* Rustam Jumazhanov
* Sefika Ozturk
* Xiaotong Ma