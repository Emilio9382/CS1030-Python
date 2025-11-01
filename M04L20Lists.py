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

Hobbies = ["motorcycle", "car", "video games"]
print(Hobbies[0])
print(Hobbies[2])
#print(HObbies[3]) gets in error
Hobbies[0] = "reading"
print(Hobbies)
Hobbies[1:2] = ["building pcs", "editing"]
print(Hobbies)
Hobbies[1:3] = ["watching YT"]
print(Hobbies)
Hobbies.append("buidling pcs")
print(Hobbies)
Hobbies.insert(0,"editing")
print(Hobbies)
Hobbies.remove("editing")
print(Hobbies)
