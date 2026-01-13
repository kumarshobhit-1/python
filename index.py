# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello, {name}!")
# print(f"You are {age} years old.")

#1
num = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
sum = num + num2
difference = num - num2
product = num * num2
quotient = num / num2
print(sum)
print(difference)
print(product)
print(quotient)

#2
a=15
b=4
print(a // b)
print(a % b)
print(a ** b)


pen = 15
notebook = 40
cost = (3 * pen) + (2 * notebook)
print(cost)


num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
num4 = float(input("Enter number 4: "))
num5 = float(input("Enter number 5: "))
average = (num1 + num2 + num3 + num4 + num5) / 5
print(average)

n = int(input("Enter a number: "))
square = n ** 2
cube = n ** 3
sqareroot = n ** 0.5
print(square)
print(cube)
print(sqareroot)

travel = 120
time = 3
average_speed = travel / time
print(average_speed)

p = 5000
r = 5
t = 3
SI = (p * r * t) / 100
print(SI)

seconds = int(input("Enter total seconds: "))
minutes = seconds // 60
seconds = seconds % 60
print(minutes,"minutes  and ", seconds, "seconds")


task = float(input("Enter the total number of tasks: "))
task2 = float(input("Enter the number of number2 tasks: "))
result = task // task2
print(result)

z = int(input("Enter a number: "))
y = int(input("Enter another number: "))
if z%y == 0:
    print(z, "is multiple of", y)
else:
    print(z, "is not multiple of", y)