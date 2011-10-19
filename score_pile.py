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
        self.lowest_card_age = None
        self.score = 0
       
                                          
    def print_self(self):
        ''' This method prints the pile. '''
        if len(self.score_pile) == 0:
            print ('This pile is empty!')
        else:
            print ('Your score pile contains (from bottom to top):')
            for i in range(len(self.score_pile)):
                print('{0}. '.format(i+1),)
                self.score_pile[i].print_self()
                print()
            print()       
            
    def update_higest_lowest_ages(self):
        assert self.score_pile != [] , 'updating empty score pile'
        self.score_pile.sort(key = lambda card : card.age)
        self.highest_card_age = self.score_pile[len(self.score_pile) - 1].age
        self.highest_card_age = self.score_pile[0].age
        print()
        print(self.owning_player.get_name() + ', You now have: ' + str(self.score) + ' points!')
        print()
        
    def add_to_score_pile(self, card):
        self.score += card.age
        self.score_pile.append(card)
        self.update_higest_lowest_ages()
    
    def remove_from_score_pile(self, index):
        assert (index in range(len(self.score_pile) , 'Trying to remove a card that doesn\'t exist in score pile.'))
        card_to_remove = self.score_pile.pop(index)
        self.score -= card_to_remove.age
        self.update_higest_lowest_ages()
        return card_to_remove
    
    def get_filtered_score_pile(self, key):
        return [card for card in self.score_pile if key(card)]
          
