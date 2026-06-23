class Person:
    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email = email

    def display_details(self):
        print(f"""ID = {self.id}
Name = {self.name}
Email = {self.email}
""")    


class Students(Person):
    def __init__(self,id,name,email,grade):
        super().__init__(id,name,email)
        self.grade=grade
        self.enrolled_courses=[]

    def enroll_course(self,course):
        self.enrolled_courses.append(course) 
          

    def view_courses(self):
        print("Your Courses : ")
        for course in self.enrolled_courses:
            print(course.course_name)    

