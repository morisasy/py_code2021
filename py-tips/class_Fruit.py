# class fruit

class Fruit:
    def __init__(self, name, color, expire_date):
        self.name = name
        self.color = color
        self.expire_date = expire_date

    def details(self):
        print(f"my {self.name} is {self.color} and expire date on {self.expire_date}")


apple= Fruit("Apple", "Red", "04.07.2022")
apple.details()

print(apple.color)
print(apple.name)
print(apple.expire_date)
