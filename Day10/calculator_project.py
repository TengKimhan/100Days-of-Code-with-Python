from art import logo
from os import system

def calculate(first_numb, next_numb, operation):
    if operation == "+":
        return first_numb + next_numb
    elif operation == "-":
        return first_numb - next_numb
    elif operation == "*":
        return first_numb * next_numb
    elif operation == "/":
        return first_numb / next_numb
  
def main():  
    print(logo)
    first_number = float(input("What's the first number?: "))
    while(True):
        operation = input("+\n-\n*\n/\nPick an operation: ")
        next_number = float(input("What's the next number?: "))
        result = calculate(first_number, next_number, operation)
        
        print(f"{first_number} {operation} {next_number} = {result}")
        
        check = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        
        if check == "y":
            first_number = result
            continue
        elif check == "n":
            system("clear")
            main()

main()