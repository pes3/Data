def myfunc(*args, **kwargs):
  print("*args: ")
  print(args)
  
  print("**kwargs: ")
  print(kwargs)
  
myfunc(1, 2, "abc") # "*args: (1, 2, "abc")

myfunc(1, 2, key="abc") # "*args: (1, 2), **kwargs = {"key": "abc"}

