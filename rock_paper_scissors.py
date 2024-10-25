import random
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
game_choices = [rock, paper, scissors]

user_choice = int(input("Welcome to the last game of your life Type 0 for rock, 1 for paper, or 2 for scissors\n"))
print(game_choices[user_choice])

comp_choice = random.randint(0, 2)
print("The Computer chose:")
print(game_choices[comp_choice])

if user_choice >= 3 or user_choice <0:
    print("Your entry is invalid, Enjoy my forever Dungeon!")
elif user_choice == 0 and comp_choice == 2:
    print("You WIN, throw the rock at their head >:) ")
elif user_choice > comp_choice:
    print("You Win! Use your weapon and take their head off!")
elif comp_choice > user_choice:
    print("You Lose, You'll be executed with the weapon you lost to.")
elif comp_choice == 0 and user_choice == 2:
    print("You Lose! Your skull will be crushed while you beg!")
elif comp_choice == user_choice:
    print("Its a Draw, run it again to determine your fate!")




