import customtkinter as ctk
from tkinter import messagebox
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KNOWLEDGE_FILE = os.path.join(BASE_DIR, "data", "knowledge.txt")


def open_faq_page():

    window = ctk.CTkToplevel()
    window.title("FAQ Assistant")
    window.geometry("750x600")

    title = ctk.CTkLabel(
        window,
        text="FAQ Assistant",
        font=("Arial", 24)
    )
    title.pack(pady=15)

    question_label = ctk.CTkLabel(
        window,
        text="Ask a Question"
    )
    question_label.pack(pady=5)

    question_entry = ctk.CTkEntry(
        window,
        width=400
    )
    question_entry.pack(pady=5)

    answer_box = ctk.CTkTextbox(
        window,
        width=600,
        height=300
    )
    answer_box.pack(pady=15)

    def get_answer():

        answer_box.delete("1.0", "end")

        question = question_entry.get().lower().strip()

        if not question:
            messagebox.showerror(
                "Error",
                "Please enter a question"
            )
            return

        ignore_words = [
            "what",
            "is",
            "a",
            "an",
            "the"
        ]

        keyword = ""

        for word in question.split():

            word = word.replace("?", "")

            if word not in ignore_words:
                keyword = word
                break

        found = False

        try:

            with open(KNOWLEDGE_FILE, "r") as file:

                for line in file:

                    data = line.strip().split("|")

                    if len(data) != 3:
                        continue

                    course = data[0]
                    topic = data[1]
                    information = data[2]

                    if (
                        keyword in course.lower()
                        or keyword in topic.lower()
                    ):

                        answer_box.insert(
                            "end",
                            f"{information}\n\n"
                        )

                        found = True

            if not found:
                answer_box.insert(
                    "end",
                    "Answer not found."
                )

        except FileNotFoundError:

            answer_box.insert(
                "end",
                "knowledge.txt not found."
            )

    ask_button = ctk.CTkButton(
        window,
        text="Get Answer",
        command=get_answer
    )

    ask_button.pack(pady=10)