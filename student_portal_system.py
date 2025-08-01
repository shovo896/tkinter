import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.subjects = {}

    def add_subject(self, subject, score):
        self.subjects[subject] = int(score)

    def calculate_gpa(self):
        if not self.subjects:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)

    def get_grade(self, score):
        if score >= 90:
            return "A+"
        elif score >= 80:
            return "A"
        elif score >= 70:
            return "B"
        elif score >= 60:
            return "C"
        elif score >= 50:
            return "D"
        else:
            return "F"

    def __str__(self):
        output = f"{self.name}, GPA: {self.calculate_gpa():.2f}\n\nSubject:\n"
        for subject, score in self.subjects.items():
            grade = self.get_grade(score)
            output += f"  {subject}: {score}; {grade}\n"
        return output.strip()

class StudentPortalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Portal System")
        self.students = {}

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="Student Portal System", font=("Arial", 18, "bold"))
        title.grid(row=0, column=0, columnspan=4, pady=10)

        # Labels
        tk.Label(self.root, text="Student ID:").grid(row=1, column=0)
        tk.Label(self.root, text="Name:").grid(row=2, column=0)
        tk.Label(self.root, text="Subject:").grid(row=3, column=0)
        tk.Label(self.root, text="Score:").grid(row=4, column=0)

        # Entries
        self.id_entry = tk.Entry(self.root)
        self.name_entry = tk.Entry(self.root)
        self.subject_entry = tk.Entry(self.root)
        self.score_entry = tk.Entry(self.root)

        self.id_entry.grid(row=1, column=1)
        self.name_entry.grid(row=2, column=1)
        self.subject_entry.grid(row=3, column=1)
        self.score_entry.grid(row=4, column=1)

        # Buttons
        tk.Button(self.root, text="Add Student", command=self.add_student).grid(row=1, column=2)
        tk.Button(self.root, text="Add Subject", command=self.add_subject).grid(row=2, column=2)
        tk.Button(self.root, text="View All Students", command=self.view_all_students).grid(row=3, column=2)
        tk.Button(self.root, text="View Top Student", command=self.view_top_student).grid(row=4, column=2)
        tk.Button(self.root, text="Save Data", command=self.save_data).grid(row=5, column=2)

        # Text display
        self.display = tk.Text(self.root, width=60, height=15)
        self.display.grid(row=6, column=0, columnspan=4, pady=10)

    def add_student(self):
        sid = self.id_entry.get()
        name = self.name_entry.get()
        if sid and name:
            if sid not in self.students:
                self.students[sid] = Student(sid, name)
                messagebox.showinfo("Success", f"Student '{name}' added.")
            else:
                messagebox.showwarning("Warning", "Student ID already exists.")
        else:
            messagebox.showerror("Error", "Please fill both Student ID and Name.")

    def add_subject(self):
        sid = self.id_entry.get()
        subject = self.subject_entry.get()
        score = self.score_entry.get()

        if sid in self.students and subject and score.isdigit():
            self.students[sid].add_subject(subject, int(score))
            messagebox.showinfo("Success", f"Subject '{subject}' added.")
        else:
            messagebox.showerror("Error", "Invalid student ID or score.")

    def view_all_students(self):
        self.display.delete("1.0", tk.END)
        for i, student in enumerate(self.students.values(), 1):
            self.display.insert(tk.END, f"{i}. {student}\n\n")

    def view_top_student(self):
        if not self.students:
            self.display.delete("1.0", tk.END)
            self.display.insert(tk.END, "No students available.")
            return

        top = max(self.students.values(), key=lambda s: s.calculate_gpa())
        self.display.delete("1.0", tk.END)
        self.display.insert(tk.END, f"Top Student:\n{top}")

    def save_data(self):
        with open("students.txt", "w") as f:
            for student in self.students.values():
                f.write(str(student) + "\n\n")
        messagebox.showinfo("Saved", "Student data saved to 'students.txt'.")

# Launch the app
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentPortalApp(root)
    root.mainloop()
