import customtkinter as ctk
from tkinter import messagebox
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENROLLMENT_FILE = os.path.join(
    BASE_DIR,
    "data",
    "enrollments.txt"
)


def open_progress_page():

    window = ctk.CTkToplevel()

    window.title("Progress Management")
    window.geometry("750x600")

    title = ctk.CTkLabel(
        window,
        text="Progress Management",
        font=("Arial", 24)
    )

    title.pack(pady=15)

    ctk.CTkLabel(
        window,
        text="Student ID"
    ).pack()

    student_entry = ctk.CTkEntry(
        window,
        width=250
    )

    student_entry.pack(pady=5)

    ctk.CTkLabel(
        window,
        text="Progress (%)"
    ).pack()

    progress_entry = ctk.CTkEntry(
        window,
        width=250
    )

    progress_entry.pack(pady=5)

    def update_progress():

        student_id = student_entry.get()

        try:

            progress = int(
                progress_entry.get()
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Progress must be a number"
            )

            return

        updated_lines = []
        found = False

        try:

            with open(
                ENROLLMENT_FILE,
                "r"
            ) as file:

                for line in file:

                    data = line.strip().split(",")

                    if data[0] == student_id:

                        if len(data) >= 2:

                            updated_lines.append(
                                f"{data[0]},"
                                f"{data[1]},"
                                f"{progress}\n"
                            )

                            found = True

                    else:

                        updated_lines.append(line)

            with open(
                ENROLLMENT_FILE,
                "w"
            ) as file:

                file.writelines(
                    updated_lines
                )

            if found:

                messagebox.showinfo(
                    "Success",
                    "Progress Updated"
                )

            else:

                messagebox.showerror(
                    "Error",
                    "Student not enrolled"
                )

        except FileNotFoundError:

            messagebox.showerror(
                "Error",
                "enrollments.txt not found"
            )

    update_btn = ctk.CTkButton(
        window,
        text="Update Progress",
        command=update_progress
    )

    update_btn.pack(pady=10)

    progress_box = ctk.CTkTextbox(
        window,
        width=600,
        height=250
    )

    progress_box.pack(pady=15)

    def view_progress():

        progress_box.delete(
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

                    if len(data) == 3:

                        progress_box.insert(
                            "end",
                            f"Student ID: {data[0]} | "
                            f"Course ID: {data[1]} | "
                            f"Progress: {data[2]}%\n"
                        )

        except FileNotFoundError:

            progress_box.insert(
                "end",
                "No progress data found."
            )

    view_btn = ctk.CTkButton(
        window,
        text="View Progress",
        command=view_progress
    )

    view_btn.pack(pady=5)