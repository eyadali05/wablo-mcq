import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import json
from datetime import datetime

# Ms. Zarwina, change the path of LOGO_PNG, LOGO_ICO, QUESTIONS_DATA, if you want it to run on your device

LOGO_PNG = r"C:\Users\razer\Documents\UCSI\FiS [FDAEN]\May 2023\FBF1163 Fundamentals of Programming\Final Project\Project Code\quiz app\logo png.png"
LOGO_ICO = r"C:\Users\razer\Documents\UCSI\FiS [FDAEN]\May 2023\FBF1163 Fundamentals of Programming\Final Project\Project Code\quiz app\logo ico.ico"
QUESTIONS_DATA = r"C:\Users\razer\Documents\UCSI\FiS [FDAEN]\May 2023\FBF1163 Fundamentals of Programming\Final Project\Project Code\quiz app\questions.json"

def place_logo(window, image_path, desired_width, placement="center"):
    logo_image = Image.open(image_path)
    width, height = logo_image.size
    desired_height = int((height / width) * desired_width)
    logo_image = logo_image.resize((desired_width, desired_height), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(window, image=logo_photo)
    logo_label.image = logo_photo

    if placement == "top_left":
        logo_label.pack(anchor="nw", pady=20, padx=20)
    else:
        logo_label.pack(pady=20, padx=20)

class OurTeamWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Our Team")
        self.geometry("400x600")
        self.iconbitmap(LOGO_ICO)
        place_logo(self, LOGO_PNG, 100, placement="center")

        additional_text = (
            "Hi there! We are Foundation in Science [FDAEN] students at UCSI University, "
            "and this is our group final project submission for the Fundamentals of Programming Course [FBF1163]. "
            "The code should be available at https:/github.com/eyadali05 , in there you may also find other projects that may interest you"
        )
        ttk.Label(self, text=additional_text, font=("Arial", 10), wraplength=380).pack(pady=10)

        team_data = {
            "Eyad Mohamed": "1002266378",
            "Yehia Tarek": "1002266841",
            "Abdulaziz Fakhri": "1002265943",
            "Omar Ali": "1002266220",
            "Lina Tamer": "1002266720",
            "Tokollo Seripa": "1002266849",
        }

        team_frame = ttk.Frame(self)
        team_frame.pack(pady=20)

        ttk.Label(team_frame, text="Name", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5, sticky="nsew", ipadx=10, ipady=5)
        ttk.Label(team_frame, text="ID", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=5, sticky="nsew", ipadx=10, ipady=5)

        for row_index, (name, ID) in enumerate(team_data.items(), start=1):
            ttk.Label(team_frame, text=name, font=("Arial", 12)).grid(row=row_index, column=0, padx=10, pady=5, sticky="nsew", ipadx=10, ipady=5)
            ttk.Label(team_frame, text=ID, font=("Arial", 12)).grid(row=row_index, column=1, padx=10, pady=5, sticky="nsew", ipadx=10, ipady=5)



class MarkingScriptWindow(tk.Toplevel):
    def __init__(self, data):
        super().__init__()
        self.title("Marking Script")
        self.geometry("800x400")
        self.iconbitmap(LOGO_ICO)
        place_logo(self, LOGO_PNG, 100, placement="center")

        self.data_frame = ttk.Frame(self)
        self.data_frame.pack(pady=20)

        headers = ["Question", "Correct Answer", "Your Answer"]
        for i, header in enumerate(headers):
            anchor = "center" if i > 0 else "e"  # Right-align the first column, center-align others
            ttk.Label(self.data_frame, text=header, font=("Arial", 12, "bold")).grid(row=0, column=i, padx=10, pady=5, sticky="nsew", ipadx=10, ipady=5)
            self.data_frame.grid_columnconfigure(i, weight=1)  # Make columns expand equally

        self.exit_button = ttk.Button(self, text="Exit", command=self.destroy)
        self.exit_button.pack(pady=10)

        self.populate_data(data)

    def populate_data(self, data):
        row_index = 1
        for question_number, answers in data.items():
            ttk.Label(self.data_frame, text=question_number, font=("Arial", 12)).grid(row=row_index, column=0, padx=10, pady=5, sticky="nsew", ipadx=10, ipady=5)

            correct_choice_label = ttk.Label(self.data_frame, text=answers["correct_choice"], font=("Arial", 12))
            correct_choice_label.grid(row=row_index, column=1, padx=10, pady=5, sticky="nsew", ipadx=10, ipady=5)
            correct_choice_label.configure(background="#D0F0C0")  # Set the background to green-yellow

            selected_choice_label = ttk.Label(self.data_frame, text=answers["selected_choice"], font=("Arial", 12))
            selected_choice_label.grid(row=row_index, column=2, padx=10, pady=5, sticky="nsew", ipadx=10, ipady=5)
            if answers["selected_choice"] == answers["correct_choice"]:
                selected_choice_label.configure(background="green")  # Set the background to green
            else:
                selected_choice_label.configure(background="red")  # Set the background to red

            row_index += 1

class QuizResultsWindow(tk.Toplevel):
    def __init__(self, name, total_marks, total_questions, selected_answers):
        super().__init__()
        self.title("Quiz Results!")
        self.geometry("600x400")
        self.iconbitmap(LOGO_ICO)
        place_logo(self, LOGO_PNG, 100, placement="center")

        congrats_label = ttk.Label(
            self,
            text=f"Congratulations, {name}!",
            font=("Arial", 16, "bold"),
            foreground="green"
        )
        congrats_label.pack(pady=20)

        marks_label = ttk.Label(
            self,
            text=f"Total Marks: {total_marks}/{total_questions}",
            font=("Arial", 14)
        )
        marks_label.pack(pady=10)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        exit_button = ttk.Button(button_frame, text="Exit", command=self.destroy)
        exit_button.pack(side="left", padx=10)

        marking_script_button = ttk.Button(
            button_frame,
            text="Marking Script",
            command=self.open_marking_script,
        )
        marking_script_button.pack(side="left", padx=10)

        self.marking_script_window = None
        self.selected_answers = selected_answers

    def open_marking_script(self):
        if self.marking_script_window is None or not self.marking_script_window.winfo_exists():
            self.marking_script_window = MarkingScriptWindow(self.selected_answers)
            self.marking_script_window.mainloop()

    def append_to_script(self, question_number, data):
        ttk.Label(self.data_frame, text=question_number, font=("Arial", 12)).grid(row=question_number, column=0, padx=10, pady=5)
        ttk.Label(self.data_frame, text=data["correct_choice"], font=("Arial", 12)).grid(row=question_number, column=1, padx=10, pady=5)
        ttk.Label(self.data_frame, text=data["selected_choice"], font=("Arial", 12)).grid(row=question_number, column=2, padx=10, pady=5)


class QuizWindow(tk.Toplevel):
    def __init__(self, parent, name, questions):
        super().__init__(parent)
        self.title("Quiz")
        self.geometry("650x400+450+100")
        self.lift(parent)
        self.iconbitmap(LOGO_ICO)
        place_logo(self, LOGO_PNG, 100, placement="center")

        self.name = name
        self.questions = questions
        self.current_question = 0
        self.selected_answers = {}

        self.question_frame = tk.Frame(self)
        self.question_frame.pack(pady=20)

        self.question_title = ttk.Label(
            self.question_frame,
            text="",
            font=("Arial", 14),
            background="green",
            foreground="white"
        )
        self.question_title.pack(fill="x", padx=10, pady=10)

        self.choices = []
        self.selected_choice = tk.StringVar()

        for i in range(4):
            choice = ttk.Radiobutton(
                self.question_frame,
                text="",
                value=i + 1,
                variable=self.selected_choice,
            )
            self.choices.append(choice)
            choice.pack(pady=5)

        self.next_button = ttk.Button(self, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)


        self.total_marks = 0
        self.start_time = datetime.now()
        self.end_time = None

        self.result_window = None
        self.marking_script_window = None

        self.display_question()

    def display_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_title.config(text=question_data["question"])
            for i in range(4):
                self.choices[i].config(text=question_data["options"][i])
                self.choices[i].state(["!disabled"])
                self.choices[i].state(["!selected"])
            self.current_question += 1
        else:
            self.next_button.config(text="Submit", command=self.submit_quiz)
            self.end_time = datetime.now()
            self.print_quiz_results()

    def next_question(self):
        selected_choice = self.selected_choice.get()

        if not selected_choice:
            tk.messagebox.showwarning("No Choice Selected", "Please select a choice!")
        else:
            question_data = self.questions[self.current_question - 1]
            correct_choice = question_data["answer"]

            self.selected_answers[question_data["question"]] = {
                "selected_choice": self.choices[int(selected_choice) - 1]["text"],
                "correct_choice": correct_choice
            }

            if self.choices[int(selected_choice) - 1]["text"] == correct_choice:
                self.total_marks += 1

            self.display_question()

    def submit_quiz(self):
        self.destroy()  
        if self.result_window is None or not self.result_window.winfo_exists():
            result_window = QuizResultsWindow(self.name, self.total_marks, len(self.questions), self.selected_answers)
            result_window.mainloop()

    def print_quiz_results(self):
        total_questions = len(self.questions)
        total_correct_answers = self.total_marks
        elapsed_time = self.end_time - self.start_time

        result_text = "Quiz Results:\n"
        result_text += f"Total Questions: {total_questions}\n"
        result_text += f"Total Correct Answers: {total_correct_answers}\n"
        result_text += f"Start Time: {self.start_time}\n"
        result_text += f"End Time: {self.end_time}\n"
        result_text += f"Total Elapsed Time: {elapsed_time}\n\n"
        result_text += "Question-wise Answers:\n"
        for question, answers in self.selected_answers.items():
            result_text += f"Question: {question}\n"
            result_text += f"Selected Choice: {answers['selected_choice']}\n"
            result_text += f"Correct Choice: {answers['correct_choice']}\n\n"

        if self.result_window is not None and self.result_window.winfo_exists():
            self.result_window.append_to_script(result_text)
        if self.marking_script_window is not None and self.marking_script_window.winfo_exists():
            self.marking_script_window.append_to_script(result_text)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FBF1163 FoP Group Final Project")
        self.geometry("600x450")
        self.iconbitmap(LOGO_ICO)
        place_logo(self, LOGO_PNG, 300, placement="center")

        self.name_label = ttk.Label(self, text="Name:", font=("Arial", 14))
        self.name_label.pack(pady=5)

        self.name_entry = ttk.Entry(self, font=("Arial", 12))
        self.name_entry.pack(pady=10)

        start_button = ttk.Button(self, text="Start Quiz", command=self.start_quiz, width=20)
        start_button.pack(pady=10)

        start_button = ttk.Button(self, text="Our Team", command=self.open_team_window, width=20)
        start_button.pack(pady=10)

    def start_quiz(self):
        name = self.name_entry.get()
        print(f"New Entry: {name}")

        with open(QUESTIONS_DATA, "r") as file:
            quiz_data = json.load(file)
            questions = quiz_data["questions"]

        if len(questions) > 0:
            quiz_window = QuizWindow(self, name, questions)
            tk.messagebox.showinfo("You may start!", "Quiz has started, best of luck!")
        else:
            tk.messagebox.showerror("Error", "No questions found in the quiz data file!")
    
    def open_team_window(self):
        team_window = OurTeamWindow()
        team_window.mainloop()

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()