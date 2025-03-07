class A:
    def __init__(self):
        self.__private_var = "Private Variable"

    def __private_method(self):
        print("This is a private method")

    def access_private(self):
        print(self.__private_var)
        self.__private_method()

class B(A):
    def try_access_private(self):
        # print(self.__private_var)  
        # self.__private_method()   
        print("Cannot access private members from subclass")

if __name__ == "__main__":
    objA = A()
    objA.access_private()  

    objB = B()
    objB.try_access_private()  