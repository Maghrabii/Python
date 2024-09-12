
import random

choices = ["Rock", "Paper", "Scissors"]
print("Welcome to the Rock, Paper, Scissors game:")
rules = input("please Enter to continue or type (Help) for the rules help\n")

if rules.lower() == "help":
     print('''
            ***********The Basic Rules of RPS***********

            Despite its underlying complexity, the game’s rules are straightforward. Players deliver hand signals representing rock, paper, or scissors, with the outcome determined by these three rules:

            1-Rock wins against scissors.
            2-Scissors win against paper.
            3-Paper wins against rock.
           
           
           ''') 



ran = random.choice(choices)
User_input = input("Enter your choice(Rock, Paper, Scissors): ").capitalize()
     
if User_input in choices:
            print(f"you choice {User_input}")
            print(f"PC choice {ran}")
            if User_input == "Rock" and ran == "Scissors":
                    print("you win")

            elif User_input == "Rock" and ran == "Paper":
                    print("PC win")
            elif User_input == "Paper" and ran == "Scissors":
                    print("PC win")
            elif User_input == "Paper" and ran == "Rock":
                    print("you win")        
            elif User_input == "Scissors" and ran == "Rock":
                    print("PC win")     
            elif User_input == "Scissors" and ran == "Paper":
                    print("You win")             
            else:
                    print("try agine")
else:
         print("invalid choice. please rerun the prgram agin and follow the rule in your choice")
