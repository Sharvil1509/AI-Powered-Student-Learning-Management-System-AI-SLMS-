class Enrollment :
    def __init__(self,student,course):
        self.student=student
        self.course=course
        self.progress_percentage= 0



    def updated_progress(self,progress):    
        self.progress_percentage=progress

    def diaplay_progress(self):
        print(f"Your Progress : {self.progress_percentage} %")


