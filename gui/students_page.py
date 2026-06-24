import customtkinter as ctk
from tkinter import messagebox
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STUDENT_FILE = os.path.join(BASE_DIR, "data", "students.txt")
from backend.students import Students


def open_students_page():

    window = ctk.CTkToplevel()
    window.title("Students Management")
    window.geometry("700x600")

    title = ctk.CTkLabel(
        window,
        text="Student Management",
        font=("Arial", 24)
    )
    title.pack(pady=15)

    # Student ID
    id_label = ctk.CTkLabel(window, text="Student ID")
    id_label.pack()

    id_entry = ctk.CTkEntry(window, width=250)
    id_entry.pack(pady=5)

    # Name
    name_label = ctk.CTkLabel(window, text="Student Name")
    name_label.pack()

    name_entry = ctk.CTkEntry(window, width=250)
    name_entry.pack(pady=5)

    # Email
    email_label = ctk.CTkLabel(window, text="Email")
    email_label.pack()

    email_entry = ctk.CTkEntry(window, width=250)
    email_entry.pack(pady=5)

    # Grade
    grade_label = ctk.CTkLabel(window, text="Grade")
    grade_label.pack()

    grade_entry = ctk.CTkEntry(window, width=250)
    grade_entry.pack(pady=5)

    def add_student():

        try:

            student_id = int(id_entry.get())
            name = name_entry.get()
            email = email_entry.get()
            grade = grade_entry.get()

            if not name or not email or not grade:
                messagebox.showerror(
                    "Error",
                    "Please fill all fields"
                )
                return

            student = Students(
                student_id,
                name,
                email,
                grade
            )

            with open(STUDENT_FILE, "a") as file:
                file.write(
                    f"{student.id},"
                    f"{student.name},"
                    f"{student.email},"
                    f"{student.grade}\n"
                )

            messagebox.showinfo(
                "Success",
                f"{name} added successfully"
            )

            id_entry.delete(0, "end")
            name_entry.delete(0, "end")
            email_entry.delete(0, "end")
            grade_entry.delete(0, "end")

        except ValueError:
            messagebox.showerror(
                "Error",
                "Student ID must be a number"
            )

    add_btn = ctk.CTkButton(
        window,
        text="Add Student",
        command=add_student
    )
    add_btn.pack(pady=10)

    student_box = ctk.CTkTextbox(
        window,
        width=500,
        height=200
    )
    student_box.pack(pady=10)

    def view_students():

        student_box.delete("1.0", "end")

        try:
            with open(STUDENT_FILE, "r") as file:

                for line in file:
                    student_box.insert("end", line)

        except FileNotFoundError:
            student_box.insert(
                "end",
                "students.txt not found."
            )

    view_btn = ctk.CTkButton(
        window,
        text="View Students",
        command=view_students
    )
    view_btn.pack(pady=5)