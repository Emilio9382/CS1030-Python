#Looks like this bit of code will loop itself a total of 5 times -EP
#it will start from 0 to 4 making it a total of 5 iteration 0,1,2,3,4 -EP
#and also prints that iteration -EP
#if changed from 5 to 10 it will iteration 10 times starting from 0 ending at 9 - EP
#it loops it self until it hits the number we want it to hit -EP
#if its -5 we run into an error -EP
#count would loop itself until we hit the range -EP
for count in range(-5):
        print(count)

#this follows the example from above but instead it starts at 2 instead of 0 -EP
#this will keep going for 4 iterations since it hops 4 times from 2 to 8 -EP
#in this case 2 would start and then it would go 3,4,5 makign it 4 iterations =EP
#if it was -2 it would be the same process but starts and -2 instead of 2 =EP
#good names would be start to penultimate (2nd last) -EP
for count in range(-2,6):
        print(count)

#for this one the range would be 0 to 10 -EP
#starts at 0 and ends not at 10 be the penultimate of 10 -EP
#but with a twist this one instead of increments by 1 it increments by 2 each time =EP
for count in range(0,10,2):
        print(count)