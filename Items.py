class Item:
  # Item class with name, price, type of product, sale applied/sale amount 
  def __init__(self, name, price, type, sale=False, sale_amount=0):
    # 

    self.name = name
    self.price = price
    self.type = type

    self.sale = sale
    self.sale_amount = sale_amount
    self.regular_price = price

  
  def __repr__(self):

    description = "Normal price for {name} is {price} $. {type} product. ".format(
      name=self.name,
      price = self.regular_price,
      type = self.type)

    if self.sale:
        description += f'{self.name} is now on {self.sale_amount} % sale. Current cost: {self.price} $.'

    else:
        pass

    return description

  # Methods do_sale/regular_price_method - to set or to end the sale
  def do_sale(self, sale_amount):

    self.sale_amount += sale_amount
    self.regular_price = self.price
    sale = self.price * sale_amount / 100
    self.price -= sale
    self.sale = True

    return f'Sale {self.sale_amount}% applied. {self.name} cost now {self.price} $.'

  def regular_price_method(self):
    self.price = self.regular_price
    self.sale = False
    self.sale_amount = 0
    return f'{self.name} backed to regular price. Its cost now {self.price} $.'