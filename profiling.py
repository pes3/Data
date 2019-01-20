import cProfile # python profiling library

def doubled_numbers_1(size):
    #Provides lis of numbers from 0 to size, but doubled

    # create a list from [0,1,2,3]
    single_numbers = [i for i in range(0,size)]

    # create empty list
    lst = []

    # for [0,1,2....]
    for n in single_numbers:
        #add the number, but its doubled
        lst.append(n*2)

    return lst
    
def doubled_numbers_2(size):
        #Provides lis of numbers from 0 to size, but doubled
    return [i for i in range(0, size*2, 2)]



def doubled_numbers_3(size):
    #Gives you a list of numbers from 0 to size, but doubled

    #empty list
    lst = []

    for i in range(0, size):

        lst.append(i*2)
    return lst

def doubled_numbers_4(size):
    #Gives you a list of numbers from 0 to size, but doubled
    # good old list comprehension. this is also very fast
    return [i*2 for i in range(0, size)]

# sanity check to make sure our functions work
assert(doubled_numbers_1(3) == [0,2,4])
assert(doubled_numbers_2(3) == [0,2,4])
assert(doubled_numbers_3(3) == [0,2,4])
assert(doubled_numbers_4(3) == [0,2,4])
assert(doubled_numbers_2(3) == doubled_numbers_1(3))
# is the assert if true, everything works, otherwise it will stop

cProfile.run("doubled_numbers_1(1000000)")
cProfile.run("doubled_numbers_2(1000000)")
cProfile.run("doubled_numbers_3(1000000)")
cProfile.run("doubled_numbers_4(1000000)")
