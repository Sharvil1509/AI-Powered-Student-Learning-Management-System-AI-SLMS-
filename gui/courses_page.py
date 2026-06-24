import customtkinter as ctk
from tkinter import messagebox
import os

from backend.courses import Courses
from backend.trainers import Trainers

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COURSE_FILE = os.path.join(BASE_DIR, "data", "courses.txt")
TRAINER_FILE = os.path.join(BASE_DIR, "data", "trainers.txt")


def open_courses_page():

    window = ctk.CTkToplevel()
    window.title("Course Management")
    window.geometry("750x650")

    title = ctk.CTkLabel(
        window,
        text="Course Management",
        font=("Arial", 24)
    )
    title.pack(pady=15)

    # Course ID
    ctk.CTkLabel(window, text="Course ID").pack()

    course_id_entry = ctk.CTkEntry(window, width=250)
    course_id_entry.pack(pady=5)

    # Course Name
    ctk.CTkLabel(window, text="Course Name").pack()

    course_name_entry = ctk.CTkEntry(window, width=250)
    course_name_entry.pack(pady=5)

    # Duration
    ctk.CTkLabel(window, text="Duration").pack()

    duration_entry = ctk.CTkEntry(window, width=250)
    duration_entry.pack(pady=5)

    # Trainer ID
    ctk.CTkLabel(window, text="Trainer ID").pack()

    trainer_id_entry = ctk.CTkEntry(window, width=250)
    trainer_id_entry.pack(pady=5)

    def add_course():

        try:

            course_id = int(course_id_entry.get())
            course_name = course_name_entry.get()
            duration = duration_entry.get()
            trainer_id = int(trainer_id_entry.get())

            trainer_found = None

            with open(TRAINER_FILE, "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if int(data[0]) == trainer_id:

                        trainer_found = Trainers(
                            int(data[0]),
                            data[1],
                            data[2],
                            data[3]
                        )

                        break

            if trainer_found is None:

                messagebox.showerror(
                    "Error",
                    "Trainer ID not found"
                )
                return

            course = Courses(
                course_id,
                course_name,
                duration,
                trainer_found
            )

            with open(COURSE_FILE, "a") as file:

                file.write(
                    f"{course.course_id},"
                    f"{course.course_name},"
                    f"{course.duration},"
                    f"{course.trainer.id}\n"
                )

            messagebox.showinfo(
                "Success",
                f"{course_name} added successfully"
            )

            course_id_entry.delete(0, "end")
            course_name_entry.delete(0, "end")
            duration_entry.delete(0, "end")
            trainer_id_entry.delete(0, "end")

        except ValueError:

            messagebox.showerror(
                "Error",
                "Invalid input"
            )

    add_btn = ctk.CTkButton(
        window,
        text="Add Course",
        command=add_course
    )
    add_btn.pack(pady=10)

    course_box = ctk.CTkTextbox(
        window,
        width=600,
        height=220
    )
    course_box.pack(pady=10)

    def view_courses():

        course_box.delete("1.0", "end")

        try:

            with open(COURSE_FILE, "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 4:

                        course_box.insert(
                            "end",
                            f"Course ID: {data[0]} | "
                            f"Course: {data[1]} | "
                            f"Duration: {data[2]} | "
                            f"Trainer ID: {data[3]}\n"
                        )

        except FileNotFoundError:

            course_box.insert(
                "end",
                "courses.txt not found."
            )

    view_btn = ctk.CTkButton(
        window,
        text="View Courses",
        command=view_courses
    )

    view_btn.pack(pady=5)