import customtkinter as ctk
from tkinter import messagebox
import os

from backend.trainers import Trainers

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRAINER_FILE = os.path.join(BASE_DIR, "data", "trainers.txt")


def open_trainers_page():

    window = ctk.CTkToplevel()
    window.title("Trainer Management")
    window.geometry("700x600")

    title = ctk.CTkLabel(
        window,
        text="Trainer Management",
        font=("Arial", 24)
    )
    title.pack(pady=15)

    # Trainer ID
    id_label = ctk.CTkLabel(window, text="Trainer ID")
    id_label.pack()

    id_entry = ctk.CTkEntry(window, width=250)
    id_entry.pack(pady=5)

    # Trainer Name
    name_label = ctk.CTkLabel(window, text="Trainer Name")
    name_label.pack()

    name_entry = ctk.CTkEntry(window, width=250)
    name_entry.pack(pady=5)

    # Email
    email_label = ctk.CTkLabel(window, text="Email")
    email_label.pack()

    email_entry = ctk.CTkEntry(window, width=250)
    email_entry.pack(pady=5)

    # Specialization
    specialization_label = ctk.CTkLabel(
        window,
        text="Specialization"
    )
    specialization_label.pack()

    specialization_entry = ctk.CTkEntry(window, width=250)
    specialization_entry.pack(pady=5)

    def add_trainer():

        try:

            trainer_id = int(id_entry.get())
            name = name_entry.get()
            email = email_entry.get()
            specialization = specialization_entry.get()

            if not name or not email or not specialization:
                messagebox.showerror(
                    "Error",
                    "Please fill all fields"
                )
                return

            trainer = Trainers(
                trainer_id,
                name,
                email,
                specialization
            )

            with open(TRAINER_FILE, "a") as file:
                file.write(
                    f"{trainer.id},"
                    f"{trainer.name},"
                    f"{trainer.email},"
                    f"{trainer.specialization}\n"
                )

            messagebox.showinfo(
                "Success",
                f"{name} added successfully"
            )

            id_entry.delete(0, "end")
            name_entry.delete(0, "end")
            email_entry.delete(0, "end")
            specialization_entry.delete(0, "end")

        except ValueError:
            messagebox.showerror(
                "Error",
                "Trainer ID must be a number"
            )

    add_btn = ctk.CTkButton(
        window,
        text="Add Trainer",
        command=add_trainer
    )
    add_btn.pack(pady=10)

    trainer_box = ctk.CTkTextbox(
        window,
        width=500,
        height=200
    )
    trainer_box.pack(pady=10)

    def view_trainers():

        trainer_box.delete("1.0", "end")

        try:

            with open(TRAINER_FILE, "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 4:
                        trainer_box.insert(
                            "end",
                            f"ID: {data[0]} | "
                            f"Name: {data[1]} | "
                            f"Email: {data[2]} | "
                            f"Specialization: {data[3]}\n"
                        )

        except FileNotFoundError:

            trainer_box.insert(
                "end",
                "trainers.txt not found."
            )

    view_btn = ctk.CTkButton(
        window,
        text="View Trainers",
        command=view_trainers
    )
    view_btn.pack(pady=5)