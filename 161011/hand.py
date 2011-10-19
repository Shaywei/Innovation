'''
Created on 11/10/2011

@author: lost_dm

This class represents the hand of a certain player.
'''

import card
import player

class Hand:

    def __init__(self, owning_player):
        self.owning_player = owning_player
        self.hand = []
        self.hand_size = 0        
                                          
    def print_self(self):
        ''' This method prints the hand. '''
        if len(self.hand) == 0:
            print ('Hand is empty.')
        else:
            print ('Your hand contains:')
            for i in range(len(self.hand)):
                print('{0}. '.format(i+1),)
                self.hand[i].print_self()
                print()
            print()
    
    def choose_card(self):
        choice = input('choose a card from your hand:')
        choice = int(choice)
        if int(choice) <= self.hand_size:
            return self.hand[choice-1]
        else:
            print ('Invalid choice. Choose again.')
            return self.choose_card()
        
    def get_size(self):
        return self.hand_size
        
    def add_to_hand(self, card):
        self.hand.append(card)
        self.hand_size += 1

    def remove_from_hand(self, index):
        index -= 1
        self.hand_size -= 1        
        return self.hand.pop(index)
