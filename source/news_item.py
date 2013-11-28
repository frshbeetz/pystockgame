#News items should have a polarity rating - eg they should make any stocks
#they mention move in a given direction.


class news_item:
    def __init__(self):
        self.stock_ticker = ""
        self.polarity = 0   #no effect by default
        self.heading = ""
        self.text = ""