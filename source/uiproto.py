import curses
from curses import panel
import sys

# This probably can't even be considered software yet
version = "0.1a"

# Initialize Curses
screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
curses.noecho()
curses.curs_set(0)
screen.keypad(1)

# Tickers & Opening Prices - I need to do all of this with functions or some sort of database? I think.
tck1 = "GOOG"
tck1p0 = 1000
tck1p1 = 1500

tck2 = "APPL"
tck2p0 = 1000

tck3 = "NFLX"
tck3p0 = 1000

tck4 = "AMD"
tck4p0 = 1000

tck5 = "INTL"
tck5p0 = 1000

# Create The Window - MUST BE AT LEAST 126 Wide by 39 Tall - Because I don't know how to do it the right way.
global win
win = screen.subwin(39, 126, 0, 0)
win.box()
win.refresh()

# win.addstr(1, 78, (sys.version)) 
win.addstr(1, 78, "       Python Networked Stock Market Game" + " " + version + " ", curses.color_pair(2))
win.addstr(1, 2, "PLAYER: PLAYER 01")
win.addstr(1, 55, "TIME LEFT:")
win.vline(1, 77, curses.ACS_VLINE, 37)

# Stock Board
mktwin = win.subwin(34, 76, 2, 1,)
mktwin.box()
mktwin.hline(1, 1, curses.ACS_HLINE, 74)
mktwin.hline(3, 1, curses.ACS_HLINE, 74)
mktwin.vline(2,  5, curses.ACS_VLINE, 31)
mktwin.vline(2, 12, curses.ACS_VLINE, 31)
mktwin.vline(2, 19, curses.ACS_VLINE, 31)
mktwin.vline(2, 26, curses.ACS_VLINE, 31)
mktwin.vline(2, 33, curses.ACS_VLINE, 31)
mktwin.vline(2, 40, curses.ACS_VLINE, 31)
mktwin.vline(2, 47, curses.ACS_VLINE, 31)
mktwin.vline(2, 54, curses.ACS_VLINE, 31)
mktwin.vline(2, 61, curses.ACS_VLINE, 31)
mktwin.vline(2, 68, curses.ACS_VLINE, 31)

# Add Headers
mktwin.addstr(2, 7, "OPEN")
mktwin.addstr(2, 14, "RND1")
mktwin.addstr(2, 21, "RND2")
mktwin.addstr(2, 28, "RND3")
mktwin.addstr(2, 35, "RND4")
mktwin.addstr(2, 42, "RND5")
mktwin.addstr(2, 49, "RND6")
mktwin.addstr(2, 56, "RND7")
mktwin.addstr(2, 63, "RND8")
mktwin.addstr(2, 70, "RND9")

# Add Tickers & Opening Prices - This is all wrong...
mktwin.addstr(4,  1, tck1)	

# mktwin.addstr(5,  8, str(tck1p0))
# mktwin.addstr(5, 13, str(tck1p1))
# win.addstr(5, 18, str(tck1p0))
# win.addstr(5, 23, str(tck1p0))
# win.addstr(5, 28, str(tck1p0))
# win.addstr(5, 33, str(tck1p0))
# win.addstr(5, 38, str(tck1p0))
# win.addstr(5, 43, str(tck1p0))
# win.addstr(5, 48, str(tck1p0))
# win.addstr(5, 53, str(tck1p0))
# win.addstr(5, 64, str(tck1p0))

mktwin.addstr(5, 1, tck2)
mktwin.addstr(6, 1, tck3)
mktwin.addstr(7, 1, tck4)
mktwin.addstr(8, 1, tck5)

# Create side stats window - Unique to each player...eventually...
global statswin
statswin = win.subwin(34, 47, 2, 78)
statswin.box()
statswin.addstr(1, 1, ">-----------------PORTFOLIO-----------------<")
statswin.addstr(3, 1, "TICK")
statswin.addstr(3, 9, "SHARES")
statswin.addstr(3, 22, "$VALUE")
statswin.addstr(3, 35, "GAINLOSS")
statswin.hline(2,  1, curses.ACS_HLINE, 45)
statswin.hline(4,  1, curses.ACS_HLINE, 45)
statswin.hline(31, 1, curses.ACS_HLINE, 45)
statswin.addstr(32, 1, "PORTFOLIO VALUE:")
statswin.vline(3, 5, curses.ACS_VLINE, 28)
statswin.vline(3, 18, curses.ACS_VLINE, 28)
statswin.vline(3, 31, curses.ACS_VLINE, 28)

# Player Balances Label
win.addstr(36, 79, "CASH BALANCE:", curses.color_pair(1))
win.addstr(37, 79, "NET WORTH:")
win.addstr(36, 2, "AVAILABLE SHARES:")
win.addstr(37, 2, "MAJORITY SHAREHOLDER:")

# I honestly don't totally understand this last bit.
while True:
    event = screen.getch()
    if event == ord("q"): break
curses.endwin=()
