

class Item:
  def __init__(self, name, price, type, sale=False, sale_amount=0):

    # Regular atr
    self.name = name
    self.price = price
    self.type = type

    # Sale atr
    self.sale = sale
    self.sale_amount = sale_amount
    self.regular_price = price

  
  def __repr__(self):

    description = "Normal price for {name} is {price} $. {type} product. ".format(
      name=self.name,
      price = self.regular_price,
      type = self.type)

    if self.sale:
        description += '{name} is now on {sale_amount} % sale. Current cost: {new_price} $.'.format(name=self.name, sale_amount=self.sale_amount, new_price=self.price)

    else:
        pass

    return description

  def do_sale(self, sale_amount):

    self.sale_amount += sale_amount
    self.regular_price = self.price
    sale = self.price * sale_amount / 100
    self.price -= sale
    self.sale = True

    return 'Sale {sale_amount} % added. {name} cost now {price} $.'.format(sale_amount=self.sale_amount, name=self.name, price=self.price)

  def regular_price_fun(self):
    self.price = self.regular_price
    self.sale = False
    self.sale_amount = 0
    return '{item} backed to regular price. Its cost now {price} $.'.format(item=self.name, price=self.price)