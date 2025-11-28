# display_numbers.py

# Print a single number
print("Single Number:")
print(10)
print("-" * 30)

# Print multiple numbers
print("Multiple Numbers:")
print(10, 20, 30, 40)
print("-" * 30)

# Print numbers using a loop
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)
print("-" * 30)

# Print numbers on the same line
print("Numbers on one line:")
for i in range(1, 11):
    print(i, end=" ")
print("\n" + "-" * 30)

# Print numbers stored in a list
numbers = [5, 15, 25, 35, 45]
print("Numbers from a list:")
for num in numbers:
    print(num)
print("-" * 30)

# Print even numbers
print("Even numbers between 1 and 20:")
for i in range(2, 21, 2):
    print(i)
print("-" * 30)

# Print odd numbers
print("Odd numbers between 1 and 20:")
for i in range(1, 21, 2):
    print(i)
print("-" * 30)
