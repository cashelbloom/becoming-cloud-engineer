class Humans:
    def __init__(self, my_custom_name, eyes, legs, hands, body):
        self.name = my_custom_name
        self.eyes = eyes
        self.legs = legs
        self.hands = hands
        self.body = body
        self.continent = 'Africa'

    # def __str__(self):
    #     return f"Name: {str(self.name)} Eyes: {self.eyes} legs: {self.legs} hands: {self.hands} body: {self.body} continent: {self.continent}"
    #   return f"Name: {str(self.name)} Eyes: {self.eyes} legs: {self.legs}"
    def display(self):
        print(f"Name: {self.name} Eyes: {self.eyes} legs: {self.legs} hands: {self.hands} body: {self.body} Continent: {self.continent}")


my_human = Humans('Rama',"2", "2", "2", "1")
print(my_human.display())
#
# my_human_with_continent = Humans('Rama',"2", "2", "2", "1")
# print(f'trying to create an object by giving an argument meant for continent: {my_human_with_continent}')
# my_human.display()
# #
# print(dir(my_human))