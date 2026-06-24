import customtkinter as ctk
from tkinter import messagebox
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

KNOWLEDGE_FILE = os.path.join(BASE_DIR, "data", "knowledge.txt")


def open_knowledge_page():

    window = ctk.CTkToplevel()
    window.title("Knowledge Base")
    window.geometry("750x600")

    title = ctk.CTkLabel(
        window,
        text="Knowledge Base Search",
        font=("Arial", 24)
    )
    title.pack(pady=15)

    topic_label = ctk.CTkLabel(
        window,
        text="Enter Topic"
    )
    topic_label.pack()

    topic_entry = ctk.CTkEntry(
        window,
        width=300
    )
    topic_entry.pack(pady=5)

    result_box = ctk.CTkTextbox(
        window,
        width=600,
        height=300
    )
    result_box.pack(pady=15)

    def search_topic():

        search = topic_entry.get().strip().lower()

        result_box.delete("1.0", "end")

        if not search:
            messagebox.showerror(
                "Error",
                "Please enter a topic"
            )
            return

        found = False

        try:

            with open(KNOWLEDGE_FILE, "r") as file:

                for line in file:

                    data = line.strip().split("|")

                    if len(data) == 3:

                        course = data[0]
                        topic = data[1]
                        information = data[2]

                        if search in topic.lower():

                            result_box.insert(
                                "end",
                                f"Course: {course}\n"
                                f"Topic: {topic}\n"
                                f"Information: {information}\n\n"
                            )

                            found = True

            if not found:

                result_box.insert(
                    "end",
                    "Topic not found."
                )

        except FileNotFoundError:

            result_box.insert(
                "end",
                "knowledge.txt not found."
            )

    search_btn = ctk.CTkButton(
        window,
        text="Search Topic",
        command=search_topic
    )

    search_btn.pack(pady=10)