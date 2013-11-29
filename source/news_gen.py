#A module which generates news items.
#News items may be "generated" by reading from a file or perhaps something
#more devious (to be determined).  
#Since there may be different ways of generating news, it is prudent to
#leave this as a base class, and have derived modules work out the 
#details.

class news_gen:
    def __init__(self):
    
    #Derived 
    def get_news(self):
        return 0