import dummy_game
import pile
import hand
import score_pile
import dummy_ui
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
        self.turn_order_place = 0       
        self.score_pile = score_pile.ScorePile(self)
        
        #TODO: score pile is a diffrent sort of pile that should be sorted by age and have a total.      
        
    def get_name(self):
        return self.name

    # For testing purpuses.
    def check_if_melded(self, name):
        for cards in self.board:
            for card in cards.pile:
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
        top_cards_ages = [1]    # 1 is default.
        for i in range(5):
            top_card = self.board[i].top_card
            if top_card is not None: top_cards_ages.append(top_card.age)
        new_draw_age = max(age for age in top_cards_ages)
    # NOT SURE ABOUT THIS ^ MAKE SURE SOMEHOW LATER.    
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
    
    def meld_card(self, card_to_meld):
        if card_to_meld.age > self.draw_age: self.draw_age = card_to_meld.age  # If we meld a card of age higher then draw age should be updated.
        elif card_to_meld.age < self.draw_age: self.update_draw_age()          # If we meld a card of age lower then draw age might need to be updated.    
        pile_color = colors_dict[card_to_meld.get_color()]
        self.board[pile_color].meld(card_to_meld)
        self.update_symbol_count()
        
    def meld_card_from_hand_by_name(self, name):   
        print(name)
        names_list = [card.name for card in self.hand.hand]       
        index = names_list.index(name)
        card_to_meld = self.hand.remove_by_index(index)
        self.meld_card(card_to_meld)
                
    def choose_card_from_list(self, list):
        chosen_card_index = self.ui.choose_card_from_list(list) - 1
        removed_card_reference = list[chosen_card_index]
        return removed_card_reference
        
    def choose_color_from_list(self, list):  #returns a string of said color
        return  self.ui.choose_color_from_list(list)
                
    def choose_player_from_list(self, key = lambda player: True):  #returns a player from the list.
        '''Args - key that checks condition on players
           Return:
           If more then one player answer conditions - choose.
           If exactly one - return it
           If no player - return None'''
        list = [player for player in self.thegame.players if key(player)]
        if len(list) > 1: return self.ui.choose_player(list)
        elif len(list) == 1 : return list[0]
        else: return None
                    
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
     
    def draw_to_hand(self, draw_age):
        self.add_card_to_hand(self.draw_card(draw_age))
       
    def get_top_card_reference(self, pile_number):
        self.board[pile_number].get_top_card_reference()
    
    def dogma(self):
        choice = self.ui.player_choose_top_card(self)
        card_to_execute = self.board[choice].get_top_card_reference()
        print('You chose to execute: '+card_to_execute.name )
        self.thegame.dogma(self, card_to_execute.get_dogmas())
        
    def dogma_by_color(self,color):
        card_to_execute = self.board[colors_dict[color.upper()]].get_top_card_reference()
        print('You chose to execute: '+card_to_execute.name )
        self.thegame.dogma(self, card_to_execute.get_dogmas())
    
    def get_top_card_reference_from_pile(self, pile):
        return self.board[pile].get_top_card_reference()
            
    def get_symbol_count(self):
        return self.symbol_count
    
    def execute_dogma(card_reference):
        pass

    def return_card(self, card_to_return):
        self.thegame.return_card(card_to_return)
        
    def tuck_card(self, card_to_tuck):
        color = card_to_tuck.color
        self.board[colors_dict[color]].tuck(card_to_tuck)
        
        


    