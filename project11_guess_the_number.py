import random

def game(number,num):
    while num>0:
        guess = int(input("Make a guess : "))
        if guess == number:
            print("You got the number , You Won")
            return
        elif guess< number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else :
            print("Enter correct number between 1 to 100")
        num -= 1
        if num>0:
            print(f"You have {num} attempts remaining to guess the number.")
        else:
            print(f"Game Over! The correct answer was {number}.")

def playgame():
    print("Welcome to the game")
    number = random.randint(1,100)
    print("I am thinking of a number between 1 to 100.")
    
    while True:
        level = input("Choose a difficulty, Type 'easy' or ' hard' : ").lower()
        if level=="easy":
            num = 10
            break
        elif level == "hard":
            num = 5
            break
        else:
            print("Invalid difficulty. Please enter 'easy' or 'hard'.\n")            
    game(number,num)
playgame()

while input("do you want to play a game again ? type 'y' or 'n': ")== "y":
    print("\n" * 5)
    playgame()
