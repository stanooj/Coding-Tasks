class A:
    def __init__(self):
        self.var = "A's variable"

class B(A):
    def __init__(self):
        super().__init__()
        self.var = "B's variable"

class C(B):
    def __init__(self):
        super().__init__()
        self.var = "C's variable"


if __name__ == "__main__":
    objA = A()
    objB = B()
    objC = C()

    print(objA.var)  
    print(objB.var)  
    print(objC.var)  
   
   
    ref = B()
    print(ref.var)  

    ref = C()
    print(ref.var)  
    