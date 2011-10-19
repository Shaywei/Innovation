import game
import pile
import hand
import score_pile
from intput import intput

colors_dict = {'RED' : 0, 'BLUE' : 1, 'YELLOW' : 2, 'PURPLE' : 3 , 'GREEN' : 4}

class Player:
    '''This is the class that represent a player in the game'''
    
    def __init__(self, thegame):
        
        self.thegame = thegame
        self.name = input('Enter Player\'s Name:')
        self.draw_age = 1
        self.board = [pile.Pile(self, 'RED'),pile.Pile(self, 'BLUE'), \
                      pile.Pile(self, 'YELLOW'),pile.Pile(self, 'PURPLE'),pile.Pile(self, 'GREEN')]
        self.symbol_count = [0,0,0,0,0,0] # By index: 0 -> CROWN, 1 -> LEAF, 2 -> LIGHTBULB \
                                          #           3 -> CASTLE, 4 -> FACTORY, 5 -> CLOCK
        
        # Initialize hand and draw two age 1 cards.
        self.hand = hand.Hand(self)
        self.draw(1)
        self.draw(1)
        
        self.score_pile = score_pile.ScorePile(self)
        
        #TODO: score pile is a diffrent sort of pile that should be sorted by age and have a total.      
        
        self.meld()
    def get_name(self):
        return self.name
        
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
        pass
        
    def check_draw_age(self):
        pass
        #TODO: Draw age can only change using a MELD action or when losing cards. Think this through.     
        
    def meld(self):
        '''This method shows hand, gets choice of card to meld and melds it'''
        card_to_meld = self.hand.choose_card()
        if card_to_meld == "invalid":
            self.thegame.invalid_option(self)
        else:
            pile_color = colors_dict[card_to_meld.get_color()]
            self.board[pile_color].meld(card_to_meld)
            self.update_symbol_count()
        
    def transfer(self, player, source, to, constraint):
        '''This method transfer a card to player names 'player' from 'from' to 'to' where 'from' and 'to' are in: hand/board/score'''
        pass
    
    def draw(self, draw_age):
        '''This methood draws from where from is draw_age or age_i 'i' in [1-10]'''
        drawn_card = self.thegame.draw(self.draw_age)
        print('{0}, you drew:'.format(self.name))
        drawn_card.print_self()
        self.hand.add_to_hand(drawn_card)
        
    def choose_top_card(self):
        #TODO: What if all piles are empty?
        print('Choose one of your top cards:')
        for i in range(5): 
            print( str(i+1) +'.'),
            self.board[i].print_top_card()
        choice = intput ('\n')
        return self.get_top_card_reference(choice)
    
    def get_top_card_reference(self, pile_number):
        self.board[pile_number].get_top_card_reference()
 
def may():
    choice = input('You may choose to execute or not. Execute? (y/n)')
    if choice == 'y':
        return True
    elif choice == 'n':
        return False
    else:
        print('Incorrect choice, choose again (only \'y\' or \'n\' allowed).')
        self.may()
   
    def dogma(self):
        card_to_execute = self.choose_top_card()
        self.thegame.dogma(self, card_to_execute)
    
    def execute_dogma(card_reference):
        pass
        
        
        


    