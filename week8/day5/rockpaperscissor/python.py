import random



# Mini-Project: Rock, Paper, Scissors
# Introduction

# Rock-paper-scissors is an old game that can be played between two people. 
# You can read about it in English or French.

# We will create a game for the user to play Rock-paper-scissors against the computer. 
# The user will input his/her move (rock/paper/scissors), 
# and the computer will select either rock, paper, or scissors at random. 
# The computer will then compare the user’s move with the computer’s move, and determine the results of the game:

# The user won,
# The computer won (the user lost), or
# A draw (tie)
# We will print the outcome of each game: the user’s choice, the computer’s choice, and the result.

# The user will be able to play again and again. Once the user decides to exit the program, 
# we will print a summary of the outcomes of all the games: 
# how many times he won, lost, and drew with the computer.



playing = True

computer_choise = ""
user_choise = ""
wins = 0
draw = 0
lost = 0


while playing:
    menu_choise = input("Menu:\n (g) play a new game \n (x) show score and exit: \n")
    if menu_choise == "g":
        user_choise = input("select (r)ock  (p)aper or (s)iccors: ")
        print(f"the user choice {user_choise}")
        computer_choise = random.choice(["r", "p", "s"])
        print(f"computer choice {computer_choise}")
        if user_choise == computer_choise:
            print("it is a tie game")
            draw += 1
        elif user_choise == "p":
            if computer_choise == "s":
                print("computer won scissor cut paper")
                lost += 1
            elif computer_choise == "r":
                print("user won")
                wins += 1
        elif user_choise == "r":
            if computer_choise == "p":
                print("computer won paper defeat rock")
                lost += 1
            elif computer_choise == "s":
                print("user won")
                wins += 1
        elif user_choise == "s":
            if computer_choise == "r":
                print("computer won rock destroy scissors")
                lost += 1
            elif computer_choise == "p":
                print("user won")
                wins += 1
        else:
            print(f"{user_choise} is not a correct input")
    if menu_choise == "x":
        print(f" wons: {wins} matches \n tie: {draw} matches \n lost {lost} matches")
        playing = False



day = input("Thanks for playing")




