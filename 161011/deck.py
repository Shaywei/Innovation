'''
Created on 09/10/2011

@author: lost_dm

This class represents the draw decks (ages 1-10).
'''


import card
import deck_parser
import random

class Deck:
    def __init__(self):
        self.deck = [[],[],[],[],[],[],[],[],[],[]] # Index i (i in [0..9]) represents the deck of age i+1.
        
    def draw(self, from_age):
        from_age -= 1    # Because ages are 1-10 and indices are 0-9.
        while 1:
            if from_age > 9:
                game_end()
            elif len(self.deck[from_age]) == 0:
                from_age += 1
            else:
                return self.deck[from_age].pop()

    def return_card(self, card):
        self.deck[card.get_age() - 1].insert(0, card)

    def shuffle(self, age_deck_to_shuffle):
        random.shuffle(self.deck[age_deck_to_shuffle])

    def add_card_to_deck(self, card, age_to_add_to):
        age_to_add_to -= 1    # Because ages are 1-10 and indices are 0-9.
        self.deck[age_to_add_to].append(card)

    
    


