'''
Classes are the blueprints for instantiating objects.

class is a keyword and hence needs to be in lower case
However, the name of the class needs to be in PascalCase

Every class needs to have a constructor method that is private.
This constructor method has a specific name: __init__()
The __init__() method will ALWAYS have self as the first  paramenter included.
The self parameter is by convention and it can be any name.
A class can have any number of attributes (properties).
The value for the properties are passed as parameter values when instantiating an object of that class.
Example:
'''


class Humans:
    def __init__(self, eyes=1, ears=None, mouth=1, nose=None, hands=None, legs=None, continent=None):
        self.eyes = eyes,
        self.ears = ears,
        self.mouth = mouth,
        self.nose = nose,
        self.hands = hands,
        self.legs = legs,
        self.continent = 'Africa'

    def __str__(self):
        return f"{self.eyes} {self.ears} {self.mouth} {self.continent}"

    # def display_humans_object(self):



# instantiating an object of the class Humans
my_human = Humans(2, 2, 2)
print(f'The data type of my_human.ears is: {type(my_human.ears)}')
print(my_human)
'''
In order to provide a string representation of an object of a class, we can define a specifi method:
__str__() and include the list of attributes that we want to concatenate as a string and return.
Example:
'''
#     def __str__(self):
#         return f"{self.eyes} {self.ears} {self.continent}"
#
# # instantiating an object of the class Humans
#     my_human = Humans(2, 2)
#     print(my_human)
