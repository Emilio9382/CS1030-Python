import random
# 1. Generate two random single-digit integers (0–6)
number1 = random.randint(0, 6)
number2 = random.randint(0, 6)

print(f"Your first dice landed on {number1}")
print(f"Your second dice landed on {number2}")

#adds both numbers dice lands -EP
finaleScore = number1 + number2 

#orubts total score -EP
print(f"your finale score is {finaleScore}")

#this is just whatever total score you get it will print the following message -EP
if finaleScore < 3:
    print(f"You lose")
elif 3 < finaleScore < 8: 
    print(f"you landed on a shark! GAME OVER")
elif finaleScore == 9: 
    print(f"YOU are the chosen one! You wont a millino dolalrs!")
elif 9 < finaleScore < 12: 
        print(F"oh nooo! You have decapetated")
