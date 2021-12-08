class itemRAT:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount #amount of food in pounds
        self.price = 0 #price of food in $
        self.total = 0 #total price

    def __pricelistRAT(self): #setting price for food
        if self.name.lower() == "dry cured iberian ham":
            self.price = 177.8
        elif self.name.lower() == "wagyu steaks":
            self.price = 450
        elif self.name.lower() == "matsutake mushrooms":
            self.price = 272
        elif self.name.lower() == "kopi luwak coffee":
            self.price = 306.5
        elif self.name.lower() == "moose cheese":
            self.price = 487.2
        elif self.name.lower() == "white truffles":
            self.price = 3600
        elif self.name.lower() == "blue fin tuna":
            self.price = 3603
        elif self.name.lower() == "le bonnotte potatoes":
            self.price = 270.81
        else:
            self.price = 0

    def totalpriceRAT(self): #calculates total cost
        self.__pricelistRAT()
        self.total = self.price * self.amount
        return self.total

    def __str__(self):
        self.totalpriceRAT()
        return f"Name: {self.name}\n Amount(pounds): {self.amount}\n Price: {self.price}\n Total: {self.total}"

    def getpriceRAT(self):
        self.__pricelistRAT()
        return self.price
