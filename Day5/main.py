# Day5: Loops

# 1. For Loops
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit + " pie")

for i in range(0, len(fruits)):
    print(fruits[i])

# 2. Sum, max method
student_scores = [150, 142, 185, 120, 172, 184, 149, 24, 59, 68, 199, 78, 65, 89]
print(f"Total scores: {sum(student_scores)}")
print(f"Max score: {max(student_scores)}")


