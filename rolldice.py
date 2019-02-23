import random

def rolldice(): # uniform dist
    return random.choice([1,2,3,4,5,6])


def testroll(n = 10): # creates a string of what we got
    result = ''
    for i in range(n):
        result = result + str(rolldice())
        print(result)
    
    
## what is the probability we roll the dice 5 times and get 1 each time
random.seed(0) # note how computers generate random numbers, set seed for easier testing
def sameroll(rolls):
    return 1/(6**rolls)
# the number of possible events, the numbers of events that have the propert of interest (this case all 1's) and then simple division

#Probability (p) always range from 0[impossible]-1[guaranteed]
#probability of not occuring is equal to 1-p
#When the events are independent of each other, the probability of all of the events occuring is equal to
##..(cont. line above) a product of the proababilites of each of the events occuring
###...(cont) - so if prob a = .4 and prob b is .5 then prob a & b is a* b = .2 if indepent ( if the outcome of one has no influence on outcome of other like a die roll)

def runSim(goal, numTrials, txt):
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rolldice())
        if result == goal:
            total += 1
    print('Actual probability of' , txt, '=',
          round(1/(6**len(goal)), 8))
    estProbability = round(total/numTrials, 8)
    print('Estimated Probability of', txt, '=', round(estProbability, 8))


#mind sample estimate, simulation must be larger considering low probability

