rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

computer = random.randint(0, 2)

computer_list = ["a", "b", "c"]
computer_list[0] = rock
computer_list[1] = paper
computer_list[2] = scissors

new = computer_list[computer]

answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
if answer == "0":
    print(rock)
    print("The computer chose:")
    print(new)
    if computer == 0:
        print("It's a draw")
    elif computer == 1:
        print("Computer wins:(")
    elif computer == 2:
        print("You win!")
elif answer == "1":
    print(paper)
    print("The computer chose:")
    print(new)
    if computer == 0:
        print("You win!")
    elif computer == 1:
        print("It's a draw")
    elif computer == 2:
        print("Computer wins:(")
else:
    print(scissors)
    print("The computer chose:")
    print(new)
    if computer == 0:
        print("Computer wins:(")
    elif computer == 1:
        print("You win!")
    elif computer == 2:
        print("It's a draw")