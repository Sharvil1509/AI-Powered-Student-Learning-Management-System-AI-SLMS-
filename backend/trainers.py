from students import Person

class Trainers(Person) :
    def __init__(self,id,name,email,specialization):
        super().__init__(id,name,email)
        self.specialization = specialization
        self.assigned_courses = []

    def assign_course(self, course):
        self.assigned_courses.append(course)    

    def view_assigned_courses(self):
        print(f"\nCourses assigned to {self.name}:")

        if len(self.assigned_courses) == 0:
            print("No courses assigned.")

        for course in self.assigned_courses:
            print(course.course_name)