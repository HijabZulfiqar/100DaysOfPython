print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure")
side = input("you're at a cross road.Where do you want to go ? Type 'Left' or 'Right'. ")
if side == "Right":
    print("Game Over")
else:
    option = input("you are at a left side do you want to 'Swim' or 'Wait'")
    if option == "Swim":
        print("Game Over")
    elif option == "Wait":
        door = input("which door you want to go? 'Blue', 'Red','Yellow'")
        if door == "Blue":
            print("Game Over!")
        elif door == "Red":
            print("Game Over!")
        else:
            print("You win!")
