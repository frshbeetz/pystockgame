# Well... Here goes...
# init some variables
stockprice = 100.0
current_balance = 1000
shares_held = 10
shares_added = 0
shares_removed = 0
position_value = stockprice * shares_held

# Define some transaction functions
def add_shares(shares_held,quantity):
	return shares_held + quantity
def remove_shares(shares_held,quantity):
	return shares_held - quantity
def transaction_negative(current_balance,cost):
	return current_balance - cost
def transaction_positive(current_balance,plus):
	return current_balance + plus
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
		current_balance = transaction_positive(current_balance,plus)
		shares_removed = remove_shares(shares_held, quantity)
		return (True, current_balance, shares_removed)

# Here begins the interactive section
quantity = None
valid_input = False
while valid_input == False:
	buysell = raw_input("Buy or Sell?(B/S): ").lower()
	valid_input = True
	if buysell == "b":
		xact_string = "buy"
		xact_fn = buy
	elif buysell == "s":
		xact_string = "sell"
		xact_fn  = sell
	else:
		valid_input = False
		print "B or S it's not hard."
	
# loop until user inputs a valid number.
while not quantity:
	print "You have %d shares." % (shares_held)
	print "Your position is worth $%d" % (position_value)
	try:
		quantity = input("The stock is $%d per share. How many shares do you want to %s?: " % (stockprice, xact_string))
	except:
		print('Invalid Input!')
		quantity = None
result, current_balance, shares_added = xact_fn(stockprice, quantity, current_balance)
print "%r,$%.2f,%d" % (result, current_balance, shares_added)

