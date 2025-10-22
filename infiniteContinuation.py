print(f"Do you want to continue?")
userSelection = input("Enter y or n: ")
timesContinued = 0 #increments everytime user say yes -EP

#while loop to see if user wanted to continue an infinte loop -EP
while userSelection == "y":                         #basically if y than continue -Ep
    timesContinued += 1
    print(f"you said you wanted to continue")
    userSelection = input("Enter y or n: ")
    if (userSelection == "n"):                      #if not then end loop and print -EP
        break
print(f"you exited the matrix!")
print(f"time spent in the matrix {timesContinued}")

#originally testes two while loops this works -EP
#wanted to make it it into one which also works -EP
#while userSelection == "n": #or != "y"
   # break
#print(f"you exited the matrix!")
#print(f"time spent in the matrix {timesContinued}")
