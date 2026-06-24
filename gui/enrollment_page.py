import customtkinter as ctk
from tkinter import messagebox
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STUDENT_FILE = os.path.join(BASE_DIR, "data", "students.txt")
COURSE_FILE = os.path.join(BASE_DIR, "data", "courses.txt")
ENROLLMENT_FILE = os.path.join(BASE_DIR, "data", "enrollments.txt")


def open_enrollment_page():

    window = ctk.CTkToplevel()
    window.title("Enrollment Management")
    window.geometry("750x600")

    title = ctk.CTkLabel(
        window,
        text="Enrollment Management",
        font=("Arial", 24)
    )
    title.pack(pady=15)

    # Student ID

    ctk.CTkLabel(
        window,
        text="Student ID"
    ).pack()

    student_entry = ctk.CTkEntry(
        window,
        width=250
    )
    student_entry.pack(pady=5)

    # Course ID

    ctk.CTkLabel(
        window,
        text="Course ID"
    ).pack()

    course_entry = ctk.CTkEntry(
        window,
        width=250
    )
    course_entry.pack(pady=5)

    def enroll_student():

        student_id = student_entry.get()
        course_id = course_entry.get()

        if not student_id or not course_id:

            messagebox.showerror(
                "Error",
                "Fill all fields"
            )

            return

        student_found = False
        course_found = False

        try:

            with open(STUDENT_FILE, "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if data[0] == student_id:

                        student_found = True
                        break

            with open(COURSE_FILE, "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if data[0] == course_id:

                        course_found = True
                        break

            if not student_found:

                messagebox.showerror(
                    "Error",
                    "Student ID not found"
                )

                return

            if not course_found:

                messagebox.showerror(
                    "Error",
                    "Course ID not found"
                )

                return

            with open(
                ENROLLMENT_FILE,
                "a"
            ) as file:

                file.write(
                    f"{student_id},{course_id}\n"
                )

            messagebox.showinfo(
                "Success",
                "Student enrolled successfully"
            )

            student_entry.delete(0, "end")
            course_entry.delete(0, "end")

        except FileNotFoundError:

            messagebox.showerror(
                "Error",
                "Required file not found"
            )

    enroll_btn = ctk.CTkButton(
        window,
        text="Enroll Student",
        command=enroll_student
    )

    enroll_btn.pack(pady=10)

    enrollment_box = ctk.CTkTextbox(
        window,
        width=600,
        height=250
    )

    enrollment_box.pack(pady=15)

    def view_enrollments():

        enrollment_box.delete(
            "1.0",
            "end"
        )

        try:

            with open(
                ENROLLMENT_FILE,
                "r"
            ) as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 2:

                        enrollment_box.insert(
                            "end",
                            f"Student ID: {data[0]} | "
                            f"Course ID: {data[1]}\n"
                        )

        except FileNotFoundError:

            enrollment_box.insert(
                "end",
                "No enrollments found."
            )

    view_btn = ctk.CTkButton(
        window,
        text="View Enrollments",
        command=view_enrollments
    )

    view_btn.pack(pady=5)