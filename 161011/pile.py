'''
Created on 09/10/2011

@author: lost_dm

This class represents a pile of certain color in-game on a player's board.
'''

import card
import player

symbols_dict = {'CROWN' : 0, 'LEAF' : 1, 'LIGHTBULB' : 2, 'CASTLE' : 3 , 'FACTORY' : 4 , 'CLOCK' : 5}

splay_dict = { "NONE" : 0 , "LEFT" : 1 , "RIGHT" : 2 , "UP" : 3 }
splay_visibility = ((0,0,0,0),(0,0,0,1),(1,1,0,0),(0,1,1,1))
splay_unvisibility = ((1,1,1,1),(1,1,1,0),(0,0,1,1),(1,0,0,0))

''' The splay_visibility matrix represents the visibility of the symbols relative to the splay mode.
    For example, since splay mode "RIGHT" is represented by 2 which is the index of the third row
    only symbols at indecise 0 and 1 are visible - the left symbols on the card. 
    
    The splay_unvisibility represents which symbols are being hidden one you meld on top of a top card
    relative to the splay mode.
    
    A 'visibility' parameter is just a single row of such matrix.                                               '''


class Pile:

    def __init__(self, owning_player, color):
        
        self.owning_player = owning_player
        self.color = color
        self.pile = []
        self.splay_mode = 'NONE'
        self.top_card = None
       
        self.symbol_count = [0,0,0,0,0,0] # By index: 0 -> CROWN, 1 -> LEAF, 2 -> LIGHTBULB \
                                          #           3 -> CASTLE, 4 -> FACTORY, 5 -> CLOCK
        
    def print_symobls_count(self):
        print ( self.color + ' current Symbol Count: ')
        print('Crowns - {0}, Leaves - {1}, Lightbulbs - {2}, Castles - {3}, Factories - {4}, Clocks - {5}'.format(self.symbol_count[0],self.symbol_count[1],self.symbol_count[2],self.symbol_count[3],self.symbol_count[4],self.symbol_count[5]))
        print()
                                          
    def print_self(self):
        ''' This method prints the pile. '''
        if len(self.pile) == 0:
            print ('This pile is empty!')
        else:
            print('Splay mode is: ' + self.splay_mode)
            self.print_symobls_count()
            print ('Your ' + self.color + ' pile contains (from bottom to top):')
            for i in range(len(self.pile)):
                print('{0}. '.format(i+1),)
                self.pile[i].print_self()
                print()
            print()
    
    def print_top_card(self):
        if len(self.pile) == 0:
            pass
        else:
            print ('Your top ' + self.color + ' card is: ')
            self.pile[len(self.pile) - 1].print_self()
            
    def get_top_card_reference(self):
        return self.pile[len(self.pile)-1]
        
    def get_visibility(self):
        splay_index = splay_dict[self.splay_mode]
        return splay_visibility[splay_index]
    
    def get_unvisbility(self):
        splay_index = splay_dict[self.splay_mode]
        return splay_unvisibility[splay_index]
    
    def get_symbol_count(self):
        return self.symbol_count
        
    def remove_symbols_of_a_card(self, visibility, card_symbols):
        for i in range(4):
            symbol = card_symbols[i]
            if visibility[i] == 1 and symbol != 'FLAVOR':
                self.symbol_count[symbols_dict[symbol]] -= 1
                #self.owning_player.remove_symbol_from_count(symbol)
    
    def add_symbols_of_a_card(self, visibility, card_symbols):
        for i in range(4):
            symbol = card_symbols[i]
            if visibility[i] == 1 and symbol != 'FLAVOR':
                self.symbol_count[symbols_dict[symbol]] += 1
                #self.owning_player.add_symbol_to_count(symbol)
    
    def tuck(self, card):
        self.add_symbols_of_a_card(self.get_visibility(), card.get_symbols())
        self.pile.insert(0, card)

    def meld(self, card):
        if len(self.pile) > 0:
            self.remove_symbols_of_a_card(self.get_unvisbility(), self.top_card.get_symbols()) # Remove covered symbols.
        self.pile.append(card)                                                                 # Append new card.
        self.top_card = card                                                                   # Update new top_card.
        self.add_symbols_of_a_card((1,1,1,1), card.get_symbols())                              # Add new symbols.
        print (card.name + 'Was melded.')
        
    def transfer_top_card(self):
        ''' This method removes the top card of a pile. '''
        pile_size == len(self.pile)                                 
        if pile_size == 0:                                 # Check if pile is empty.
            return None
        else:                                              
            top_card = self.pile.pop()
            pile_size -= 1        
            if pile_size == 0:                             # Check if we popped the last card
                self.top_card = None
            else:
                self.top_card == self.pile[pile_size-1]    # If not, update top card.
            if pile_size == 1 and splay_mode != 'NONE':    # Check if the pile is now unplayed
                self.change_splay_mode('NONE')         
            return top_card
            
    def transfer_bottom_card(self):
        ''' This method removes the bottom card of a pile. '''
        pile_size == len(self.pile)                                 
        if pile_size == 0:                                 # Check if pile is empty.
            return None
        else:                                              
            bottom_card = self.pile.pop(0)
            pile_size -= 1        
            if pile_size == 0:                             # Check if we popped the last card
                self.top_card = None
            elif pile_size == 1 and splay_mode != 'NONE':  # Check if the pile is now unplayed
                self.change_splay_mode('NONE')         
            return bottom_card

    def change_splay_mode(self, new_splay_mode):
        ''' This method should be called every time the splay_mode is changed. '''
        assert new_splay_mode in ('NONE', 'LEFT', 'RIGHT', 'UP'), 'Invalid Splay Mode'
        if (len(self.pile) < 2):
            print('Unable to splay ' + self.color + ' ' + new_splay_mode + ', less then 2 cards')
        else:
            self.splay_mode = new_splay_mode                                    # Change splay_mode
            self.symbol_count = [0,0,0,0,0,0]                                   # Reset symbol_count
            visibility = self.get_visibility()                                  # get (new) visibility.
            for i in range(len(self.pile) - 1):                                 # update all non-top cards symbols.
                symbols = self.pile[i].get_symbols()
                self.add_symbols_of_a_card(visibility, symbols)
            self.add_symbols_of_a_card((1,1,1,1), self.top_card.get_symbols())  # All the symbols of top_card are visible.
            