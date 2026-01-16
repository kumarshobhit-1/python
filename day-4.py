#create a list of 5 no. print the first and last element and length from the list
numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Length of the list:", len(numbers))

#take a list of no. and find the sum and average using built in functions
num_list = [5, 15, 25, 35, 45]
total = sum(num_list)
average = total / len(num_list)
print("Sum:", total)
print("Average:", average)

#create a list of fruits. add a new fruit using append() and .insert() one at position 2 using .insert()
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
fruits.insert(2, 'grape')
print("Fruits list:", fruits)

#remove an element from the list using remove() and delete the last element using pop()
fruits.remove('banana')
fruits.pop()
print("Updated fruits list:", fruits)

#create a list with duplicate numbers. use count() to check how many times a number appears
dup_numbers = [1, 2, 3, 2, 4, 2, 5]
count_of_twos = dup_numbers.count(2)
print("Count of number 2:", count_of_twos)