import card
import random
import player
import deck_parser
import deck
from intput import intput

class Game:

    def __init__(self):

        # Initiallizing and shuffling the game deck.
        self.game_deck = deck.Deck()
        self.parser = deck_parser.DeckParser(self.game_deck)
        self.parser.parse()
        self.game_end = False
        for i in range(10):
            self.game_deck.shuffle(i)
            
                
        print('Only allowed 2 players at this stage')
        self.players = [player.Player(self), player.Player(self)]
        
        def melded_card(player):
            for i in range(5):
                if player.board[i].top_card != None: return player.board[i].get_top_card_reference().get_name()
        
        #sorting players play order
        self.players = [(melded_card(player), player) for player in self.players]
        self.players.sort(key = lambda pair: pair[0])
        self.players = [pair[1] for pair in self.players]
        
        print ('Player order is: ')
        for i in range(len(self.players)):
            print(self.players[i].get_name())
             
        #TODO: In GUI I will have to add 'ready' and actually determine first player using the melded card.
        self.play()                
        
    def draw(self, from_age):
        return self.game_deck.draw(from_age)

    def game_end(self):
        print('Game has ended! And the winner is:')       

    def take_turn(self, player):
        self.take_action(player)
        self.take_action(player)

    def invalid_option(self, player):
        print('Invalid choice, choose again')
        self.take_action(player)

    def take_action(self, player):
        print('{0}, Choose an action:'.format(player.get_name()))
        print()
        print('1. Draw')
        print('2. Meld')
        print('3. Dogma')
        print('4. Achieve')
        print('Does not count as an action:')
        print('5. Show hand.')
        print('6. Show the melded cards of some color.')
        print('7. Show symbol count.')        
        print()
        action = intput('')        
        print()
        
        if action == 1:
            player.draw(player.draw_age)
        elif action == 2:
            player.meld()
        elif action == 3:
            player.dogma()
        elif action == 4:
            pass
        elif action == 5:
            player.hand.print_self()
        elif action == 6:
            choice = intput('Choose color: Red - 1, Blue - 2, Yellow - 3, Purple - 4, Green -5')
            choice -= 1
            if choice not in range(5):
                self.invalid_option(player)
            else:
                player.board[choice].print_self()
        elif action == 7:
            player.print_symobls_count()
        elif action == 99:
            new_splay = input('Choose new splay mode for all your piles')        
            for i in range(5):
                player.board[i].change_splay_mode(new_splay)
        else:
            self.invalid_option(player)
            
    def play(self):
        while not self.game_end:
            for i in range(len(self.players)):
                self.take_turn(self.players[i])
    
    def return_card (self, card):
        self.game_deck.return_card(card)
    
    def dogma(initiating_player, card_refernce):
        pass
    
    def get_sharing_players(self):
        pass
        
    def get_victims(self):
        pass
        
             
            
            
        
        

        
                

