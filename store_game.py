from Items import Item
from Shopper import Shopper
from Store import Store
import random


# Item file (self, name, price, type, sale=False, sale_amount=0)


strawberry = Item('Strawberry', 3, 'Fruit')
pear = Item('Pear', 2, 'Fruit')
apple = Item('Apple', 1, 'Fruit')
banana = Item('Banana', 2, 'Fruit')

bread = Item('Bread', 1, 'Bakery')
roll = Item('Roll', 0.5, 'Bakery')
rye_bread = Item('Rye Bread', 1.5, 'Bakery')
baguette = Item('Baguette', 1, 'Bakery')
cake = Item('Chocolate Cake', 3, 'Bakery')
cookies = Item('Tea cookies', 2, 'Bakery')

candy = Item('Fruit Candies', 2, 'Sweets')
choc_candy = Item('Chocolate Candies', 2, 'Sweets')
nougat = Item('Pistacho Nougat', 4, 'Sweets')


apple.do_sale(20)
nougat.do_sale(30)
pear.do_sale(10)


fruits_candy = Store('Fruits&Candy', 10000)
print(fruits_candy)


# loop for random

all_items = [strawberry, pear, apple, banana, bread, roll, rye_bread, baguette, cake, cookies, candy, choc_candy, nougat]


for item in all_items:
    number = random.randint(70, 250)
    fruits_candy.deliver(item, number)





name = input("Welcome to the Worlds of Stores, what's your name?\n")
wallet = input("Today we suggest shopping at the Fruits&Canddy store. What is your budget in $?\n")


customer = Shopper(name, int(wallet))

customer.shopping(fruits_candy)
