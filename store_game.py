from Items import Item
from Shopper import Shopper
from Store import Store
import random


### Creating Item class productc with initial name, price, category
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

# Giving discounts to products
apple.do_sale(20)
nougat.do_sale(30)
pear.do_sale(10)

# Store instance
fruits_candy = Store('Fruits&Candy', 10000)
print(fruits_candy)

#Adding items to the shop inventory
all_items = [strawberry, pear, apple, banana, bread, roll, rye_bread, baguette, cake, cookies, candy, choc_candy, nougat]

#Iterating through products in order to add them in random quantity to the store's assortment 
for item in all_items:
    number = random.randint(70, 250)
    fruits_candy.deliver(item, number)


#Initiating a conversation with a player
name = input("Welcome to the Worlds of Stores, what's your name?\n")
wallet = input("Today we suggest shopping at the Fruits&Canddy store. What is your budget in $?\n")

#Creating player instances and launching functions with game mechanics
customer = Shopper(name, int(wallet))
customer.shopping(fruits_candy)
