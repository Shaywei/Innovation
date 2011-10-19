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
                
    def score_card(self, card):
        '''This method moves the card to the score pile'''
        self.score_pile.add_to_score_pile(card)
        
    def check_draw_age(self):
        pass
        #TODO: Draw age can only change using a MELD action or when losing cards. Think this through.     
        
    def meld_action(self):
        '''This method shows hand, gets choice of card to meld and melds it'''
        card_to_meld = self.choose_card_from_hand()
        self.meld_card(card_to_meld)
    
    def choose_card_from_hand(self):
        '''This method shows the player his hand and pops a card of his choice, then return popped card.'''
        self.hand.print_self()
        choice = self.ui.choose_card_from_hand(self.hand.get_size())
        chosen_card = self.hand.hand.pop(choice - 1)
        return chosen_card
    
    def meld_card(self, card_to_meld):
        pile_color = colors_dict[card_to_meld.get_color()]
        self.board[pile_color].meld(card_to_meld)
        self.update_symbol_count()
        
    def meld_card_from_hand_by_name(self, name):
        card_to_meld = self.hand.get_filtered_hand(lambda card: card.name==name)[0]
        pile_color = colors_dict[card_to_meld.color]
        self.board[pile_color].meld(card_to_meld)
        self.update_symbol_count()
        
    def choose_card_from_list(self, list):
        chosen_card = self.ui.choose_card_from_list(list)
        removed_card = self.hand.remove_from_hand_by_name(chosen_card.name)
        return removed_card              
        
    def transfer(self, player, source, to, constraint):
        '''This method transfer a card to player names 'player' from 'from' to 'to' where 'from' and 'to' are in: hand/board/score'''
        pass
    
    def draw_action(self):
        '''This methood draws from where from is draw_age or age_i 'i' in [1-10]'''
        drawn_card = self.draw_card(self.draw_age)
        self.hand.add_to_hand(drawn_card)
    
    def draw_card(self, draw_age):
        '''This methood draws from where from is draw_age or age_i 'i' in [1-10]'''
        drawn_card = self.thegame.draw(draw_age)
        print('{0}, you drew:'.format(self.name))
        drawn_card.print_self()
        return drawn_card
        
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

        
        


    