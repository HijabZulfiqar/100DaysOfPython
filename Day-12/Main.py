################### Scope ####################

# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# local Scope

def decrease_enemies():
    enemies_demo = 1
    print(f"{enemies_demo} enemies")
decrease_enemies()
# print(f"enemies outside function:{enemies_demo}") #error local scope

# Global Scope
enemies_demo_l=1
def increase_enemies_demo():
    enemies_demo_l =50
    print(f"{enemies_demo_l} enemies")
#     There is no Block Scope In Python
game_level=1
# enemies=["Zombie","Skeleton"]
# if game_level<5:
#     new_enemies=enemies[0]
# print(new_enemies)
def checkO():
    enemies = ["Zombie", "Skeleton"]
    if game_level < 5:
        new_enemies = enemies[0]

        print(new_enemies)


# changing global variables
enemies = 1


def increase_enemies():
    global enemies
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

PI=2.11
def check():
    PI=3
    print(f"value of PI is {PI}")
check()