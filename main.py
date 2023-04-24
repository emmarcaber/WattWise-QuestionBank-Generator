"""WattWise QuestionBank Generator"""

import json
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
from tkinter import messagebox
import os


class App(ttk.Window):

    def __init__(self):
        super().__init__()

        self.title("WattWise QuestionBank Generator")
        self.state("zoomed")

        # Initialize an empty questions dictionary
        self.questions = {}

        self.create_GUI()



    # Method when add question button is clicked
    def add_question(self):

        # Get the fields entered by the user
        question = self.question_text.get(1.0, "end-1c")
        option_a = self.option_a_entry.get()
        option_b = self.option_b_entry.get()
        option_c = self.option_c_entry.get()
        option_d = self.option_d_entry.get()
        correct_answer = self.correct_answer_combobox.get()

        # IF there is one field empty, show an error
        if question == "" or option_a == "" or option_b == "" or option_c == "" or option_d == "":
            messagebox.showerror("Error", "Please input all question fields!")

        # ELSE, proceed to adding question to the preview and question dictionary
        else:
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
                self.preview_text.insert(tk.END, f'{q}\n')
                self.preview_text.insert(tk.END, f'A. {opts[0]}\n')
                self.preview_text.insert(tk.END, f'B. {opts[1]}\n')
                self.preview_text.insert(tk.END, f'C. {opts[2]}\n')
                self.preview_text.insert(tk.END, f'D. {opts[3]}\n')
                self.preview_text.insert(
                    tk.END, f'Correct Answer: {opts[4]}\n')
                self.preview_text.insert(tk.END, '\n')



    # Method when the save questions button is clicked
    def save_questions(self):
        path = os.path.join(
            os.getcwd(), f"question_bank\\{self.category_combobox.get()}.json")

        # Ask confirmatiion to save the questions
        confirm_to_save = messagebox.askyesno(
            "Confirm Save", 
            f"Are you sure you want to save the new {self.category_combobox.get()} questions?")
        
        # IF yes, proceed to adding the questions
        if confirm_to_save:

            # IF the json file is already created, proceed to append_json method
            if os.path.exists(path):
                self.append_json(path)

            # ELSE, create a new folder and proceed to write_json method
            else:
                # Check if the question_bank folder already existed
                # If not, create the question_bank folder
                if not os.path.isdir("question_bank"):
                    os.mkdir("question_bank")
                self.write_json(path)

            # Empty the questions dictionary and
            # empty also the preview_text
            self.questions = {}
            self.preview_text.delete('1.0', tk.END)

            messagebox.showinfo("Success", "The questions has been saved!")



    # Method to append questions in an existing JSON category question file
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



    # Method to write questions in a JSON category question file
    def write_json(self, path):
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
        fields_frame = ttk.Frame(self)
        fields_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        preview_frame = ttk.Frame(self)
        preview_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create the preview textarea
        self.preview_text = ttk.ScrolledText(preview_frame, font=('Arial', 11))
        self.preview_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create category Combobox
        self.selected_category = tk.StringVar()

        category_label = ttk.Label(fields_frame, text='Categories:')
        category_label.pack(side=tk.TOP, padx=10, pady=10)

        self.category_combobox = ttk.Combobox(
            fields_frame, textvariable=self.selected_category, state='readonly')
        self.category_combobox['values'] = ('ESAS', 'Mathematics', 'EEPS')
        self.category_combobox.current(0)
        self.category_combobox.pack(side=tk.TOP, padx=10, pady=3)

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
