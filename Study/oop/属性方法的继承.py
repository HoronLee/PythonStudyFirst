class Person:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
    
    def show(self,end='\n'):
        print(self.name,self.gender,self.age,end=end)

    def display(self,end='\n'):
        print(self.name,self.gender,self.age,end=end)

class Student(Person):
    def __init__(self,name,gender,age,major,dept):
        Person.__init__(self,name,gender,age)
        self.major = major
        self.dept = dept
        
    def show(self):
        Person.show(self,'')
        print(self.major,self.dept)

    def setName(self,name):
        self.name =name

s = Student("james","male","20","software","computer")
s.show()
s.display()
s.setName("robert")
s.show()
s.display