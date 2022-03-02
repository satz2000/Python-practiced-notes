"""
# What is Inheritance?
    Inheritance provides a reusability of a code, using the feature of existing class.

    subclass - subclass/ child class use all the feature from the parent class/super class
    Parent class - But it doesn't use the feature of subclass/child class

    Three types of Inheritance is there:
        * Single Inheritance
        * Multilevel Inheritance
        * Multiple Inheritance
"""

# Here we use static methods because we just print something, not any stuff

print("Single Inheritance:")
# Single Inheritance:

class A:                        # Class A is parent class/super class, that can't use feature of class B

    @staticmethod
    def feature_1():
        print("Feature 1")

    @staticmethod
    def feature_2():
        print("Feature 2")

class B(A):                     # Class B is subclass of A, that can use feature of Class A

    @staticmethod
    def feature_3():
        print("Feature 3")

    @staticmethod
    def feature_4():
        print("Feature 4")

# creating an object for the class B
obj = B()                       # B is subclass of A, so we just create an object only for class B

# Accessing all the features from the Class A by using Inheritance method
obj.feature_1()
obj.feature_4()


print("-----------------------------------------------")
print("Multilevel Inheritance:")
# Multilevel Inheritance:

class A:                        # A is parent class of B

    @staticmethod
    def feature_1():
        print("Feature 1")

class B(A):                     # B is subclass of A and Parent class of C

    @staticmethod
    def feature_2():
        print("Feature 2")

class C(B):                     # C is subclass of B, using all feature of B

    @staticmethod
    def feature_3():
        print("Feature 3")

# creating an object for the class C
obj = C()

# Accessing all the features from the parent class of A and B by using Inheritance method
obj.feature_1()
obj.feature_2()
obj.feature_3()


print("-----------------------------------------------")
print("Multilevel Inheritance:")
# Multiple Inheritance:

class A:                        # Here A is parent class of C

    @staticmethod
    def feature_1():
        print("Feature 1")

# here class B is not subclass of A
class B:                        # Here B is parent class of B

    @staticmethod
    def feature_2():
        print("Feature 2")

class C(A, B):                  # C is subclass of A and B / A and B are parent class of C

    @staticmethod
    def feature_3():
        print("Feature 3")

# creating an object for the class C
obj = C()

# Accessing the all feature from the class A and B by using Inheritance method
obj.feature_1()
obj.feature_2()
obj.feature_3()



"""
# Constructor in Inheritance:
    Constructor means special method called __init__ 
    MRO - method revolution order(if two super class has special method init then, it print left to right)
"""

print("----------------------------------------------------------")
print("\nConstructor in Inheritance:")
# creating a class
class A:                        # Class A is parent class/super class, that can't use feature of class B

    def __init__(self):
        print("Init of A")

    def feature_1(self):
        print("Feature 1")

    def feature_2(self):
        print("Feature 2")

class B(A):                     # Class B is subclass of A, that can use feature of Class A

    def __init__(self):
        super().__init__()      # super() methods used for printing the init function in super class
        print("Init of B")      # In class B already has init method also want init method of class A

    def feature_3(self):
        print("Feature 3")

    def feature_4(self):
        print("Feature 4")

# creating an object for the class B
obj = B()                       # B is subclass of A, so we just create an object only for class B

# Accessing all the features from the Class A by using Inheritance method
obj.feature_1()
obj.feature_4()
