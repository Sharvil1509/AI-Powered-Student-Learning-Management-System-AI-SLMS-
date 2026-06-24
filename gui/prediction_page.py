import customtkinter as ctk
from tkinter import messagebox
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRAIN_DATA_FILE = os.path.join(BASE_DIR, "data", "traindata.txt")


def open_prediction_page():

    window = ctk.CTkToplevel()
    window.title("Text Prediction")
    window.geometry("750x600")

    title = ctk.CTkLabel(
        window,
        text="Text Prediction",
        font=("Arial", 24)
    )
    title.pack(pady=15)

    input_label = ctk.CTkLabel(
        window,
        text="Enter Incomplete Sentence"
    )
    input_label.pack()

    input_entry = ctk.CTkEntry(
        window,
        width=400
    )
    input_entry.pack(pady=5)

    prediction_box = ctk.CTkTextbox(
        window,
        width=600,
        height=300
    )
    prediction_box.pack(pady=15)

    def predict_text():

        prediction_box.delete("1.0", "end")

        user_input = input_entry.get().strip()

        if not user_input:

            messagebox.showerror(
                "Error",
                "Please enter a sentence"
            )
            return

        predictions = []

        try:

            with open(TRAIN_DATA_FILE, "r") as file:

                for sentence in file:

                    sentence = sentence.strip()

                    if sentence.lower().startswith(user_input.lower()):

                        words = sentence.split()

                        predictions.append(words[-1])

            if predictions:

                for word in predictions:

                    prediction_box.insert(
                        "end",
                        f"{word}\n"
                    )

            else:

                prediction_box.insert(
                    "end",
                    "No predictions found."
                )

        except FileNotFoundError:

            prediction_box.insert(
                "end",
                "traindata.txt not found."
            )

    predict_btn = ctk.CTkButton(
        window,
        text="Predict",
        command=predict_text
    )

    predict_btn.pack(pady=10)