# Scope and Global Scope

enemies = 1

def modify_enemies():
    global enemies 
    enemies += 1
    print("After modify: ", enemies)

modify_enemies()
print("Enemies outside the function: ", enemies)

# Constant
PI = 3.14