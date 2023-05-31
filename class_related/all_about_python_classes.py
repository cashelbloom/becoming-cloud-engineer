'''
Classes are the blueprints for instantiating objects.

class is a keyword and hence needs to be in lower case
However, the name of the class needs to be in PascalCase

Every class needs to have a constructor method that is private.
This constructor method has a specific name: __init__()
The __init__() method will ALWAYS have self as the first  paramenter included.
The name self for the first parameter is by convention and it can be any name.
You can even have different name for the first paramenter for different methods of a clas.
A class can have any number of attributes (properties).
The value for the properties are passed as parameter values when instantiating an object of that class.
However, if properties can also have default values  set in the constructor definition and you can specify
that a parameter can also have None as the default value.
If a parameter is included in the deinition of the __init__() method and it doesn't have a default value specified,
then a value has to be passed. Otherwise, the constructor will fail.
Example:
'''
class Humans:
    def __init__(self, my_custom_name, eyes, legs, hands, body):
        self.name = my_custom_name
        self.eyes = eyes
        self.legs = legs
        self.hands = hands
        self.body = body
        self.continent = 'Africa'

    def __str__(self):
        return f"Name: {str(self.name)} Eyes: {self.eyes} legs: {self.legs} hands: {self.hands} body: {self.body} continent: {self.continent}"
    def display(self):
        print(f"Name: {self.name} Eyes: {self.eyes} legs: {self.legs} hands: {self.hands} body: {self.body} Continent: {self.continent}")

my_human = Humans('Rama',"2", "2", "2", "1")
print(my_human)
my_human.display()


# class Humans:
#     # def __init__(self, eyes=1, ears=None, mouth=1, nose=None, hands=None, legs=None, continent=None, blood_color):
#     # def __init__(self, eyes="1", ears=None, mouth="1", nose=None, hands=None, legs=None, continent=None):
#     def __init__(self, eyes, ears, mouth, continent):
#         self.eyes = eyes,
#         self.ears = ears,
#         self.mouth = mouth,
#         self.continent = 'Africa'
#         # self.blood_color = blood_color
#
#     def __str__(self):
#         return f"Name: {self.eyes} Ears: {self.ears} Mouth: {self.mouth} Continent: {self.continent}"
#
#     # def display_humans_object(self):
#
#
#
# # instantiating an object of the class Humans
# my_human = Humans("2", "2", "2", "Asia")
# print(f'The data type of my_human.ears is: {type(my_human.ears)}')
# print(my_human)
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
