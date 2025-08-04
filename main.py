# rock paper scissors game 
import random
'''
rock is 0
scissor is -1
paper is 1
'''

def logic():
    while True:
        choice = [0, 1, -1]
        computer_choice = random.choice(choice)
        youDict = {"paper": 1, "scissor": -1, "rock": 0}
        reverseDict = {1: "paper", -1: "scissor", 0: "rock"}
        # taking user input 
        user = input("Enter your choice (rock, paper, scissor): ").lower()
        # check if user input is right or not 
        if user not in youDict:
            print("You entered something wrong. Please try again.\n")
            return

        # main logic of game

        user_choice = youDict[user]
        print(f"you choosed  {reverseDict[user_choice]} and computer choosed {reverseDict[computer_choice]} ")
        if user_choice == computer_choice:
            print("this game has been drawn")
        elif user_choice == 1 and computer_choice == 0:
            print("you  won")
        elif user_choice == 1 and computer_choice == -1:
            print("you  lost")
        elif user_choice == 0 and computer_choice == 1:
            print("you  lost")
        elif user_choice == 0 and computer_choice == -1:
            print("you  won")
        elif user_choice == -1 and computer_choice == 0:
            print("you  lost")
        elif user_choice == -1 and computer_choice == 1:
            print("you  won")
        # for looping the game
        inp = input("do you want to play it again if yes say y: ").lower()
        if inp != "y":
            print("thanks for playing game now you have quited the game")
            break
    


logic()

