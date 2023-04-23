import json
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
import os


class App(ttk.Window):

    def __init__(self):
        super().__init__()

        self.title("WattWise QuestionBank Generator")
        self.state("zoomed")

        # Initialize an empty questions dictionary
        self.questions = {}

        self.add_components()

    # Method to add question inside the questions dictionary
    def add_question(self):
        question = self.question_text.get(1.0, "end-1c")
        option_a = self.option_a_entry.get()
        option_b = self.option_b_entry.get()
        option_c = self.option_c_entry.get()
        option_d = self.option_d_entry.get()
        correct_answer = self.correct_answer_combobox.get()

        # Add the question to the dictionary
        self.questions[question] = [option_a, option_b,
                                    option_c, option_d, correct_answer]

        # Clear the entry fields
        self.question_text.delete(1.0, tk.END)
        self.option_a_entry.delete(0, tk.END)
        self.option_b_entry.delete(0, tk.END)
        self.option_c_entry.delete(0, tk.END)
        self.option_d_entry.delete(0, tk.END)

        # Update the preview textarea
        self.preview_text.delete('1.0', tk.END)
        for q, opts in self.questions.items():
            self.preview_text.insert(tk.END, f'{q}?\n')
            self.preview_text.insert(tk.END, f'A. {opts[0]}\n')
            self.preview_text.insert(tk.END, f'B. {opts[1]}\n')
            self.preview_text.insert(tk.END, f'C. {opts[2]}\n')
            self.preview_text.insert(tk.END, f'D. {opts[3]}\n')
            self.preview_text.insert(tk.END, f'Correct Answer: {opts[4]}\n')
            self.preview_text.insert(tk.END, '\n')


    # Method when the save button is clicked
    def save_questions(self):
        path = os.path.join(os.getcwd(), f"question_bank\\{self.subject_combobox.get()}.json")

        # IF the json file is already created, proceed to append_json method
        if os.path.exists(path):
            print("File does exist", path)
            self.append_json(path)

        # ELSE, create a new folder and proceed to write_json method
        else:
            os.mkdir("question_bank")
            self.write_json(path)

        self.questions = {}


    # Method to append questions in an existing JSON subject question file
    def append_json(self, path):

        # Read the existing JSON file
        with open(path, 'r') as file:
            data = json.load(file)

        # Append a new objects to the array
        for q, opts in self.questions.items():
            data.append({
                "question": q,
                "options": [
                    f"A. {opts[0]}",
                    f"B. {opts[1]}",
                    f"C. {opts[2]}",
                    f"D. {opts[3]}",
                ],
                "correct_answer": opts[4]
            })

        # Write the updated JSON data
        # back to the file
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)

    # Method to write questions in a JSON subject question file
    def write_json(self, path):
        print("File does not exist", path)
        # print(self.questions.items())
        with open(path, 'w+') as f:
            questions = self.format_questions_to_write_in_json([])
            json.dump(questions, f)


    # Method to format questions to write in json
    def format_questions_to_write_in_json(self, to_save):
        return [
            {
                "question": q,
                "options": [
                    f"A. {opts[0]}",
                    f"B. {opts[1]}",
                    f"C. {opts[2]}",
                    f"D. {opts[3]}",
                ],
                "correct_answer": opts[4]
            }
            for q, opts in self.questions.items()
        ]


    # Method to create the GUI
    def create_GUI(self):
        # Create the frames
        preview_frame = ttk.Frame(self)
        preview_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        fields_frame = ttk.Frame(self)
        fields_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create the preview textarea
        self.preview_text = ttk.ScrolledText(preview_frame, font=('Arial', 11))
        self.preview_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create Subject Combobox
        self.selected_subject = tk.StringVar()

        subject_label = ttk.Label(fields_frame, text='Subjects:')
        subject_label.pack(side=tk.TOP, padx=10, pady=10)

        self.subject_combobox = ttk.Combobox(
            fields_frame, textvariable=self.selected_subject, state='readonly')
        self.subject_combobox['values'] = ('ESAS', 'Mathematics', 'EEPS')
        self.subject_combobox.current(0)
        self.subject_combobox.pack(side=tk.TOP, padx=10, pady=3)

        # Create the fields
        question_label = ttk.Label(fields_frame, text='Question:')
        question_label.pack(side=tk.TOP, padx=10, pady=10)

        self.question_text = ttk.Text(fields_frame, height=3)
        self.question_text.pack(side=tk.TOP, padx=10, pady=(3, 20))

        option_a_label = ttk.Label(fields_frame, text='Option A:')
        option_a_label.pack(side=tk.TOP, padx=10, pady=3)

        self.option_a_entry = ttk.Entry(fields_frame, width=50)
        self.option_a_entry.pack(side=tk.TOP, padx=10, pady=3)

        option_b_label = ttk.Label(fields_frame, text='Option B:')
        option_b_label.pack(side=tk.TOP, padx=10, pady=10)

        self.option_b_entry = ttk.Entry(fields_frame, width=50)
        self.option_b_entry.pack(side=tk.TOP, padx=10, pady=3)

        option_c_label = ttk.Label(fields_frame, text='Option C:')
        option_c_label.pack(side=tk.TOP, padx=10, pady=10)

        self.option_c_entry = ttk.Entry(fields_frame, width=50)
        self.option_c_entry.pack(side=tk.TOP, padx=10, pady=3)

        option_d_label = ttk.Label(fields_frame, text='Option D:')
        option_d_label.pack(side=tk.TOP, padx=10, pady=3)

        self.option_d_entry = ttk.Entry(fields_frame, width=50)
        self.option_d_entry.pack(side=tk.TOP, padx=10, pady=10)

        # Create Correct Answer Combobox
        self.selected_correct_answer = tk.StringVar()

        correct_answer_label = ttk.Label(fields_frame, text='Correct Answer:')
        correct_answer_label.pack(side=tk.TOP, padx=10, pady=10)

        self.correct_answer_combobox = ttk.Combobox(
            fields_frame, textvariable=self.selected_correct_answer, state='readonly')
        self.correct_answer_combobox['values'] = ('A', 'B', 'C', 'D')
        self.correct_answer_combobox.current(0)
        self.correct_answer_combobox.pack(side=tk.TOP, padx=10, pady=(3, 20))

        # Create Buttons
        add_button = ttk.Button(
            fields_frame, text='Add Question', command=self.add_question)
        add_button.pack(side=tk.TOP, padx=10, pady=10)

        save_button = ttk.Button(
            fields_frame, text='Save Questions', bootstyle="success.TButton", command=self.save_questions)
        save_button.pack(side=tk.TOP, padx=10, pady=10)


# Run the application
if __name__ == '__main__':
    App().mainloop()
