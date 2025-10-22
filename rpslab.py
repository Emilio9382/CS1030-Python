

print(f"Welcome to rock paper scissor")
def start_game(): 
    print(f"type r for rock, type p for paper, or type s for scissors")
    playerChoice = input("Your choice is: ")

    if (playerChoice == "r"):
        print(f"you chose rock")
    elif (playerChoice == "p"):
        print(f"you chose paper")
    elif (playerChoice == "s"):
        print(f"you chose scissors")

    import random
    # random generator
    botChoice = random.randint(1, 3)
    print(f"Bot chose: {botChoice}")
    if (botChoice == 1):
        print(f"bot chose rock")
    elif (botChoice == 2):
        print(f"bot chose paper")
    elif (botChoice == 3):
        print(f"bot chose scissors")

    if (playerChoice == "r" and botChoice == 1): 
        print(f"tie game")
    elif (playerChoice == "p" and botChoice == 2):
        print(f"tie game")
    elif(playerChoice == "s" and botChoice == 3):
        print(f"tie game")
    elif(playerChoice == "r" and botChoice == 2):
        print(f"you lost to a bot!")
    elif(playerChoice == "r" and botChoice == 3):
        print(f"dont get to excited. YOu only won because it's an AI")
    elif(playerChoice == "p" and botChoice == 1):
        print(f"look at that AI is not so smart after all")
    elif(playerChoice == "p" and botChoice == 3):
        print(f"what-a-loser")
    elif(playerChoice == "s" and botChoice == 1):
        print(f"CONGRATUALTIONS! YOU LOSE!")
    elif(playerChoice == "s" and botChoice == 2):
        print(f"YOU WON!!!")

    print(f"do you want to continue playing: ")
    continueGame = input("Enter y or n: ")

    if(continueGame == "y"):
        start_game()
    if(continueGame == "n"):
        print(f"Game OVer")

start_game()