class Student:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
    def show(self):
        print(self.name,self.gender,self.age)
student = []
try:
    f = open('./Study/normal/file/file01.txt',mode='rt')
    while True:
        name = f.readline().strip("\n")
        if name == "":
            break
        gender = f.readline().strip("\n")
        age = float(f.readline().strip("\n"))
        student.append(Student(name,gender,age))
    f.close()
    for s in student:
        s.show()
except Exception as err:
    print(err)