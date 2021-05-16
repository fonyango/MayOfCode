
# --- DAY FIFTEEEN ---

''' 
Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number
of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.
'''

class Flower():

    def __init__(self, name, petals, price):
        self.name = name
        self.petals = petals
        self.price = price

    def get_name(self):
        print("The name of the flower is ",self.name)

    def get_petals(self):
        print("The flower has {} petals".format(self.petals))

    def get_price(self):
        print("The flower costs {} US dollars".format(self.price))


f1 = Flower("Rose flower", 9, "USD 500")

print(f1.get_name())
print(f1.get_petals())
print(f1.get_price())