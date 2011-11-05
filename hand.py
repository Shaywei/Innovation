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
        self.max_age = 0
                                          
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
        choice = input('Choose a card from your hand:')
        choice = int(choice)
        if int(choice) <= self.hand_size:
            return self.hand[choice-1]
        else:
            print ('Invalid choice. Choose again.')
            return self.choose_card()
    
    def update(self):
        self.hand_size = len(self.hand)
        self.hand.sort()
        if self.hand_size > 0:
            self.max_age = self.hand[self.hand_size-1].age
        else:
            self.max_age = 0
    
    def get_size(self):
        return self.hand_size
        
    def add_to_hand(self, card):
        print(self.owning_player.name+' added: '+card.name + ' to hand.')
        self.hand.append(card)
        self.update()

    def remove_by_index(self, index):    
        card_to_return = self.hand.pop(index)
        print('Removed: '+card_to_return.name)
        self.update()
        return card_to_return
        
    def remove_by_name(self, name):
        card_to_return_index = [card.name for card in self.hand].index(name)
        card_to_return = self.hand.pop(card_to_return_index)
        self.update()
        return card_to_return
                
    def get_filtered_hand(self, key):
        ''' Returns all cards that matches given criteria without removing from hand'''
        return [card for card in self.hand if key(card)]
        
    def pop_filtered_hand(self, key):
        '''Returns all cards that matches given criteria also removing them from hand'''
        cards_to_return = []
        for card in self.hand:
                if key(card): cards_to_return.append(card)
        for card in cards_to_return: self.remove_by_name(card.name)
        return cards_to_return
