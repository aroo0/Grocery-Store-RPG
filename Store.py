from re import L
import pandas as pd
import numpy as np
from Items import Item


class Store:

  # Whole sale rate determines the amount at which the store buys from the wholesaler,
  #if we assume that the customer buys an item for 1 
  # then the store bought from the wholesaler for 0.7 and has an earnings of 0.3
  wholesale_rat = 0.7

  def __init__(self, name, budget=1000, inventory={}):
    self.name = name
    self.budget = budget
    self.inventory = inventory
    self.sale_product = []

  def __repr__(self):
    return 'Shop name: {name}\nCash in hand: {cash} $'.format(name=self.name, cash=round(self.budget, 2))
    
    

  def inventory_display(self):
    # Displaying the assortment as a dataframe
    print("Inventory:\n~~~~")
    names = [item.name for item in self.inventory.keys()]
    amounts = [item for item in self.inventory.values()]
    prices = [item.price for item in self.inventory.keys()]
    table = pd.DataFrame(
      {'Name': names,
      'Price $': prices,
      'Amount': amounts
    })
    table.index = np.arange(1, len(table)+1)
    print(table)

    return range(len(table))

  def deliver(self, product, amount):
    # Purchase of products by the store from a wholesaler.
      if type(product) is Item:
          cost = product.price * amount * self.wholesale_rat
          round_cost = round(cost, 2)

          if self.budget - round_cost < 0:
              run_out_amount = round(abs(self.budget - round_cost), 2)

              print('Store has no enough money. Current store budget is {budget} $. The order of {amount} {product} costs {cost_order}. You are {dif} $ short. Try a smaller amount.'.format(budget=round(self.budget, 2),amount=amount, product=product.name, cost_order = round_cost, dif=run_out_amount))

          else:
              self.budget -= round_cost
              self.inventory[product] = amount
              print(
                '''
                        Products succesfull delivered. 
                        Store current budget: {budget} $
                        The delivery: {name} in {amount} amount.
                        Delivery cost: {cost} $
              '''
              .format(budget=round(self.budget, 2), name=product.name, amount=amount, cost=round_cost))

      else:
        return '{product} is not available at wholesale.'.format(product=product)

  def buy(self, item, amount):
    # Integrated with Shopper class buying function.

    self.inventory[item] -= amount 
    self.budget += item.price * amount


  def display_sale(self):
    #Displaying products on sale
    for item in self.inventory.keys():
      if item.sale:
        print('{number}.'.format(number=number), item, 'Amount x {amount}'.format(amount=self.inventory[item]))
        number += 1
        self.sale_product.append(item)

    return list(range(1,number+1))


  def checking_sale(self):

    for item in self.inventory.keys():
      return not item.sale
      

  def farwell(self):
    print('{name} store thanks you for your time. See you soon!'.format(name=self.name))



