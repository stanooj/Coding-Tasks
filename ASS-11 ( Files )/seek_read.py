with open("sample.txt", "r") as file:
    file.seek(15)  
    print(file.read(10))  