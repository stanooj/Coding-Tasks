class A:
    def override_method(self):
        print("Overridden method in Class A")

class B(A):
    def override_method(self):
        print("Overridden method in Class B")

class C(B):
    def override_method(self):
        print("Overridden method in Class C")


if __name__ == "__main__":
    refB = A()
    refB.override_method()  
    refB = B()
    refB.override_method() 
    refC = A()
    refC.override_method()  
    refC = C()
    refC.override_method()  