# Here we saw about the inner class in oops.


# creating a class using keyword called class
class Students:

    # creating a special method using __init__ keyword:
    def __init__(self, name, roll_no, age):             # passing arguments
        self.name = name                                # Instance variable
        self.roll_no = roll_no                          # Instance variable
        self.age = age                                  # Instance variable
        self.lap = self.Laptop()                        # Instance variable

    # creating Instance method (Accessor method)
    def show(self):
        print(self.name, self.roll_no, self.age)
        self.Laptop().show()                            # prints value of inner class by call in main class

    # creating class inside a class (# inner class)
    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i7"
            self.ram = 16

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Students("sathish", 29, 21)
s2 = Students("siva", 31, 20)

s1.show()
s2.show()
