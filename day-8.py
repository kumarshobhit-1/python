#File Handling & Error Handling
#open students.txt and read the contents

with open("C:\\Users\\Hp\\OneDrive\\Desktop\\students.txt", 'r') as file:
        contents = file.read()
        print(contents)


with open("C:\\Users\\Hp\\OneDrive\\Desktop\\students.txt", 'r') as file:
        contents1 = file.readline()
        print(contents1)


with open("C:\\Users\\Hp\\OneDrive\\Desktop\\students.txt", 'r') as file:
    lines = file.readlines()
    print(lines)


with open("C:\\Users\\Hp\\OneDrive\\Desktop\\students.txt", 'r') as file:
    for line in file:
        print(line.strip())


with open("C:\\Users\\Hp\\OneDrive\\Desktop\\students.txt", 'r') as file:
    lines = file.readlines()
    number_of_students = len(lines)
    print(f"Number of students: {number_of_students}")

with open("C:\\Users\\Hp\\OneDrive\\Desktop\\students.txt", 'w') as file:
    file.write("sita, 20, Abc\n")
    file.write("rita, 22, Bcd\n")
    file.write("gita, 19, Abc+\n")

with open("C:\\Users\\Hp\\OneDrive\\Desktop\\students.txt", 'r') as file:
    contents = file.read()
    print(contents)

with open("C:\\Users\\Hp\\OneDrive\\Desktop\\students.txt", 'a') as file:
    file.write("karan, 23, Pune\n")

with open("C:\\Users\\Hp\\OneDrive\\Desktop\\students.txt", 'r') as file:
    contents = file.read()
    print(contents)

with open("C:\\Users\\Hp\\OneDrive\\Desktop\\students.txt", 'r+') as file:
    contents = file.readlines()
    contents[0] = "sita kumari, 20, Abc\n"
    file.seek(0)
    file.writelines(contents)

with open("C:\\Users\\Hp\\OneDrive\\Desktop\\students.txt", 'r+') as file:
    contents = file.read()
    print(contents)
    file.write("shneha, 20, xyz\n")
    file.seek(0)
    contents = file.read()
    print(contents)