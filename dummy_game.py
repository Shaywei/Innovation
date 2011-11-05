import card
import random
import dummy_player
import deck_parser
import deck
from intput import intput
import dummy_ui

symbols_dict = {'CROWN' : 0, 'LEAF' : 1, 'LIGHTBULB' : 2, 'CASTLE' : 3 , 'FACTORY' : 4 , 'CLOCK' : 5}

class Game:

    def __init__(self):
        
        self.available_special_achievements = { 'Monument', 'World', 'Empire', 'Wonder', 'Universe'}
        
        # Initiallizing and shuffling the game deck.
        self.game_deck = deck.Deck()
        self.parser = deck_parser.DeckParser(self.game_deck)
        self.parser.parse()
        self.game_end = False
        
        # These two variables help us deal with dogmas.
        self.dogma_data = None
        self.is_sharer = True
        self.something_happened = False
        
        for i in range(10):
            self.game_deck.deck[i].reverse()
            
        self.ui = dummy_ui.UI(self)
        self.number_of_players = self.ui.choose_number_of_players()
        
        
        self.players = []
        for i in range(self.number_of_players):
            self.players.append(dummy_player.Player(self, self.ui))
        
        self.players[1].name = 'VICTIM'
        #Not needed for dummy:
        '''def melded_card(player):
            for i in range(5):
                if player.board[i].top_card != None: return player.board[i].get_top_card_reference().get_name()
        
        #sorting players play order
        self.players = [(melded_card(player), player) for player in self.players]
        self.players.sort(key = lambda pair: pair[0])
        self.players = [pair[1] for pair in self.players]
        
        print ('Player order is: ')
        for i in range(len(self.players)):
            self.players[i].set_turn_order_place(i)
            print(self.players[i].get_name())'''

        # This dict will help me refer to the player list as circular when computing sharers/victims.
        self.circular_list_dict = {}
        for i in range(len(self.players)):
            self.circular_list_dict[i] = i
            self.circular_list_dict[i + self.number_of_players] = i
            
        #TODO: In GUI I will have to add 'ready' and actually determine first player using the melded card.
        
        #self.play()                
        
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
        action = self.ui.get_player_action(player.get_name())
        if action == 1:
            player.draw_action()
        elif action == 2:
            player.meld_action()
        elif action == 3:
            player.dogma()
        elif action == 4:
            pass
        elif action == 5:
            player.hand.print_self()
        elif action == 6:
            choice = self.ui.get_color()
            player.board[choice].print_self()
        elif action == 7:
            player.print_symobls_count()
        elif action == 99:
            new_splay = input('Choose new splay mode for all your piles')        
            for i in range(5):
                player.board[i].change_splay_mode(new_splay)
                
    def reveal(self, age):
        card_to_reveal = self.draw(age)
        self.ui.reveal(card_to_reveal)
        return card_to_reveal   
        
    def play(self):
        while not self.game_end:
            for i in range(len(self.players)):
                self.take_turn(self.players[i])
    
    def return_card (self, card):
        self.game_deck.return_card(card)
       
    def get_sharing_players(self):
        pass
        
    def get_victims(self):
        pass
        
    def dogma(self, initiating_player, card_dogma):
        self.dogma_data = None
        symbol_count_snapshot = [player.get_symbol_count() for player in self.players]
        initiating_player_index = initiating_player.turn_order_place
        
        #Todo: add support for multiple symbols actions.
        symbol = card_dogma[0][0]
        symbol_index = symbols_dict[symbol]

        symbol_count_of_initiating_player = initiating_player.get_symbol_count()[symbol_index]

        victims = []
        victims_names = []
        sharers = []
        sharers_names = []
        for i in range(initiating_player_index + 1, initiating_player_index + self.number_of_players):
            real_i = self.circular_list_dict[i]
            symbol_count_of_player = symbol_count_snapshot[real_i][symbol_index]
            if symbol_count_of_player < symbol_count_of_initiating_player:
                victims.append(self.players[real_i])
                victims_names.append(self.players[real_i].get_name())
            else:
                sharers.append(self.players[real_i])
                sharers_names.append(self.players[real_i].get_name())
        
        
        print()
        print('Victims are: ' + str(victims_names))
        print()
        print('Sharers are: ' + str(sharers_names))                
        print()

        
        for action in card_dogma:
        
            action_desc = action[1]
            action_type = action[2]
            action_func = action[3]
            

            
            if action_type == 'demand':
                for player in victims:
                    action_func(player, initiating_player)
            else:
                self.is_sharer = True
                for player in sharers:
                    action_func(player)
                self.is_sharer = False
                action_func(initiating_player)
        if self.something_happened: initiating_player.draw_action()
        self.something_happened = False     # Reset this variable after dogma phase is finished                    
                
            
            
            
            
            

'''            
def draw_and_x_from_age(x, age):
	def doit(theplayer):
		x(theplayer, theplayer.draw(age))
	return doit
	
effect= draw_and_x_from_age(player.Player.meld, 1)'''

            
        
        
        

    
        
             
            
            
        
        

        
                

