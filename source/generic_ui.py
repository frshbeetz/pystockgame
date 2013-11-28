#This should contain a "Generic" kind of UI for an eventual
#ncurses or otherwise renderable UI class to be derived from.
#So, the main job here is to explicitly lay out what functions
#are available to render a UI.
#It may even be possible/useful to use a derived class to "render" the
#game state over the network, to other players. This partmay or may not
#be a good idea.

import game_state

class generic_ui:
        def init(self):
        
        def render(self, game_state):
            