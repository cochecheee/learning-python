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

import random as r
your_turn = int(input("What's do you choose? Type 0 for Rock, Type 1 for Paper, Type 2 for scissors\n"))
bot_turn = r.randint(0,2)

list_type = list([rock, paper, scissors])
print(list_type[your_turn])
print("Bot's turn ")
print(list_type[bot_turn])

if your_turn == bot_turn:
    print("Equal result!!")
elif your_turn-1 == bot_turn:
    print("You win!!!")
elif your_turn+1 == bot_turn:
    print("You lose!!!")
elif your_turn-1==-1 and bot_turn==2:
    print("You win!!!")
else:
    print("You lose!!!")