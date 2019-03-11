class Person():
    name = "noname"
    age = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def announce(self):
        print("I am {}, {} years old".format(self.name, self.age))


guy = Person("dude", 20)

        
# This is demonstrating the ability to inspect a class' methods while the program is running.
print(Person.__name__) # Here we get the name of the class, which is 'Person'.
print(Person.__dict__['announce']) # Here we inspect the 'announce' method.

# These two lines of code accomplish the same thing.
Person.__dict__['announce'](guy) # We are using the 'announce' method, passing 'guy' as the first argument to the 'announce' function that 'Person' owns.
guy.announce()
##relction not used often
