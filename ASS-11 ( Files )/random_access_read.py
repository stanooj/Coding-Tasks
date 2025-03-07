with open("sample.txt", "r") as file:
    file.seek(5)  
    content = file.read(10)  
    print(content)