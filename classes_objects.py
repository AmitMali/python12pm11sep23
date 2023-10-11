# Classes are blueprints
class Person:
    # name="amit mali"
    def setInfo(self,name):
        self.name=name
    def getInfo(self):
        print(self.name)


a=Person()
b=Person()
# print(a.name)
# print(b.name)
a.setInfo("amit")
b.setInfo("sushil")
a.getInfo()
b.getInfo()
