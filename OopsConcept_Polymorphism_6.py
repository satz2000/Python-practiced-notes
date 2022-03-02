"""
# What is Polymorphism?
    Methods are present in different class are in same name (or)
    Different class have a different methods but name of the methods is same.

    Types of Polymorphism:
        * Operator Overloading
            Using the existing operator/predefined methods with our own modification in the method for the use
        * Method Overloading
            Creating a function with many arguments by passing default value is None,This methods is called method overloading
"""

# Polymorphism:
print("Polymorphism:")

# creating a different class
class Pycharm:

    # But creating a methods in same name
    @staticmethod
    def execute():                  # creating staticmethod for printing some words not any coding
        print("Hai G")
        print("Welcome all")

# creating another class with different name
class Mycharm:

    # name of the method is same compared to methods in previous class
    @staticmethod
    def execute():
        print("Hai G")
        print("Welcome all")
        print("How are you G ?")


# creating class for using the methods in previous function
class Python:

    # creating a function to run the execute methods
    def editor(self, ide):          # passing the arguments as object created for the class
        ide.execute()               # calling the execute methods with an object which are passing

# for passing the argument of the object in the methods, we created
ide = Mycharm()

# creating an object for the class Python
py = Python()

# call the methods in Class Python and passing the arguments as Class name already we created
py.editor(ide)





# Operator Overloading
print("---------------------------------------")
print("Operator Overloading:")

class OverLoading:

    # create a special method/constructor for passing the value
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # use the pre-defined methods and make changes in your way
    def __add__(self, other):
        s1 = self.num1 + self.num2
        s2 = other.num1 + other.num2
        s3 = s1 + s2
        return s3

    # Again using the predefined methods name and make changes in it
    def __gt__(self, other):
        s1 = self.num1 + self.num2
        s2 = other.num1 + other.num2
        if s1 > s2:
            return 0
        elif s1 == s2:
            return 1
        elif s1 < s2:
            return 2
        else:
            pass


student_1 = OverLoading(67, 89)
student_2 = OverLoading(71, 85)

# creating new variable to store value of the sum of the student 1 and student 2
student_3 = student_1 + student_2
print(student_3)                    # print the value

# checking whether student 1 get higher marks then student or student 2 gets higher
if student_1.__gt__(student_2) == 0:
    print("Student 1 gets higher mark than Student 2")

elif student_1.__gt__(student_2) == 1:
    print("Both of them has same mark")

elif student_1.__gt__(student_2) == 2:
    print("Student 2 gets higher mark than Student 1")



# Method Overloading
print("---------------------------------------")
print("Method Overloading:")

class Method_Overloading:

    # pass the special function, In future we may use these methods and write some stuff inside
    def __init__(self):
        pass

    # creating staticmethod for the general purpose,Not for comparing two objects
    @staticmethod
    # creating a method using method overloading by passing arguments value
    def sum(a=None, b=None, c=None):                # passing 3 arguments but the value assigned is None

        # if passing three values
        if a!=None and b!=None and c!=None:
            s = a + b + c

        # if passing two values only
        elif a!=None and b!=None:
            s = a + b

        # otherwise, print the single value that are entered
        else:
            s = a
        print(s)

# creating an object for the class
obj = Method_Overloading()

# call the methods inside the class by using object.methods
obj.sum(5, 7)                                       # method required 3 arguments but passing 2 only. because, there is default value is None





# Method Overriding
print("---------------------------------------")
print("Method Overriding:")

"""
# What is Method Overriding?
    creating a two different class with parent and child class but the child class has not methods just pass the class 
"""

class A:                        # parent/super class doesn't use the methods in child class

    @staticmethod
    def show():
        print("In Class A")

class B(A):                     # creating child class with pass function and use the methods of parent class
    pass                        # passing the function and using another class methods in it, called method overriding

# creating an object for child class
obj = B()

# calling the methods of class A in class B by using Inheritance methods
obj.show()
