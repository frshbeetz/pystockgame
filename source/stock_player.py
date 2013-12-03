#Should contain info about the state of a single player.
#Info might include: Name, list of (ticker, shares_held) tuples,
#account value, cash available, debts owed, etc.  

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
# | 	|
# | 	+-------LandCorp
# |	
# |
# +----ENERGY COMPANIES
# 	 |
# 	 +------GasEnergy
# 	 |		Seed = Gas COMMODITY
# 	 +------CoalEnergy
# 			Seed = Coal COMMODITY
#
# COMMODDITIES
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
# +----AGRICULTUAL COMMODITIES
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
