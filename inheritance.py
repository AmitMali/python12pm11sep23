class Person:
    # this is parent(super) class
    def __init__(self,name,email,contact):
        self.name=name
        self.email=email
        self.contact=contact
    def getInfo(self):
        print(f'''\nName : {self.name}\nEmail : {self.email}\nContact : {self.contact}''')

class Student(Person):
# this is child (derived) class inheritance parent class 'Person'
    def __init__(self,name,email,contact):
        super().__init__(name,email,contact)
    def setCourse(self,courseName,courseFees):
        self.courseName=courseName
        self.courseFees=courseFees

    def getInfo(self):
        super().getInfo()
        print(f'''Course : {self.courseName}\nFees : {self.courseFees}''')
class Trainer(Person):
# this is child (derived) class inheritance parent class 'Person'
    def __init__(self,name,email,contact):
        super().__init__(name,email,contact)
    def setCourses(self,course):
        self.course=course


    def getInfo(self):
        super().getInfo()
        print(f'''Courses : {self.course}''')

s=Student("Amit Mali","amit@gmail.com",9595949452)
s.setCourse("Python",5000)
s.getInfo()
t=Trainer("Arvind","arvind@gmail.com",94345834893)
t.setCourses(['Python','PHP','JavaScript','Full Stack'])
t.getInfo()