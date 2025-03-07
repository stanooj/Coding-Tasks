from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def __init__(self):
        print("Abstract class constructor")

    @abstractmethod
    def abstract_method(self):
        pass  

    def non_abstract_method(self):
        print("This is a non-abstract method in AbstractClass")