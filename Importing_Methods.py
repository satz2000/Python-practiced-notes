# Types of Importing Modules in Python

# 1. Import modules and calling with modules name:
import math
a = math.sqrt(25)
print(a)


# 2. Import modules with specific function u want:
from math import pow       # From this method no need call the module name in everytime
a = pow(4, 5)
print(a)


# 3. Importing every function in that modules:
import math as m           # Importing the math function as m for shortcut
a = m.pow(4, 5)
print(a)
