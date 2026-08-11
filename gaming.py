import random

while True:
    rat = ["rock", "paper", "siser"]
    ran = random.choice(rat)

    choose = input("Enter a choes: ")
    print(f"you choes {choose}. and the computer choos {ran}")

    if choose == "siser" and ran == "rock":
        print("ooooooooooo siser cut`s paper you loos")
    elif choose == "rock" and ran == "paper":
        print("oooooooo paper cover the rock and rock is defeting the leef it is a draw")
    elif choose == "paper" and ran == "siser":
        print("oooooooooo siser cut the paper you loos")
    elif choose == "siser" and ran == "paper":
        print("congragulations siser cut`s paper you won")
    elif choose == "paper" and ran == "rock":
        print("oooooooo paper cover the rock and rock is defeting the leef it is a draw")
    elif choose == ran:
        print("it is a draw")
    elif choose == "rock" and ran == "siser":
        print("yessssssssssss you won")
    else:
        print("Pleas try again!")
        continue

    hax = input("do you want to play agein [y/n]?")
    if hax == "y" or hax == "Y":
        continue
    else:
        print("thank you for playing with us")
        exit()