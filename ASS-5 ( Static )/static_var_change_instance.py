class Example:
    static_var = 10  

obj1 = Example()
obj1.static_var = 20 
print(Example.static_var)  
print(obj1.static_var)     