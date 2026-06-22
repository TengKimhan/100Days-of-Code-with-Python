def greet():
    print("Hello, World!")
    print("Welcome to Day 8 of the coding challenge.")
    print("Let's have fun coding together!")
    
greet()

# Function with input parameters
def greet_with_name(name):
    print(f"Hello, {name}!")
    print("Welcome to Day 8 of the coding challenge.")
    print("Let's have fun coding together!")
    
greet_with_name("Alice")

# Function with multiple input parameters
def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"Welcome to {location} for Day 8 of the coding challenge.")
    print("Let's have fun coding together!")
    
# Positional arguments
greet_with("Bob", "New York")
# keyword arguments
geet_with(location="Los Angeles", name="Charlie")