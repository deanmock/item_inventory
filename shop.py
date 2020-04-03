#shop.py
#quick python object program - a simple inventory checker for a coffee
#bean product
#TODO - add more classes for different products and add to menu toggling between products

class SumatranBeans:
	def __init__(self,stock=0):
		self.stock = stock


	def displaystock(self):
		print("We have currently {} bags of beans available for purchase.".format(self.stock))
		return self.stock

	def SaleMade(self, x):
		if x <= 0:
			print("Enter a valid number")
			return None

		elif x > self.stock:
			print("Inventory cannot fulfil this order. There are only {} items available for purchase.".format(self.stock))
			return None

		else:
			self.stock -= x
			print("{} units have been sold. {} units remaining.".format(x, self.stock))
			return None

	def addStock(self, y):
		new = y
		if new <= 0:
			print("Enter a valid number")
			return None
		else:
			self.stock += new
			print("{} units added. {} units total.".format(new, self.stock))
			return None

class Shopkeeper:

    def __init__(self):
    	self.items = 0
    	self.capacity = 10,000

    def depleteStock(self):
        
                      
        items = input("How many items were sold?")
        try:
            items = int(items)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if items < 1:
            print("Invalid input. Number of items should be greater than zero!")
            return -1
        else:
            self.items = items
        return self.items

    def replenishStock(self):
        items = input("How many items were sold?")
        try:
            items = int(items)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if items < 1:
            print("Invalid input. Number of items should be greater than zero!")
            return -1
        else:
            self.items = items
        return self.items
