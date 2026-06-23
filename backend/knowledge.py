class Knowledge :
    def __init__(self,course,topic,information):
        self.course=course
        self.topic=topic
        self.information=information

    def display_topicinfo(self):
        print(f"""Course : {self.course}
Topic : {self.topic}
Information : {self.information}""")
        
        