import math

def cookoutHotDogsCalculator():
    hotDogPackage = 10
    bunsPackage = 8

    numberOfPeople = int(input("How many people are attending the cookout?\n""Enter the Amount: "))
    numberOfDogsPerPerson = int(input("How many hot dogs will each person be given?\n""Enter the Amount: "))
    
    sumOfHotDogs = numberOfDogsPerPerson * numberOfPeople
    minOfBunsPackage = math.ceil(sumOfHotDogs / bunsPackage)
    sumOfBuns = minOfBunsPackage * bunsPackage
    minOfDogsPackage = math.ceil(sumOfHotDogs / hotDogPackage)
    sumOfDogs = minOfDogsPackage * hotDogPackage
    
    leftoverDogs = sumOfDogs - sumOfHotDogs
    leftoverBuns = sumOfBuns - sumOfHotDogs
    
    print(f"The minimum number of packages of hot dogs required is: {minOfDogsPackage}")
    print(f"The minimum number of packages of hot dog buns required is: {minOfBunsPackage}")
    print(f"The number of hot dogs that will be left over is: {leftoverDogs}")
    print(f"The number of hot dog buns that will be left over is: {leftoverBuns}")
    
cookoutHotDogsCalculator()