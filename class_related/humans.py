class Humans:
    def __init__(self, my_custom_name, eyes, legs, hands, body):
        self.name = my_custom_name
        self.eyes = eyes
        self.legs = legs
        self.hands = hands
        self.body = body

    def __str__(self):
        return f"Name: {str(self.name)} Eyes: {self.eyes} legs: {self.legs} hands: {self.hands} body: {self.body}"
    # def display(self):
    #     print(f"Name: {self.name} Eyes: {self.eyes} legs: {self.legs} hands: {self.hands} body: {self.body}")

my_human = Humans('Rama',"2", "2", "2", "1")
print(my_human)
# my_human.display()