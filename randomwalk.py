#imagine you have a field mowed like a graph, and someone walking randomly from origin

#let's first look at location, it will be immutable
#this class is just made to be inhereted ie a 'Base Class', not realy useful on itself
class Location(object):
    def __init__(self, x, y):
        #x and y are floats
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX,
                        self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distFrom(self, other):
        xDist = self.x - other.getX()
        yDist = self.y - other.getY()
        return (xDist**2 + yDist**2)**.05
    def __str__(self):
        return '<' + str(self.x) + ', '\
               + str(self.y) + '>'
class pedestrian(object):
    def __init__(self, name = None): ## why do we have name = None here??
            #assume name is a str
        self.name = name
    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'
import random
#pedestrian wanders random
class typicalpedestrian(pedestrian):
    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1,0), (-1,0)]
        return random.choice(stepChoices)
### pedestrian wanders north 
class lesstypicalpedestrian(pedestrian):
    def takeStep(self):
        stepChoices = [(0.0,1.1), (0.0, -0.9), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

#pedestrian and locatoins are immutable, we want them to be hashable/use as a key in a dictionary
    

class Field(object):
    def __init__(self):
        self.pedestrians = {}
    def addpedestrian(self, pedestrian, loc):
        if pedestrian in self.pedestrians:
            raise ValueError ('Duplicate pedestrian')
        else:
            self.pedestrians[pedestrian] = loc
    def getLoc(self, pedestrian):
        if pedestrian not in self.pedestrian:
            raise ValueError('Pedestrian not in Field')
        return self.pestrians[pedestrian] # what exactly is this doing

def movePedestrian(self, pedestrian):
    if pedestrian not in self.pedestrians:
        raise ValueError('Pedestrian not in Field')
    xDist, yDist = pedestrian.takeStep()
    #use move method of Location to  get new location
    self.pedestrians[pedestrian] =\
        self.pedestrians[pedestrian].move(xDist, yDist)
# Fields are mutable, see we can change the value of the dictionary

# now to simulate single walk
def walk(f, d, numSteps):
    # assumes: f a Field, D a Pedestrian, and NumStps an int >=0.
    #Moves d numSteps times; returns the distance between the final location and origin
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

#simulating multiples Walks

def simWalks(numSteps, numTrials, dClass):
    #Assumes numSteps an int >= 0, numtrails an in >0, dclass a subclass of Pedestrian,
    #returns list of final distances for each trial
    Joe = dClass()
    origin = Location(0,0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addpedestrian(Joe, origin)
        distances.append(round(walk(f, Joe, numTrials), 1))
    return distances


def pedestrianTest(walkLengths, numTrials, dClass): # how come we later pass in 4 args
# assumes walkLengths a sequence of ints >= 0,. numTrails an int > 0, dClass a subclass of Drunk
#for each number of steps in walkLengths, runs simWalks with numTrials walks and prints reults
 
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials,
                             dClass)
        print(dClass.__name__, 'random walk of',
            numSteps, 'steps')
        print(' Mean =',
            round(sum(distances)/len(distances), 4))
        print(' Max =', max(distances),'Min =', min(distances)) 

    
    
