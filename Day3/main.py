# # Day3
# # Conditional Statements, Logical Operators, Code Blocks and Scope
#
# # 1. Control Flow with if / else and Conditional Operators
# # 1.1. if/else
# print("Welcome to the rollercoaster")
# height = int(input("What s your height in cm? "))
#
# if height > 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry you have to grow taller before you can ride.")
#
# # 1.2. Comparison: > < >= <= != ==
# if height == 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry you have to grow taller before you can ride.")
#
# # 2. Modulo %
# print(10 % 3) # Result remainder: 1
# print(10 % 2) # Result remainder: 0
#
# number_to_check = int(input("What is the number you want to check?"))
#
# if number_to_check % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# 3. Nested if statement and elif statement
# print("Welcome to rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# 4. Multiple If Statement in Succession
# print("Welcome to rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         bill = 5
#         print("Please pay $5.")
#     elif age <= 18:
#         bill = 7
#         print("Please pay $7.")
#     else:
#         bill = 12
#         print("Please pay $12")
#
#     wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
#     if wants_photo == "y":
#         # Add $3 to their bill
#         bill += 3
#
#     print(f"Your final bill is ${bill}")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# 5. Logical Operators
# A and B
# A or B
# not A
print("Welcome to rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45 <= age <= 55: # age >= 45 and age <= 55
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Please pay $12")

    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == "y":
        # Add $3 to their bill
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
