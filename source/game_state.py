#Holds info about the state of a game.
#Player state. Stock Prices. News Items. Bank status
#Round info etc. should all be stored here.  Each should
#be a list encapsulated in the game state object.
#The game state should be exposed to the UI,
#and it must also be serializable for network transmission. 

import time

class game_state:
    
    def __init__(self):
    #I'm simply setting members up as arrays or int types for the moment.
    #Types are likely to change in the future.
        self.players = []
        self.time_start = time.gmtime()
        self.time_now = time.gmtime()
        self.round_number = 0
        
        #arbitrary -- maybe should be passed to init
        self.num_rounds = 10
        self.news_items = []
        
        
