# ответить на вопрос - какую роль играет init() ?
# init() --> pentru caracterizarea unui obiect 
# почему метод init - принимает аргумент self и откуда он берется?
# din motivul că self primește esența caracteristicilor după care obiectul poate fi identificat după numiți parametri
class Product:
    def __init__(self, name, price, rating):
        self.name     = name
        self.price    = price
        self.rating   = rating

    def __str__(self):
        return f"-= PRODUCT({self.name} {self.price}$ {self.rating}) =-"

    def __gt__(self, b):
        if self.rating > b.rating:
            return Product

    def __lt__(self, b):
        if self.rating < b.rating:
            return Product

########################################
p1 = Product("Programming book", 100, 4.5)
p2 = Product("Hacking book", 150, 5.0)
print(p1)
print(p2)
if p1 > p2:
   print("First book is better")
elif p1 < p2:
   print("Second book is better")