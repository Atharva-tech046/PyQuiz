# PyQuiz
PyQuiz: The Simple CLI Quiz Engine 🚀
Welcome to PyQuiz! This repository provides a simple, clean, and powerful framework for building your own command-line quiz games in pure Python.

This project is the perfect starting point for anyone looking to create an interactive terminal application. It strips away all complexity and relies on pure Python fundamentals—no external libraries needed!

Whether you want to create a fun trivia game for your friends, a study tool for an exam, or a technical knowledge test, this project is your launchpad. The script is intentionally straightforward, making it incredibly easy to add your own questions and answers on any topic you can imagine.

The code included in this repository serves as a ready-to-use example: a short quiz on Amazon Web Services (AWS). Use it as a template to build your own!

✨ Features
Fully Customizable: Easily edit the script to create a quiz on any topic.

Interactive CLI: A classic, text-based game experience that runs in any terminal.

Instant Feedback: The script immediately validates each answer and provides "Correct✅" or "Incorrect❌" feedback.

Final Score Report: At the end of the quiz, the user gets a summary of their performance with a raw score and a final percentage.

Zero Dependencies: Built with 100% standard library Python. It runs anywhere Python is installed—no pip install required.

⚙️ Technical Deep Dive
This script demonstrates core Python fundamentals for building an interactive application:

Core Engine: A single, procedural Python script that executes from top to bottom.

User I/O: All interaction is handled through the standard library.

print() is used to display welcome messages, questions, and results.

input() is used to capture user responses from the terminal.

State Management:

A playing variable confirms the user's intent to start.

A score integer variable is initialized to 0 and incremented for each correct answer.

Validation Logic: The "brains" of the quiz.

A series of if/else conditional blocks are used to validate each answer.

Validation is performed using exact string matching (e.g., answer == "Your Correct Answer"). This is the main part you will edit to create your own quiz.

Scoring System:

After the final question, the script calculates the percentage score by dividing the score by the total number of questions.

The final numbers are converted to strings using str() for clean concatenation and display.

🚀 How to Make Your Own Quiz
Customizing this framework is simple. Just follow these steps:

Open the .py script in your favorite text editor.

Change the Questions: Find each line that starts with answer = input(...). Replace the question string (e.g., "What does EC2 stand for? ") with your own custom question.

Set the Correct Answers: In the if statement immediately following your question, change the hard-coded string (e.g., "Elastic compute cloud") to the correct answer for your question.

Update the Final Score Calculation:

Count how many total questions you have.

At the end of the file, find the line: print("You scored " + str(score/7*100) + "%")

Change the 7 to match your total number of questions (e.g., score/10*100 if you have 10 questions).

That's it! You've created your own custom terminal quiz.

💡 How to Run the Game
Clone the repository (or download the script):

Bash

git clone [your-repo-url]
cd [your-repo-name]
Ensure you have Python 3 installed.

Run the script from your terminal:

Bash

python your_script_name.py
(Replace your_script_name.py with the actual name of your file.)

Type yes when prompted, and start playing!

🔮 Future Improvements
This project is a fantastic base. Here are some ways you can make it even better:

Case-Insensitive Validation: Use the .lower() method on the user's answer to accept answers regardless of capitalization.

Data-Driven Questions: The "next level" for this framework! Move the questions and answers out of the if/else blocks and into a more flexible data structure, like a dictionary or a list of objects.

Python

# Example of a more advanced structure
questions = {
    "What does EC2 stand for?": "Elastic compute cloud",
    "What does VPC stand for?": "Virtual Private Cloud"
}

for question, correct_answer in questions.items():
    answer = input(question)
    if answer.lower() == correct_answer.lower():
        # ...
External Question File: Load your questions from an external .json or .csv file. This way, you can build a massive question bank without ever touching the main Python logic file.

Question Randomization: Use the random.shuffle() module to shuffle the order of questions each time the game is played.
