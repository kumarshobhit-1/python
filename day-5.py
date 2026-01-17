# #create a set of 5 colors
# color={"red", "green", "blue", "yellow", "orange"}
# print(color)

# #ceate a set of numbers with duplicate and check how python handles duplicates
# numbers={1,2,3,4,5,3,2,1}
# print(numbers)

# #write a pogram to loop through a set and print each element
# for col in color:
#     print(col)


# #create a set and use .add to insert a new element
# fruits={"apple", "banana", "cherry"}
# fruits.add("orange")
# print(fruits)


# #remove and element from a set using .remove and observe what happens if the element is not present
# fruits.remove("banana")
# print(fruits)
# fruits.remove("grape")
# print(fruits)

# #remove an element using .discard and compare its behavior with .remove
# fruits.discard("cherry")
# print(fruits)
# fruits.discard("kiwi")
# print(fruits)


# #use .pop to remove a random element from a set
# removed_fruit=fruits.pop()
# print("Removed fruit:",removed_fruit)
# print("Fruits after pop:",fruits)


#create to sets and find their union, intersection, and difference
setA={1,2,3,4,5}
setB={4,5,6,7,8}
union=setA.union(setB)
intersection=setA.intersection(setB)
difference=setA.difference(setB)
print("Union:",union)
print("Intersection:",intersection)
print("Difference:",difference)


#use .copy to create a copy of a set and modify the copy
setC=setA.copy()
setC.add(10)
print("Original setA:",setA)
print("Modified copy setC:",setC)


#use .clear to empty a set
setC.clear()
print("Cleared setC:",setC)

#convert a list with duplicate elements into a set to remove duplicates
my_list=[1,2,2,3,4,4,5]
my_set=set(my_list)
print("List:",my_list)
print("Set without duplicates:",my_set)

#write a program to find all unique characters in a string using a set
my_string="hello world"
unique_chars=set(my_string)
print("Unique characters in the string:",unique_chars)

#given two list of students (cricket and football), find students who play both sports (intersection).
cricket_players=["Alice","Bob","Charlie","David"]
football_players=["Charlie","David","Eve","Frank"]
cricket_set=set(cricket_players)
football_set=set(football_players)
both_sports=cricket_set.intersection(football_set)
print("Students who play both sports:",both_sports)


#take a sentence as input and print all unique words using a set
sentence="this is a test this is only a test"
words=sentence.split()
unique_words=set(words)
print("Unique words in the sentence:",unique_words)

#write a program to check if two sets are equal (ignoring order)
set1={1,2,3,4,5}
set2={5,4,3,2,1}
are_equal=set1==set2
print("Are the two sets equal?",are_equal)

#create a two sets and check if they have at least one element in common(hint: usi intersection)
setX={"apple","banana","cherry"}
setY={"cherry","date","fig"}
have_common=setX.intersection(setY)
print("Do setX and setY have at least one element in common?",bool(have_common))

