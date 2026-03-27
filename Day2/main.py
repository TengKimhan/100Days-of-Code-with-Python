# Day2
# 1. Primitive Data Types
# 1.1. String
print("Hello")
print("Hello"[0])

# 1.2. Integer
print(123 + 123)
print(123_456_789)

# 1.3. Float
print(3.14159)

# 1.4. Boolean
print(True)
print(False)

# 2. Type Error, Type Checking and Type Conversion
# 2.1. len(123)
# TypeError: object of type 'int' has no len(), it is expected a string

# 2.2. Type Checking
print(type(123))
print(type("Hello world"))
print(type(True))
print(type(3.14))

# 2.3. Type Conversion
print(float("3.14"))
print(int("123"))
print(bool("True"))
print(type(str(123)))

# 3. Mathematical Operation in Python

# 3.1. Subtraction
print(7 - 3)

# 3.2. Addition
print(123 + 456)

# 3.3. Multiplication
print(3 * 2)

# 3.4. Division
# Implicit type casting to float
print(6 / 3)

# 3.5. Floor Division
print(6 // 3)

# 3.6. Exponent
print(2**2)

# Rule order of priority: PEMDAS (Parenthesis, Exponent, Multiplication/Division, Addition/Subtraction)

# 4. Number Manipulation and F Strings in Python
# 4.1. Flooring a Number
int(3.738) # become 3

# 4.2. Rounding a Number
bmi = 84 / 1.65 ** 2
print(round(bmi, 2))

# 4.3. Assignment Operator
# +=, -+, *=, /=
score = 0
score += 1
print(score)

# 4.4. f-string
height = 1.0
is_winning = True
print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")
