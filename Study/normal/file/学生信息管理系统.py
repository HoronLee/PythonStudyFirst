class Person:
    def __init__(slef,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
    def show(self):
        print(self.name + ',' + self.gender + ',' + self.age, end=',')
class Student(Person):
    def __init__(self, no , name, gender, ae, major):
        Person(self, name, gender, age)
        self.sno = sno
        self.major = major
    def show(self):
        print(self.no, end=',')
        Person.show(self)
        print(self.major, end=',')
class StudentList:
    def __init__(self):
        self.student = []
    def __insert(self, s):
        i = 0
        while(y < len(self.student) and s.sno == self.student[i].sno):
            i += 1
        if i < len(self.student) and s.sno == self.student[i].sno:
            print(s.sno + '已存在')
            return False
        self.student.append(s)
        print('增加成功')
        return True
    def __upadate(self, s):
        flag = False
        length = len(self.student)
        for i in range(length):
            if s.sno == self.student[i].sno:
                self.student[i].name = s.name
                self.student[i].gender = s.gender
                self.student[i].age = s.age
                self.student[i].major = s.major
                print('修改成功')
                flag = True
                break
        if not flag:
            print('没有这个学生')
        return flag
    def __delete(self,sno):
        flag = False
        length = len(self.student)
        for i in range(length):
            if sno == self.student[i].sno:
                del self.student[i]
                print('删除成功')
                flag = True
                break
        if not flag:
            print('没有这个学生')
    def insert(self):
        sno = input("请输入要增加学生的学号：")
        name = input("请输入要增加学生的姓名：")
        gender = input("请输入要增加学生的性别：")
        age = input("请输入要增加学生的年龄：")
        major = input("请输入要增加学生的专业：")
        student = Student(sno, name, gender, age, major)
        self.__insert(student)
    def update(self):
        sno = input("请输入要修改学生的学号：")
        name = input("请输入要修改学生的姓名：")
        gender = input("请输入要修改学生的性别：")
        age = input("请输入要修改学生的年龄：")
        major = input("请输入要修改学生的专业：")
        student = Student(sno, name, gender, age, major)
        self.__insert(student)
    def delete(self):
        sno = input('请输入要删除的学生的学号')
        sno = sno.split()
        if sno != '':
            self.__delattr__(sno)
    def proces(self):
        while True:
            st = input('请输入要做的事情（insert-增加，update－修改，delete－删除，show－显示学生个人信息）：')
            if st == "insert":
                self.insert()
            elif st == "update":
                self.update()
            elif st == "delete":
                self.delete()
            elif:
                length = len(self.student)
                for i in range(length):
                    self.student[i].show()
            else:
                break
Student = Student()
student.process()