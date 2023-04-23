# WattWise-QuestionBank-Generator
A Python Program to generate questions in a JSON file for WattWise : Kiosk Test Generator and Checker.

## Usage
1. __Clone__ the repository.

    ```
        git clone https://github.com/emmarcaber/WattWise-QuestionBank-Generator.git
    ```

2. Run the command:

    ```
        py main.py
    ```

## JSON Question Format
The questions are inside the question_bank folder generated in a JSON file like this:

    ```
    [
        {
            "question": (The question here),
            "options": [
                'A. (option A here)',
                'B. (option B here)',
                'C. (option C here)',
                'D. (option D here)',
            ],
            "correct_answer": (correct answer here)
        }
    ]
    ```