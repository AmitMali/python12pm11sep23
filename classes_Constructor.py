class Person:
    def __init__(self,name):
        self.name=name
    def getInfo(self):
        print(self.name)

a=Person("amit mali")
b=Person("Rahul")
a.getInfo()
b.getInfo()

