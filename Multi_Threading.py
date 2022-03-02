# Multi-Threading

# Simultaneously runs the different class or run the code
# For multithreading, we want to use the threading packages

# importing all function from the threading packages
from threading import *

# importing time packages for the changing the execution times
from time import sleep

# creating a class in the name of Hai, Hai is subclass/child class of Thread
class Hai(Thread):

    # creating methods that are present in threading packages in same name
    def run(self):

        # using the for loop to print "Hai" 5 times
        for i in range(5):
            print("Hai")
            sleep(1)                    # sleeping time is 1 seconds for each execution of "Hai"

# creating another class for printing the output in simultaneously
class Hello(Thread):                    # Hello class is subclass of Thread for the purpose of Multi-threading

    # creating methods that are present in threading packages in same name
    def run(self):
        # using for loop to print "Hello" 5 times
        for i in range(5):
            print("Hello")
            sleep(1)                    # sleeping time is 1 seconds for each execution of "Hello"


# crating an object of H1 and H2 for the classes
H1 = Hai()
H2 = Hello()

# Instated of call the methods name with an object,
# here we call the object with start method is build methods of threading
H1.start()
# for each execution we need some time cap for printing it one by one properly
sleep(0.5)
H2.start()

# Join method is used for printing the all statements then only it prints the final statement that are in outside class
# Waiting until the H1 and H2 are printed the output then print this one by using join function in Threading library
H1.join()
H2.join()
print("Bye Sir!")
