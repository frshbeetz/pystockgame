# This code is written poorly and doesn't work.
current_balance = 1000
stockprice = 100.0
shares_held = 10
shares_added = 0
# If I knew what I was doing, these would probably be one function.
def add_shares(shares_held,quantity):
	return shares_held + quantity
def remove_shares(shares_held,quantity):
	return shares_held - quantity
def transaction_negative(current_balance,cost):
	return current_balance - cost
def transaction_positive(current_balance,plus):
	return current_balance + plus
"""	
Fixed by welbornprod!
 For some reason calling the buy and sell functions breaks the program 
 on the grounds that current_balance is a string and not an integer... I can't figure out why.
"""
def buy(stockprice, quantity, current_balance, balance_threshold=0):
	cost = stockprice * quantity
	if current_balance - cost < balance_threshold:
		return (False, current_balance, 0)
	else:
		current_balance = transaction_negative(current_balance,cost)
		shares_added = add_shares(shares_held, quantity)
		return (True, current_balance, shares_added)

def sell(stockprice, quantity, current_balance):
	plus = stockprice * quantity
	if shares_held  < quantity:
		return (False, current_balance, 0)
	else:
		transaction_positive(current_balance,plus)
		remove_shares(shares_held, quantity)
		return (True, current_balance, shares_held)

# Asks the user explictly for B or S because I'm lazy.  Then calls the functions... or rather... breaks.

buysell = raw_input("Buy or Sell?(B/S): ").lower()
if buysell == "b":
	quantity = None
	# loop until user inputs a valid number.
	while not quantity:
		quantity = raw_input("The stock is $" + str(stockprice) + " per share." " How many shares do you want to buy?: ")
		try:
			# convert to int  number for math - no fraction shares.
			quantity = int(quantity)
		except:
			# user entered non-number input
			print('Invalid amount given!')
			quantity = None
	
		result, current_balance, shares_held = buy(stockprice, quantity, current_balance)
		print "%r,%.2f.%d" % (result, current_balance, stocks_added)

elif buysell == "s":
	quantity = raw_input("The stock is $" + str(stockprice) + " per share." " How many shares do you want to sell?: ")
	print sell(stockprice, quantity, current_balance)

else:
	print "Invalid Input"
