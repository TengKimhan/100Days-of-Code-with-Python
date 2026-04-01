# Coding exercise

# Exercise 1
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))
print(friends[random.randint(0, len(friends))])

# Exercise 2
random_heads_or_tails = random.randint(0, 1)
print(random_heads_or_tails)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
