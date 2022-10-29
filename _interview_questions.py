# 1. Reverse a list
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

# 2. Find all occurrences of a substring in a given string by ignoring the case
str1 = "Welcome to India. India is awesome, isn't it?"
sub_string = "India"

temp_str = str1.lower()

count = temp_str.count(sub_string.lower())
print("The India count is:", count)

# 3. Check if all items in the tuple are the same
def check(t):
    return all(i == t[0] for i in t)

tuple1 = (45, 45, 45, 45)
print(check(tuple1))

# 4. Remove items from set1 that are not common to both set1 and set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)

# 5. Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary'] = 8500
print(sample_dict)

# 6. Calculate the cube of all numbers from 1 to a given number
input_number = 6
for i in range(1, input_number + 1):
    print("Current Number is :", i, " and the cube is", (i * i * i))

# 7. Write a program to print the following start pattern using the for loop
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

# 7. Assign a different name to function and call it through the new name

def display_student(name, age):
    print(name, age)

display_student("Emma", 26)
showStudent = display_student
showStudent("Emma", 26)

# 8. Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]
print(max(x))

# 9. Use a loop to display elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[1::2]:
    print(i, end=" ")

# 10. Find the sum of the series upto n terms
n = 5
start = 2
sum_seq = 0

for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)

# 11. Count the total number of digits in a number
num = 75869
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print("Total digits are:", count)

#12. Return multiple values from a function
def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction
res = calculation(40, 10)
print(res)

# 13. Write a function named "evens" which returns True if a number is even and otherwise returns False.
def evens(i):
    if i % 2 == 0:
        return True
    else:
        return False

# 14. Write an if statement that asks for the user's name via input() function. If the name is "Bond" make it print "Welcome on board 007." Otherwise make it print "Good morning NAME".

name = input("Please enter your name.")
if name == "Bond":
    print("Welcome on board 007.")
else:
    print("Good morning " + name)

# 15. Write a program to print multiplication table of a given number
n = 2

for i in range(1, 11, 1):
    product = n * i
    print(product)

# 16. Display Fibonacci series up to 10 terms
num1, num2 = 0, 1

print("Fibonacci sequence:")
for i in range(10):
    print(num1, end="  ")
    res = num1 + num2
    num1 = num2
    num2 = res

# 17. Find the factorial of a given number
num = 5
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)

# 18. Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)
print(res["Kelly"])

# 19. Create a dictionary by extracting the keys from a given dictionary
sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ["name", "salary"]

newDict = {k: sampleDict[k] for k in keys}
print(newDict)

# 20. Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]

sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
print(sample_dict)















