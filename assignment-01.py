# # Q.1 => write a program to print numbers from 1 to 10 using a for loop
# for i in range(1, 11):
#     print(i)


# # Q.2 => Find the sum of first 10 natural numbers using a while loop
# sum_natural = 0
# i = 1
# while i <= 10:
#     sum_natural += i
#     i += 1
# print("Sum of first 10 natural numbers is:", sum_natural)


# # Q.3 => Take a number as input and print its multiplication table up to 10
# num = int(input("Enter a number to print its multiplication table: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")


# # Q.4 => find the factorial of a number usign a while loop.
# number = int(input("Enter a number to find its factorial: "))
# factorial = 1
# i = 1
# while i <= number:
#     factorial *= i
#     i += 1
# print(f"Factorial of {number} is: {factorial}")


# # Q.5 => Take a integer as input and reverse its digits
# number = int(input("Enter an integer to reverse its digits: "))
# reversed_number = 0
# while number > 0:
#     digit = number % 10
#     reversed_number = reversed_number * 10 + digit
#     number //= 10
# print("Reversed number is:", reversed_number)


# # Q.6 => Print all even numbers between 1 and 50
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)


# # Q.7 => Take a number as input and find the sum of its digits
# number = int(input("Enter a number to find the sum of its digits: "))
# sum_of_digits = 0
# while number > 0:
#     digit = number % 10
#     sum_of_digits += digit
#     number //= 10
# print("Sum of the digits is:", sum_of_digits)


# Q.8 => Print the first 10 terms of the Fibonacci series
a, b = 0, 1
print("Fibonacci series up to 10 terms:")
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
print()
