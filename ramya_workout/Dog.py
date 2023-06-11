class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in reponse to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

"""Instantiate a class"""

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)
print("My dog's name is " + your_dog.name + ".")
print("My dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()


