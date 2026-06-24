import customtkinter as ctk 
from gui.students_page import open_students_page
from .trainers_page import open_trainers_page
from .courses_page import open_courses_page
from .knowledge_page import open_knowledge_page
from .faq_page import open_faq_page
from .prediction_page import open_prediction_page
from .enrollment_page import open_enrollment_page
from .progress_page import open_progress_page

app= ctk.CTk()
app.title("AI-SLMS Dashboard")
frame1= ctk.CTkFrame(app)
frame1.pack(pady=10)
frame2= ctk.CTkFrame(app)
frame2.pack(pady=10)
label1=ctk.CTkLabel(frame1,text=" AI-SLMS Dashboard ",font=("Arial",24))
label1.pack(pady=10)

button1=ctk.CTkButton(frame2,text="Students Page",command=open_students_page)
button1.grid(row=0,column=0,padx=10,pady=5)
button2=ctk.CTkButton(frame2,text="Trainers Page",command=open_trainers_page)
button2.grid(row=0,column=1,padx=10,pady=5)
button3=ctk.CTkButton(frame2,text="Courses Page",command=open_courses_page)
button3.grid(row=1,column=0,padx=10,pady=5)
button4=ctk.CTkButton(frame2,text="Knowledge Page",command=open_knowledge_page)
button4.grid(row=1,column=1,padx=10,pady=5)
button5=ctk.CTkButton(frame2,text="FAQ Page",command=open_faq_page)
button5.grid(row=2,column=0,padx=10,pady=5)
button6=ctk.CTkButton(frame2,text="Prediction Page",command=open_prediction_page)
button6.grid(row=2,column=1,padx=10,pady=5)
button7=ctk.CTkButton(frame2,text="Enrollment Page",command=open_enrollment_page)
button7.grid(row=3,column=0,padx=10,pady=5)
button8=ctk.CTkButton(frame2,text="Progress Page",command=open_progress_page)
button8.grid(row=3,column=1,padx=10,pady=5)

app.mainloop()