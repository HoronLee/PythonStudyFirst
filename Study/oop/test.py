class A:
    def __init__(self):
        print('c')
    def test1(self,env1,env2):
        return env1,env2

    def test2(self,t1,t2):
        print(self.test1(t1,t2))


A = A()
A.test2(3,4)