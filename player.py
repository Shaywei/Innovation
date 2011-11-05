import game
import pile
import hand
import score_pile
import ui
from intput import intput

colors_dict = {'RED' : 0, 'BLUE' : 1, 'YELLOW' : 2, 'PURPLE' : 3 , 'GREEN' : 4}

class Player:
    '''This is the class that represent a player in the game'''
    
    def __init__(self, thegame, ui):
        
        self.achievements = set()
        self.achievements_number = 0
        
        self.number_of_tucked_cards_this_turn = 0
        self.number_of_scored_cards_this_turn = 0
        
        self.thegame = thegame
        self.ui = ui
        self.name = self.ui.get_player_name()
        self.draw_age = 1
        self.board = [pile.Pile(self, 'RED'),pile.Pile(self, 'BLUE'), \
                      pile.Pile(self, 'YELLOW'),pile.Pile(self, 'PURPLE'),pile.Pile(self, 'GREEN')]
        self.symbol_count = [0,0,0,0,0,0] # By index: 0 -> CROWN, 1 -> LEAF, 2 -> LIGHTBULB \
                                          #           3 -> CASTLE, 4 -> FACTORY, 5 -> CLOCK
        
        # Initialize hand and draw two age 1 cards.
        self.hand = hand.Hand(self)
        self.draw_action()
        self.draw_action()
        self.turn_order_place = None
        
        self.score_pile = score_pile.ScorePile(self)
        
        #TODO: score pile is a diffrent sort of pile that should be sorted by age and have a total.      
        
        self.meld_action()
        
    def get_name(self):
        return self.name
    
    # For testing purpuses.
    def check_if_melded(self, name):
        for pile in self.board:
            for card in pile:
                if card.name == name: return True
        return False
    
    #TODO: something more serious 
    def check_for_victory(self):
        if self.achievements_number > 5: print('VICTORY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        
    def reset_scored_tucked_num(self):
        self.number_of_tucked_cards_this_turn = 0
        self.number_of_scored_cards_this_turn = 0
        
    def set_turn_order_place(self, place):
        self.turn_order_place = place
        
    def print_symobls_count(self):
        print ('Your Current Symbol Count: ')
        print('Crowns - {0}, Leaves - {1}, Lightbulbs - {2}, Castles - {3}, Factories - {4}, Clocks - {5}'.format(self.symbol_count[0],self.symbol_count[1],self.symbol_count[2],self.symbol_count[3],self.symbol_count[4],self.symbol_count[5]))
        print()
                   
    def update_symbol_count(self):
        self.symbol_count = [0,0,0,0,0,0]
        for i in range (5):
            for j in range (6):
                self.symbol_count[j] += self.board[i].get_symbol_count()[j]
                
    def score_card_from_hand(self):
        '''This method chooses a card from hand and put it in score pile'''
        if self.hand.hand_size != 0:
            card_to_score = self.choose_card_from_hand()
            self.score_pile.add_to_score_pile(card_to_score)
        
    def score_card_by_age(self, age):
        '''This method draws a card according to age and put it in score pile'''
        card_to_score = self.draw_card(age)
        self.score_pile.add_to_score_pile(card_to_score)

    def score_card_by_card(self, card_to_score):
        '''This method recives a card and put it in score pile'''
        self.score_pile.add_to_score_pile(card_to_score)
        
    def update_draw_age(self):
        pass
        new_draw_age = 1 # Default
        top_cards = []
        for i in range(5):
            top_card = self.board[i].top_card
            if top_card is not None: top_cards.append(top_card)
        new_draw_age = max(top_card, lambda card: card.age)
        
    def meld_action(self):
        '''This method shows hand, gets choice of card to meld and melds it'''
        if self.hand.hand_size != 0:
            card_to_meld = self.choose_card_from_hand()
            self.meld_card(card_to_meld)
    
    def choose_card_from_hand(self):
        '''This method shows the player his hand and pops a card of his choice, then return popped card.'''
        if self.hand.hand_size == 0: return None
        self.hand.print_self()
        choice = self.ui.choose_card_from_hand(self.hand.get_size())
        chosen_card = self.hand.remove_by_index(choice)
        return chosen_card
    
    def choose_card_from_list(self, list):  #RETURNS A REFERENCE ONLY!!!
        return self.ui.choose_card_from_list(list)
#        removed_card_reference = list[chosen_card_index]
#        return removed_card_reference
        
    def choose_color_from_list(self, list):  #returns a string of said color
        return  self.ui.choose_color_from_list(list)
        
    def choose_player_from_list(self, list):  #returns a player from the list.
        return  self.ui.choose_player(list)
            
    def meld_card(self, card_to_meld):
        if card_to_meld.age > self.draw_age: self.draw_age = card_to_meld.age  # If we meld a card of age higher then draw age should be updated.
        elif card_to_meld.age < self.draw_age: self.update_draw_age()          # If we meld a card of age lower then draw age might need to be updated.
        pile_color = colors_dict[card_to_meld.get_color()]
        self.board[pile_color].meld(card_to_meld)
        self.update_symbol_count()
                  
    def draw_action(self):
        '''This methood draws from where from is draw_age or age_i 'i' in [1-10]'''
        drawn_card = self.draw_card(self.draw_age)
        self.hand.add_to_hand(drawn_card)
        
    def add_card_to_hand(self, card_to_add):
        '''This methood recieves a card and adds it to the hand'''
        self.hand.add_to_hand(card_to_add)
    
    def draw_card(self, draw_age):
        '''This methood draws from where from is draw_age or age_i 'i' in [1-10]'''
        drawn_card = self.thegame.draw(draw_age)
        print('{0}, you drew: {1}'.format(self.name, drawn_card.name))
        return drawn_card
    
    def draw_card_to_hand_by_age(self, draw_age):
        self.add_card_to_hand(self.draw_card(draw_age))
            
    def dogma(self):
        choice = self.ui.player_choose_top_card(self)
        card_to_execute = self.board[choice].get_top_card_reference()
        print('You chose to execute: ')
        self.thegame.dogma(self, card_to_execute.get_dogmas())
    
    def get_top_card_reference_from_pile(self, pile):
        return self.board[pile].get_top_card_reference()
        
    def get_symbol_count(self):
        return self.symbol_count
    
    def return_card(self, card_to_return):
        self.thegame.return_card(card_to_return)
        
    def tuck_card(self, card_to_tuck):
        color = card_to_tuck.color
        self.board[colors_dict[color]].tuck(card_to_tuck)
        


    