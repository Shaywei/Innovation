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
        self.max_age_in_score_pile = 0
        self.min_age_in_score_pile = 0
        self.score = 0
        self.score_pile_size = 0
       
                                          
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
            
    def update(self):
        self.score_pile_size = len(self.score_pile)
        if self.score_pile_size > 0:
            self.score_pile.sort()
            self.max_age_in_score_pile = self.score_pile[len(self.score_pile) - 1].age
            self.min_age_in_score_pile = self.score_pile[0].age
        else:
            self.max_age_in_score_pile = 0
            self.min_age_in_score_pile = 0
        
        

        print()
        print(self.owning_player.get_name() + ', You now have: ' + str(self.score) + ' points!')
        print()
        
    def add_to_score_pile(self, card):
        self.owning_player.number_of_scored_cards_this_turn += 1
        self.score += card.age
        self.score_pile.append(card)
        self.update()
    
    def remove_by_index(self, index):
        assert (index in range(len(self.score_pile) , 'Trying to remove a card that doesn\'t exist in score pile.'))
        card_to_remove = self.score_pile.pop(index)
        self.score -= card_to_remove.age
        self.update()
        return card_to_remove
        
    def remove_by_name(self, name):
        card_to_remove_index = [card.name for card in self.score_pile].index(name)
        card_to_remove = self.score_pile.pop(card_to_remove_index)
        self.score -= card_to_remove.age
        self.update()
        return card_to_remove
    
    def get_filtered_score_pile(self, key):
        return [card for card in self.score_pile if key(card)]

    def pop_filtered_score_pile(self, key):
        '''Returns all cards that matches given criteria also removing them from hand'''
        cards_to_return = []
        for card in self.score_pile:
                if key(card): cards_to_return.append(card)
        for card in cards_to_return: self.remove_by_name(card.name)
        return cards_to_return
        
         
