age = 36
txt = f"My name is John, I am {age}"
print(txt)

# sting defintions -EP
name_of_dog = "rose"
name = "Emilio" 
favHob = "Gaming"


# integer definitions -EP
number_of_dog = "8"
age = 21
numberOne = 10
numberTwo = 5

#usage of cocancnation -EP
print ("I have " + number_of_dog + " dogs !")

#f sting usage -EP
print(f"my dogs name is {name_of_dog}")

#f string with integers -EP
print(f"I have {number_of_dog} dogs!")

#itterations -EP
print(f"I have {age + 70}!")

#subtracting -EP
print(f"subtracting 10-5 = {numberOne - numberTwo}") 

#sentence with declared variables -EP
print(f"My name is {name} and my favorite hobby is {favHob}!")  

#Lab2 
#instructions 
# - declare variables name, hobby, year of birth and the current year for usesr input -EP
# - print user name and hobby -EP
# - calculate age with current year and year of birth -EP
# - print name and age -EP
#Declerations -EP
userName = input("What is your name? ")                #Declares that userName = userinput -EP
userHobby = input("What's your favorite hobby? ")      #Declares that userHobby = user fav hobby -EP
currentYear = int(input("wWhat year is it? "))         #declares that currentYear = user input on currentYear -EP
birthYear = int(input("What is the year you were born? "))  #declares that birthYEar = year that user was born -EP
userAge = currentYear - birthYear                           #calculates userAge by subtrating birthYear from currentYear -EP

#Displays user name and users fav hobby -EP
print(f"My name is {userName}. My Favorite hobby is {userHobby}." ) 

#displays users age by subtracting birthYear from currentYEar -EP
print(f"You are {currentYear - birthYear} years old!")

#displays users name and age -EP
print(f"My name is {userName} and I am {userAge}")