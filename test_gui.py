import customtkinter as ctk 
from backend.students import Students

app = ctk.CTk()
frame1 = ctk.CTkFrame(app)
frame1.pack(pady=10)
frame2 = ctk.CTkFrame(app)
frame2.pack(pady=10)

students_list = []
def display():
    name = entry1.get()
    email = entry2.get()
    grade = entry3.get()

    student=Students(1,name,email,grade)
    students_list.append(student)

def stu_window():
    new_window=ctk.CTkToplevel()
    label4=ctk.CTkLabel(new_window,text="this is Student page")
    label4.pack(pady=10)

def show():
    text.delete("1.0", "end")
    for student in students_list:
        text.insert("end",f"{student.email} {student.name}\n")

label1 = ctk.CTkLabel(frame1, text="Name")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = ctk.CTkEntry(frame1)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2=ctk.CTkLabel(frame2,text="Email ")
label2.pack(pady=10)

entry2=ctk.CTkEntry(frame2,placeholder_text="Enter your email here")
entry2.pack(pady=10)

label3=ctk.CTkLabel(frame2,text="Grade")
label3.pack(pady=10)

entry3=ctk.CTkEntry(frame2,placeholder_text="Enter your grade here")
entry3.pack(pady=10)

button1=ctk.CTkButton(frame2,text="get student info",command=display)
button1.pack(pady=10)

button2=ctk.CTkButton(frame2,text="go to students page",command=stu_window)
button2.pack(pady=10)

button3=ctk.CTkButton(frame2,text="show students",command=show)
button3.pack(pady=10)

text=ctk.CTkTextbox(frame2,width=300,height=150)
text.pack(pady=10)

grade= ctk.CTkOptionMenu(frame2,values=["O", "A", "B", "C", "D"])
grade.pack(pady=10)
app.mainloop()
