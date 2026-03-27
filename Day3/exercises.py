# Coding exercise 1

# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)
#
# # 🚨 Do not modify the values above
# # Write your code below 👇
# if bmi < 18.5:
#     print("underweight")
# else:
#     if bmi < 25:
#         print("normal weight")
#     else:
#         print("overweight")


# Coding Exercise 2
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
final_bill = 0

if size == "S":
    final_bill += 15
elif size == "M":
    final_bill += 20
elif size == "L":
    final_bill += 25
else:
    print("Please input correct size")

if pepperoni == "Y":
    if size == "S":
        final_bill += 2
    else:
        final_bill +=3

if extra_cheese == "Y":
    final_bill += 1

print(f"Your final bill is: ${final_bill}")
