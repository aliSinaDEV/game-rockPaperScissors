import random

print('''
                         /$$ /$$                                             /$$
                        | $$| $$                                            | $$
 /$$  /$$  /$$  /$$$$$$ | $$| $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ | $$
| $$ | $$ | $$ /$$__  $$| $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$| $$
| $$ | $$ | $$| $$$$$$$$| $$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$|__/
| $$ | $$ | $$| $$_____/| $$| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/    
|  $$$$$/$$$$/|  $$$$$$$| $$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$ /$$
 \_____/\___/  \_______/|__/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/|__/
                                                                                
                                                                                
                                                                                
''')

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
game_images = [rock, paper, scissors]

while True:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))
    print("You Chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer Chose:")
    print(game_images[computer_choice])

    if user_choice == 0:
        if computer_choice == 0:
            print("Tie")
        elif computer_choice == 1:
            print("You Lose!")
        else:
            print("You Win")
    elif user_choice == 1:
        if computer_choice == 0:
            print("You Win!")
        elif computer_choice == 1:
            print("Tie")
        else:
            print("You Lose!")
    elif user_choice == 2:
        if computer_choice == 0:
            print("YOu Lose!")
        elif computer_choice == 1:
            print("You Win!")
        else:
            print("Tie")
