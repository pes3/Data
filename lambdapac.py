mylist = [1,4,6,2,3,1,7,5,-20,-5,-1,-3,-4,-5]
sorted(mylist, key=lambda x: x)
sorted(mylist, key=lambda x: -x)
sorted(mylist, key=lambda x: x, reverse=True)
sorted(mylist, key=lambda x: x**2)
## note the logic above is to determine whatto sort to what order, not changing any values in my list
#key is a keyword argument
def howBigIsThisCowTuple(cow_tuple):
    """Example: howBigIsThisCowTuple(("andy", 4)) -> 4"""
    return cow_tuple[1]

mylist = [2,3,4,5,6,7]
mynewlist = [x**2 for x in mylist]


def print_thing(thing_1, thing_2):
  print(thing_1)
  print(thing_2)
  
print_thing(1,2)
print_thing(thing_1=2, thing_2=1)
