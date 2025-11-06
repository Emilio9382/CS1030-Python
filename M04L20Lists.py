#declares list -EP
scores = [37,73,91]
#prints the score in the 2nd spot of the list -EP
print(scores[2])
#displays all varaibles in list -EP
for scores in scores:
    print(scores)

#list of food (in string) =EP
foods = ["pizza","burgers","hot dogs"]
#prints list =EP
print(foods)
#prints the 2nd spot in the list =EP
print(foods[2])
#prints the number of things in the list -EP
print(len(foods))
#prints i like ___ for everything in the list =EP
for food in foods: 
    print("i like", food)

#declares list of favo hobbies -EP
Hobbies = ["motorcycle", "car", "video games"]
#print hobbie 0 -EP
print(Hobbies[0])
#prints hobbie 1 -EP
print(Hobbies[2])
#print(HObbies[3]) gets in error =EP
#reaplaces hobbie 0 with new one =EP
Hobbies[0] = "reading"
print(Hobbies)
#reaplaces 2nd hobbie with 2 more -EP
Hobbies[1:2] = ["building pcs", "editing"]
print(Hobbies)
#replaces hobbie hobbie 2 and 3 with one hobbie -EP
Hobbies[1:3] = ["watching YT"]
print(Hobbies)
#add new hobbie at the end of list -EP
Hobbies.append("buidling pcs")
print(Hobbies)
#add new hobbie to the beggining of list (0)-EP
Hobbies.insert(0,"editing")
print(Hobbies)
#removes a specific hobbie -EP
Hobbies.remove("editing")
print(Hobbies)
#removes one hobbie from a ceratin point on the list -EP
Hobbies.pop(2)
print(Hobbies)
#deletes the list entirely -EP
Hobbies = ["motorcycle", "car", "video games"]
del Hobbies
#deletes contents of list but not the list itself -EP
Hobbies = ["motorcycle", "car", "video games"]
Hobbies.clear()
print(Hobbies)
