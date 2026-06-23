class Courses:
    def __init__(self,course_id,course_name,duration,trainer):
        self.course_id = course_id
        self.course_name = course_name
        self.duration = duration
        self.trainer = trainer


    def display_course(self):
        print(f"""Course Details :-
Course ID : {self.course_id}
Course Name : {self.course_name}
Course Duration : {self.duration}
Course Trainer : {self.trainer.name}""")    
        

