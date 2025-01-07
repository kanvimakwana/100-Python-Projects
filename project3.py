print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************''')

print("Welcome to the Treasure Island \nYour mission is to find the Treasure\n")
print("Make the right choices and the Treasure will be yours\n\n")
input('Press "Enter" to START the adventure')  

choice1 = input('\n\nYou are at a crossroad,\nWhere do you want to go?\nType "right" or "left":\n\n').lower()
if choice1 == "left":
    choice2 = input('\n\nYou\'ve come to a lake.\nThere is an island in the middle of the lake.\nType "wait" to wait for a boat or type "swim" to swim through:\n\n').lower()
    if choice2 == "wait":
        while True:  
            choice3 = input("\n\nYou arrive at the island unharmed.\nThere is a house with 3 doors.\nOne RED\nOne BLUE\nOne YELLOW\nWhich color do you choose?\n\n").lower()
            if choice3 == "red":
                print("\n\nGame Over, the room is full of fire!")
                break
            elif choice3 == "yellow":
                print("\n\nYou WON, the room is full of TREASURE!")
                break
            elif choice3 == "blue":
                print("\n\nGame Over, the room is full of poison!")
                break
            else:
                print("Invalid choice! Please choose a correct color (red, blue, or yellow).")
    else:
        print("\n\nGame Over, you were attacked by pirates!")
else:
    print("\n\nGame Over, you fell into a hole!")


