with open("my_file.txt",mode= "r") as fe:
    content = fe.read()
    print(content)

with open("/Users/Dolphin/Desktop/new_file.txt", mode= "w") as fe:
    fe.write("hello world")