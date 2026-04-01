# Coding exercise

# Exercise 1
student_scores = [150, 142, 185, 120, 172, 184, 149, 24, 59, 68, 199, 78, 65, 89]
max_score = student_scores[0]

for score in student_scores:
    if max_score <= score:
        max_score = score
print(f"Maximum score: {max_score}")


# Exercise 2
for num in range(1, 101):
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)