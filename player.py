import game
import pile
import hand

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
        
        #TODO: score pile is a diffrent sort of pile that should be sorted by age and have a total.      
        score_pile = None
        
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
        
        # Check if there are cards to meld.
        hand_size = self.hand.get_size()
        if hand_size == 0:
            print('Your hand is empty',)
            self.thegame.invalid_option(self)
        else:
            print()
        
            # Show hand and get choice.
            self.hand.print_self()
            choice = input('Choose card number to meld:') 
            card_num_to_meld = int(choice)
            print()
            
            # Make sure choice is valid, and if so, meld.
            if hand_size < int(card_num_to_meld):
                self.thegame.invalid_option(self)
            else:
                card_to_meld = self.hand.remove_from_hand(card_num_to_meld)
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
    
    def dogma(self):
        self.update_symbol_count()

    