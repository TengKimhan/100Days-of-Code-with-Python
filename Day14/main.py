from art import logo, vs
from game_data import data
from random import randint
from os import system

score = 0
lose = False

def clear_screen():
    system("clear")
    print(logo)
    
def compare_follower(a, b, check):
    global score
    global lose
    if (check == 'A' and a["follower_count"] >= b["follower_count"]) or (check == 'B' and b["follower_count"] >= a["follower_count"]):
        score+=1
    else:
        lose = True
    result = {
        "score": score,
        "lose": lose
    }
    return result

print(logo)
while(True):
    a = data[randint(0, len(data)-1)]
    b = data[randint(0, len(data)-1)]
    
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")
    check = input("Who has more followers? Type 'A' or 'B': ")
    clear_screen()
    result = compare_follower(a, b, check)
    if (result["lose"]):
        print(f"You are wrong your score is {result['score']}")
        break
    print(f"You are correct your score is {result['score']}")
