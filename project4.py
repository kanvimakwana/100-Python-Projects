import random
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

user=int(input('What do you choose? Type 0 for rock , 1 for paper and 2 for scissors\n'))
if user==0:
    print(rock)
elif user==1:
    print(paper)
else:
    print(scissors)
    
print("computer chose:")
    
computer = random.randint(0,2)
if computer==0:
    print(rock)
elif computer==1:
    print(paper)
else:
    print(scissors)

if user >=3 or user<0:
    print("You typed an invalid number!")
elif user==0 and computer == 2:
    print("you win!")
elif user==2 and computer==0:
    print("You lose!")   
elif user == computer:
    print("Its a Draw") 
elif computer>user:
    print("You lose!")
elif computer<user:
    print("You Win!")
elif computer==0 and user==2:
    print("you Lose!")

    
