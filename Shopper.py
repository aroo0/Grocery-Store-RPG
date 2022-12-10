from Items import Item

class Shopper:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        #items in cart
        self.cart = {}
        # how much items costs
        self.cart_sum = 0
        # what was eventually purchased
        self.bought = {}


    def __repr__(self):
        return 'Hi! I`m {}. My shopping money is {} $'.format(self.name, self.wallet)

    
    def add_to_cart(self, product, amount, store):
      # Adding products to the shopping cart from the store's assortment.


        if type(product) != Item:
          # checking if item exists
            print('Sorry, {} is not in our storage. ;('.format(product.name))

        elif amount > store.inventory.get(product):
          # checking if there is enough product in stock
            print(
              'Sorry, there is only {amount} of {product} in our storage. Choose a lower quantity of product.'
              .format(
                amount = store.inventory.get(product),
                product = product.name
            ))

        else:
          # added to cart
            self.cart[product] = amount
            self.cart_sum += product.price * amount
            print('{} {} succesufly added to cart.'.format(amount, product.name))


    def display_cart(self):
      # printing of shopping cart contents, quantities, prices and total bill
      if not self.cart:
        print('Your cart is empty.')

      else:
          total_bill = 0
          number = 1
          for product, amount in self.cart.items():
              single_product_price = round((amount * product.price), 2)
              total_bill += single_product_price
              print('{}. {} x{}: {} $'.format(number, product.name, amount, single_product_price))
              number += 1
          print('--------------')
          print('Total bill: {} $'.format(round(total_bill, 2)))


    def remove_from_cart(self, product, amount):
        if self.cart[product] - amount < 0:
            print('You can`t have a negative number of {}. Choose smaller amount.'
            .format(product.name))

        else:
            self.cart[product] -= amount
            self.cart_sum -= product.price * amount
            print('{} successfully removed from the cart.'.format(product.name))

            if self.cart[product] == 0:
              self.cart.pop(product)

            else:
              pass


    def checking_for_money(self):
        if self.cart_sum < self.wallet:
            return True



    def settelment(self, store):


        if self.checking_for_money():
          for item, amount in self.cart.items():
            self.wallet -= item.price * amount
            self.bought[item] = amount
            store.buy(item, amount)
            print('{} {} bought.'.format(amount, item.name))
          self.cart.clear()

        else:
          print('Not enough money.')


    def display_wallet(self):
      print("Your current wallet is {} $".format(round(self.wallet, 2)))


    def display_bought(self):
      if not self.bought:
        print("You haven't bought anything yet.")

      else:
        print('You bought:')
        number = 1
        for item, amount in self.bought.items():
          print('{number}. {name} in {amount} amount for {price} $'.format(
            number=number, name= item.name,amount=amount, price = item.price*amount
            ))
          number += 1
        print('------------')
        print('Your bill: {amount} $'.format(amount=self.cart_sum))
        print('Your current wallet: {wallet} $'.format(wallet=self.wallet))


    def stock_shopping(self, store):
      # Looping the shopping selection
        answer = ''
        while answer != 'con':

          print('## Regular stock of {store} ##'.format(store=store.name))
          range = store.inventory_display()

          answer = input("\nWrite product number to select, or 'con' to go to the cart.\n")


          if answer == 'con':
            break


          try:
            # Adding items to your cart
            product_list = list(store.inventory)
            product = product_list[int(answer)-1]
            selected_product = store.inventory[product]
            print('You selected {name}. Amount in our storage: {amount}'.format(name=product.name, amount=selected_product))

            answer = input('What quantity do you want to add to your cart?\n')
            self.add_to_cart(product, int(answer), store)

            answer = input('Do you want to see a stock? Press "stock" or "con" to display cart.\n')

          except:
            print('Invalid input. Try again.')


    def shopping(self, store):

      #Main conversation from the beginning to the end of the game
      print('## {store} at your servise. ##\n'.format(store=store.name))

      if store.checking_sale():
        # Buying discounts 
        # There is no point in repeating intricate code, but this is the first project xd
        answer = ''

        while answer != 'con':
          print("Today's discounts are:")
          range = store.display_sale()

          answer = input("\nWrite item number to select, or 'con' to go to the regular stock.\n")

                  
          if str(answer) == 'con':
            break
          

          try:
            selected_product = store.sale_product[int(answer)-1]
            print('You selected {name}. Amount in our storage: {amount}'.format(name=selected_product.name, amount=store.inventory[selected_product]))

            answer = input('What quantity do you want to add to your cart?\n')
            self.add_to_cart(selected_product, int(answer), store)

            answer = input('Do you want to see a list of promotions again or go to the regular stock? Press "sale" or "con".\n')

          except:
            print('Invalid input or number out of range. There is no such product in our stock. Try diffrent number.')

        self.stock_shopping(store)


        answer = ''
        while answer != 'set':

          print('\nYour cart:')
          self.display_cart()
          print('\n')
          self.display_wallet()

          answer = input("Press 'remove' if you like to remove product from cart, press 'shop' if you want to add more product to the cart, and 'bill' if you like to settlement. Or 'esc' if you want to leave without buying.\n")

          if answer == 'remove':
            product = input('What product would you like to remove from your cart? Press product number.\n')

            try:
              list_cart = list(self.cart)
              selected = list_cart[int(product)-1]

              amount = input('Your selected {product}. In what quantity?\n'.format(product=selected.name))

              try:
                self.remove_from_cart(selected, int(amount))

              except:
                print('Sorry wrong number.\n')

            except:
              print('Sorry, wrong number.\n')

          elif answer == 'shop':
            self.stock_shopping(store)

          elif answer == 'bill':
          
            if self.checking_for_money():
              self.settelment(store)
              print('////////////////')
              answer = 'set'
              self.display_bought()
              store.farwell()
              
              

            else:
              print('Not enough money, try to remove products from your cart.')

          elif answer == 'esc':
            store.farwell()
            answer = 'set'


