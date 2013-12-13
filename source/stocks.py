#Should contain Stock info
#Price, shares available
#Description

# Equities - These are the Companies
# |	
# +-----BLUE CHIP COPORATIONS/CONGLOMERATES
# |	|
# |	+-------UltraCorp
# |	|		Highest Tier Corporation
# |	|		Highest starting EQUITY price 
# |	|		Seed = Average of Commodity Indexes
# |	|		Volatility = low	
# |	+--------MegaCorp
# |	|		High Tier Corporation
# |	|		High starting EQUITY price
# |	|		Seed = Average of Commodity Indexes * 1.25
# |	|		Volatility = mid	
# |	+--------MultiCorp
# |     |		Low Tier Corporation
# |	|		Low starting EQUITY Price
# |	|		Seed = Average of Commodity Indexes * 1.50
# |	|		Volatility = high
# |	+--------Unicorp
# |			Lowest Tier Corporation
# |			Lowest Starting EQUITY Price
# |			Seed = Average of Commodity Indexes * 2
# |			Volatility = highest
# |
# +-----INDUSTRIAL COMPANIES
# |	 |
# |	 +------SteelCorp 
# |	 |	 	Seed = Average of Industrial Metals
# |	 |	 	Starts at a highest price of INDUSTRIAL COMPANIES
# |	 +------FactoryCorp
# |	 |		Seed = Average of Industrial Metals
# |	 |		Starts at mid price of INDUSTRIAL COMPANIES
# |	 +------FarmCorp
# |			Seed = Average of AGRICULTURAL COMMODITIES
# |			Starts at lowest price of INDUSTRIAL COMPANIES
# |
# +----TRANSPORT COMPANIES
# |	|
# |	+-------AirCorp
# |     |       	Seed based on energy prices
# | 	|
# | 	+-------LandCorp
# |			Seed based on energy prices
# |
# +----ENERGY COMPANIES
# 	 |
# 	 +------GasEnergy
# 	 |		Seed = Gas COMMODITY
# 	 +------CoalEnergy
# 			Seed = Coal COMMODITY
#
# COMMODITIES
# |
# +----ENERGY
# |	 |
# |	 +----OIL
# |	 |
# |	 +----COAL
# |	 |
# |	 +----GAS
# |
# +----INDUSTRIAL METALS
# |	 | 
# |	 +----STEEL
# |	 |
# |	 +----ALUMINUM
# |
# +----AGRICULTURAL COMMODITIES
# |	 |
# |	 +----WHEAT
# |	 |
# |	 +----COFFEE
# |	 |
# |	 +----LIVESTOCK
# |
# +----PRECIOUS METALS
# 	 |
# 	 +------GOLD
#	 |        Inversely moves with WHOLE MARKET INDEX 
#	 |	  High price & High Volatility
#	 +------SILVER
#	 	  Inversely moves with WMI
#	 	  LOW price & mid Volatility
#
# INDEXES - Average of the underlying
# |
# +----Whole Market
# |
# +----Blue Chips
# |
# +----Industry Cos
# |
# +----Transportation Cos
# |
# +----Energy Cos
# |
# +----Whole Commodities
# |
# +----Energy Com.
# |
# +----Agric Com.
# |
# +----Precious Metals
#
# BONDS
# |
# +---BONDS GAIN a low fixed rate per turn.

TICKERS

# Corporations [ULTR,MEGA,MULTI,UNIC,STCO,FACT,FARM,AIRC,LAND,GACO,COCO]
# Commoddities [OIL, COAL, GAS, STEEL, ALUM, WHT, COFF, LIVE]
# Precious Metals [AU, AG]
# Indexes [XWMI, XBLU, XIND, XTRA, XENC, XCOM, XNRG, XAGR, XAUG]
# Bonds [BOND]

# These are the basic companies, each should respond to related commodities
# in a more or less realistic way, IE: Oil prices being high will cause
# lost revenue for transport companies.
# The amount of shares Bought or Sold should affect the volatility in some way.
# IE: If more shares are bought than sold, the price should trend up.
#	the same should happen in reverse if the reverse is true.
class Equities:

	def __init__(self)
		self.ticker = None
		self.price = None # based on change from round 0 opening price
		self.volatity = None # calculation based on related Commod. / News
		self.sharesAvail = None # default 1000000
		self.desc = None # A short description of the company

# I know this is the same as above, but later on when we want to make a
# distinction between the two, hopefully it'll make sense to do it like
# this.
class Commodities:

	def __init__(self)
		self.ticker = None
		self.price = None # Generally lower priced than equities
		self.volatility = None # calculation based on News/Random Number Gen
		self.commodAvail = None # default 5000000
		self.desc = None # A short description of the commodity

# Precious metals should move inversely to the markets. While not a rule IRL,
# this will give players a means to "bet against" the whole market index.
# Gold should start at a higher price than Silver.
# Gold = high/mid volatility | Silver = low volatility
# It would be cool to initialize the values with the spot price of gold/silver
# from the internet.
class PrecMetals:
	
	def ___init__(self)
		self.ticker = None
		self.price = None 
		self.volatility = None # calculation based on XWMI price change

# Indexes should be based on a calculation of the underlying stocks.
# Whole Market Index should be an average of all Equities and Commod. prices.
# Energy Co's index would be just an average of the Energy Companies prices.
class Indexes:
	
	def __init__(self)
		self.ticker = None
		self.price = None

# Bonds are a non-volatile investment option.  Basically they should gain
# a small amount consistently every round.  The price should be set to par
# ($100) by default.  But it could be configured.  The rate of return could
# be set at say 5% by default, or fluctuate between non-negative values.
# If we implement Loans, we could base bonds off of the interest rate.
class Bonds:

	def __init__(self)
		self.ticker = None
		self.price = None	
