'''
Created on 16/10/2011

@author: lost_dm

This class represents a score pile of certain player.
'''

import card
import player

class ScorePile:

    def __init__(self, owning_player):
        
        self.owning_player = owning_player
        self.score_pile = []
        self.highest_card_age = None
        self.score = 0
       
                                          
    def print_self(self):
        ''' This method prints the number of points the player has. '''
        print(self.owning_player.get_name() + ' has: ' + str(self.score) + ' points.')
        print()

    def print_self(self):
        ''' This method prints the pile. '''
        if len(self.pile) == 0:
            print ('This pile is empty!')
        else:
            print ('Your score pile contains (from bottom to top):')
            for i in range(len(self.pile)):
                print('{0}. '.format(i+1),)
                self.pile[i].print_self()
                print()
            print()       
        
    #def transfer_card(self):
        ''' This method removes the top card of a pile. 
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
            return top_card'''
