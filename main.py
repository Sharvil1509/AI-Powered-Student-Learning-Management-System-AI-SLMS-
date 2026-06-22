from students import Students
from trainers import Trainers
from courses import Courses
from enrollment import Enrollment
from knowledge import Knowledge


students = []
trainers = []
courses = []
enrollments = []
knowledge_list=[]

with open("knowledge.txt","r") as file:
   for line in file:
      data = line.strip().split("|")
      knowledge = Knowledge(
            data[0],
            data[1],
            data[2]
        )
      knowledge_list.append(knowledge)

while True:

    print("\n1. Add Student")
    print("2. Add Trainer")
    print("3. Create Course")
    print("4. Enroll Student")
    print("5. Update Progress")
    print("6. View Students")
    print("7. View Courses")
    print("8. Save Data")
    print("9. Exit")
    print("10. Search topic ")

    choice = input("Enter choice: ")

    if choice == "1":

       id = int(input("Enter Student ID: "))
       name = input("Enter Student Name: ")
       email = input("Enter Email: ")
       grade = input("Enter Grade: ")

       student = Students(id, name, email, grade)
       students.append(student)
       print("Student Added Successfully")

    elif choice == "2" :
       id = int(input("Enter Trainer ID: "))
       name = input("Enter Trainer Name: ")
       email = input("Enter Email: ")  
       specialization = input("specialization : ")

       trainer = Trainers(id, name, email,specialization )
       trainers.append(trainer)
       print("Trainer Added Successfully")


    elif choice== "3":
       course_id = int(input("Enter your Course Id :"))
       course_name = input("Enter Your Course Name :")
       duration = input("Enter Your Course Duration :")
       trainer = trainers[0]

       course = Courses(course_id,course_name,duration,trainer)   
       courses.append(course) 
       print("Course Added Successfully") 


    elif choice == "4":

       student = students[0]
       course = courses[0]

       student.enroll_course(course)
       enrollment = Enrollment(student, course)
       enrollments.append(enrollment)
       print("Student Enrolled Successfully!")
          
    
    elif choice == "5":

       progress = int(input("Enter Progress: "))

       enrollment = enrollments[0]
       enrollment.updated_progress(progress)
       enrollment.diaplay_progress()


    elif choice == "6":

      if len(students) == 0:
         print("No Students Found")

      else:
         for student in students:
            student.display_details()   

    elif choice == "7" :
       for course in courses:
          course.display_course()

    elif choice == "8":

       if not students and not trainers and not courses and not enrollments:
           print("No data available to save.")

       else:

       
           with open("students.txt", "w") as file:

               for student in students:

                   file.write(
                       f"{student.id},"
                       f"{student.name},"
                       f"{student.email},"
                       f"{student.grade}\n"
                )

           with open("trainers.txt", "w") as file:

               for trainer in trainers:

                   file.write(
                       f"{trainer.id},"
                       f"{trainer.name},"
                       f"{trainer.email},"
                       f"{trainer.specialization}\n"
                )

     
           with open("courses.txt", "w") as file:

               for course in courses:

                   file.write(
                       f"{course.course_id},"
                       f"{course.course_name},"
                       f"{course.duration}\n"
                )

      
           with open("enrollments.txt", "w") as file:

               for enrollment in enrollments:

                   file.write(
                       f"{enrollment.student.id},"
                       f"{enrollment.course.course_id},"
                       f"{enrollment.progress_percentage}\n"
                )
            
        
    
    elif choice == "9":
       break


    elif choice == "10":
       search = input("Enter Topic: ").strip().lower()
       found = False
       for item in knowledge_list:
          if search.lower() in item.topic.lower():
             item.display_topicinfo() 
             found = True

       if not found:
          print("Topic not found")               

