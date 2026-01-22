# Basic Try-Except
# 1. Write a program to divide two numbers. Handle the case when the denominator is 0.
try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# 2. Take user input for age. If the input is not an integer, handle the error.
try:
    age = int(input("Enter your age: "))
    print(f"Your age is: {age}")
except ValueError:
    print("Error: Please enter a valid integer for age.")

# 3. Open a file data.txt in read mode. Handle the error if the file does not exist.
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file data.txt does not exist.")


# 4. Access the 5th element of a list. Handle the error if the list has fewer than 5 elements.
my_list = [1, 2, 3]
try:
    print(my_list[4])
except IndexError:
    print("Error: The list has fewer than 5 elements.")

# 5. Convert a string "abc" to an integer. Handle the error.
try:
    num = int("abc")
    print(num)
except ValueError:
    print("Error: Cannot convert 'abc' to an integer.")

# Using else

# 6. Write a program that asks for two numbers and divides them. Use else to print "Division successful" only if no error occurs.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"Division successful. The result is: {result}")

# 7. Ask the user for a filename. If the file exists, print its contents; else, handle the error. Use else to say "File read successfully".
filename = input("Enter the filename: ")
try:
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    print(f"Error: The file {filename} does not exist.")
else:
    print("File read successfully.")
    print(content)

# Using finally
# 8. Write a program to open a file and read data. Ensure the file is always closed using finally.
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file data.txt does not exist.")
finally:
    try:
        file.close()
    except NameError:
        pass

# 9. Divide two numbers, handle ZeroDivisionError, and in finally, print "Program finished".
try:
    a = float(input("Enter the numerator: "))
    b = float(input("Enter the denominator: "))
    result = a / b
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
finally:
    print("Program finished.")

# 10. Use try-except-finally to handle invalid list index access and always print "Execution complete" in finally.
my_list = [10, 20, 30]
try:
    index = int(input("Enter an index to access: "))
    print(my_list[index])
except IndexError:
    print("Error: Invalid list index.")
finally:
    print("Execution complete.")

# Mixed Cases
# 11. Write a program to input two numbers, divide them, handle ValueError and ZeroDivisionError separately, and print "Done" in finally.
try:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    result = x / y
    print(f"The result is: {result}")
except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
finally:
    print("Done.")

# 12. Write a program where you try to open a file, if not found then create it, else print "File already exists", and finally close it.
try:
    file = open("newfile.txt", "r")
except FileNotFoundError:
    print("File not found. Creating newfile.txt.")
    file = open("newfile.txt", "w")
else:
    print("File already exists.")
finally:
    file.close()

# 13. Write a program that handles multiple exceptions: divide by zero, wrong type conversion, and invalid list index.
my_list = [1, 2, 3]
try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    result = a / b
    print(f"Division result: {result}")
    
    index = int(input("Enter an index to access from the list: "))
    print(f"List element: {my_list[index]}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input type.")
except IndexError:
    print("Error: Invalid list index.")
