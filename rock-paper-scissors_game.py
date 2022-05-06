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

#Write your code below this line 👇


game_image = [rock, paper, scissors]

user_choice = int(input("What do you pick? 0 for rock, 1 for paper and 2 for scissors.\n "))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose! ")
else:   
    print(game_image[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_image[computer_choice])


    if user_choice == 0 and  computer_choice == 2:
            print("Rock smashes scissors! You win! ")
    elif computer_choice == 0 and user_choice == 2:
            print("Paper cover rock! You lose! ")
    elif computer_choice > user_choice:
            print("Scissors cut paper! You lose! ")

    elif user_choice > computer_choice:
            print("scissors cut the paper! You win! ")
    elif user_choice == computer_choice:
        print(f" You both selected the same {computer_choice}It's a tie! ")

            






