import random
    # random generator
tieGame = 0 
wonGame = 0
lostGame = 0

print(f"Welcome to rock paper scissor")
def start_game():  #function to start the game -EP
    global tieGame, wonGame, lostGame #prevents them from reseting upon a new game -EP
    #userINput -EP
    print(f"type r for rock, type p for paper, or type s for scissors")
    playerChoice = input("Your choice is: ")

    # displays user input -EP
    if (playerChoice == "r"):
        print(f"you chose rock")
    elif (playerChoice == "p"):
        print(f"you chose paper")
    elif (playerChoice == "s"):
        print(f"you chose scissors")

    
    
    botChoice = random.randint(1, 3)
    #displays bot choices -EP
    print(f"Bot chose: {botChoice}")
    if (botChoice == 1):
        print(f"bot chose rock")
    elif (botChoice == 2):
        print(f"bot chose paper")
    elif (botChoice == 3):
        print(f"bot chose scissors")

    #possibilties -EP
    if (playerChoice == "r" and botChoice == 1): 
        print(f"tie game")
        timeGame += 1 #increments if it was a tie -EP
    elif (playerChoice == "p" and botChoice == 2):
        print(f"tie game")
        timeGame += 1 #increments if it was a tie -EP
    elif(playerChoice == "s" and botChoice == 3):
        print(f"tie game")
        tieGame += 1 #increments if it was a tie -EP
    elif(playerChoice == "r" and botChoice == 2):
        print(f"you lost to a bot!")
        lostGame += 1 #increments if it was a lost -EP
    elif(playerChoice == "r" and botChoice == 3):
        print(f"dont get to excited. YOu only won because it's an AI")
        wonGame += 1 #increments if it was a won -EP
    elif(playerChoice == "p" and botChoice == 1):
        print(f"look at that AI is not so smart after all")
        wonGame += 1 #increments if it was a won -EP
    elif(playerChoice == "p" and botChoice == 3):
        print(f"what-a-loser")
        lostGame += 1 #increments if it was a lost -EP
    elif(playerChoice == "s" and botChoice == 1):
        print(f"CONGRATUALTIONS! YOU LOSE!")
        lostGame += 1 #increments if it was a lost -EP
    elif(playerChoice == "s" and botChoice == 2):
        print(f"YOU WON!!!")
        wonGame += 1 #increments if it was a won -EP

    #restart -EP
    print(f"do you want to continue playing: ")
    continueGame = input("Enter y or n: ")

    if(continueGame == "y"):
        start_game() #restart option after first match -EP
    if(continueGame == "n"):
        print(f"Game Over")
        print(f"game stats")
        print(f"you tied {tieGame}")
        print(f"you won {wonGame}")
        print(f"you lost {lostGame}")

#starts the first game than will go back to the restart line up -EP
start_game()