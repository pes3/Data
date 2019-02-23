# seeing if two people share the same birthday in different size groups
import random, math
def sameDate(numPeople, numSame): 
    possibleDates = range(366)
    birthdays = [0]*366
    for p in range(numPeople):
        birthDate = random.choice(possibleDates)
        birthdays[birthDate] += 1
    return max(birthdays) >= numSame

def birthdayProb(numPeople, numSame, numTrials):
    numHits = 0
    for t in range (numTrials):
        if sameDate(numPeople, numSame):
            numHits += 1
    return numHits/numTrials

for numPeople in [10, 20, 40, 100]:
    print('For', numPeople,
          'est. prob. of a shared birthday is',
          birthdayProb(numPeople, 2, 10000))
    numerator = math.factorial(366)
    denom = (366**numPeople)*math.factorial(366-numPeople)
    print('Actual prob. for N = 100 = ',
          1 - numerator/denom)

#displays estimated probability again 
#100 person group, 99% chance 2 people have the same bday. Wow suprising stat to me!

# note looking if 3 share the same bday is much more complex

# you could adjust simulation model to calculate 3 easier than analytic model

#This model below is a change in simulation, NOT MATHEMATICAL CHANGE , as it is simpler
#this model accounts for the fact some birthdas are more common(distributed, ie recognize birthdays are not uniformally dist) than others, so you would swap this function in for the one above

def sameDatev2(numPeople, numSame):
    possibleDates = 4*list(range(0, 57)) + [58]\
                    + 4*list(range(59, 366))\
                    + 4*list(range(180,270))
    birthdays = [0]*366
    for p in range(numPeople):
        birthDate = random.choice(possibleDates)
        birthdays[birthDate] += 1
    return max(birthdays) >= numSame

## these have been examples that are descriptive  not prescriptive , simulation model is 'if I do this something happens' which is why simulation models are different than optimization model
