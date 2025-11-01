#user give a number and it will give the times table up to 10 -EP
finalTotal = 0
userChoise = int(input("what number do you want a times table for? "))
for multi in range (1,11):
    finalTotal = userChoise * multi 
    print(f"{userChoise} * {multi} = {finalTotal}")