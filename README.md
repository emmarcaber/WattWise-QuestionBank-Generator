# WattWise-QuestionBank-Generator
A Python program to generate questions in a JSON file for WattWise : Kiosk Test Generator and Checker.

![Main Window with Confirmation](https://i.ibb.co/StYR19D/image.png)

## Usage
1. __Clone__ the repository.

    ```
    git clone https://github.com/emmarcaber/WattWise-QuestionBank-Generator.git
    ```

2. __Run__ the command:

    ```
    py main.py
    ```

## JSON Question Format
The questions are inside the question_bank folder generated in a JSON file like this:
    
    [
        {
            "sub-category": "(Sub-category here)",
            "question": (The question here),
            "options": [
                'A. (option A here)',
                'B. (option B here)',
                'C. (option C here)',
                'D. (option D here)',
            ],
            "correct_answer": (correct answer here)
        }
        {
            "sub-category": "(Sub-category here)",
            "question": (Then another question here),
            "options": [
                'A. (option A here)',
                'B. (option B here)',
                'C. (option C here)',
                'D. (option D here)',
            ],
            "correct_answer": (correct answer here)
        }, ...
    ]
    
