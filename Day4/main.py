# Day4: Randomisation and Python Lists

# 1. Module
import module_test
print(module_test.my_favourite_number)

# 2. Random Module
import random

# 2.1. Random integer
random_integer = random.randint(1, 10)
print(random_integer)

# 2.2. Random Floating Point (Real-valued distributions)
# random float from 0.0, 1.0
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

# random fload form a, b
random_float = random.uniform(10, 100)
print(random_float)

# 4. Lists - Data Structure
states_of_america = ["Delaware", "Pennsylvania"]
print(states_of_america)
print(states_of_america[0])
print(states_of_america[-1])

# 4.1. Update list
states_of_america[1] = "Pencilvania"
print(states_of_america)

# 4.2. Add list
states_of_america.append("Angelaland")
print(states_of_america)

# 4.3. Extend list
states_of_america.extend(["Kimhanland", "newland"])
print(states_of_america)

# 4.4. Index Error and Working with Nested Lists
# IndexError: list index out of range
# print(states_of_america[50])

# 4.5. Nested List
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
