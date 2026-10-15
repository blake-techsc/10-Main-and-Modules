"""
Modules are an extremely useful tool for organizing and reusing code.
Simply, a module is a python file that has code, variables, functions, classes that you can have in another program.
Like functions, modules help code be:
-reusable
-organized
-easier to maintain

DRY Principle - Don't repeat yourself

Examples of built in modules:
time, random, os, math......

eg.
import math # including the module
print(math.pi) # using code from the imported module
"""
# import math
# lets see the built in modules:
# help("modules")
# help(math)

# import a module with an alias
import math as m
print(m.pi)

# we could also import specific functions from a module
from random import randint
print(randint(1,10))