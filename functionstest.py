# This code is written poorly and doesn't work.

current_balance = 1000
stockprice = 100
shares_held = 10

# If I knew what I was doing, these would probably be one function.

def add_shares(shares_held,quantity):
	newshares_held = shares_held + quantity
	shares_held = newshares_held
	return shares_held

def remove_shares(shares_held,quantity):
	newshares_held = shares_held - quantity
	shares_held = newshares_held
	return shares_held

def transaction_negative(current_balance,cost):
	newbalance = current_balance - cost 
	current_balance = newbalance
	return current_balance

def transaction_positive(current_balance,plus):
	newbalance = current_balance + plus 
	current_balance = newbalance
	return current_balance
"""	
 For some reason calling the buy and sell functions breaks the program 
 on the grounds that current_balance is a string and not an integer... I can't figure out why.
"""
	
def buy(stockprice, quantity, current_balance):
	cost = stockprice * quantity
	if current_balance - cost < 0:
		print "Insufficient Funds"
	else:
		transaction_negative(current_balance,cost)
		addshares(shares_held, quantity)
		print "You hold: " + str(shares_held) + " shares."
		print "Your remaining balance is: $" + str(current_balance)

def sell(stockprice, quantity, current_balance):
	plus = stockprice * quantity
	if shares_held  < quantity:
		print "Insufficient Shares"
	else:
		transaction_positive(current_balance,plus)
		remove_shares(shares_held, quantity)
		print "You hold: " + str(shares_held) + " shares."
		print "Your remaining balance is: $" + str(current_balance)

# Asks the user explictly for B or S because I'm lazy.  Then calls the functions... or rather... breaks.

buysell = raw_input("Buy or Sell?(B/S): ")
if buysell == "B":
	quantity = None
	# loop until user inputs a valid number.
	while not quantity:
		quantity = raw_input("The stock is $" + str(stockprice) + " per share." " How many shares do you want to buy?: ")
		try:
			# convert to float number for math
			quantity = float(quantity)
		except:
			# user entered non-number input
			print('Invalid amount given!')
			quantity = None
	
	print buy(stockprice, quantity, current_balance)
elif buysell == "S":
	quantity = raw_input("The stock is $" + str(stockprice) + " per share." " How many shares do you want to sell?: ")
	print sell(stockprice, quantity, current_balance)
else:
	print "Invalid Input"
