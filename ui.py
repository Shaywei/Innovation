'''
Created on 18/10/2011

@author: lost_dm

This class implements a UI for the game.
'''
import player
from intput import intput
import os

    
class UI:
    def __init__(self, thegame):
        self.thegame = thegame
        self.players = []
        
        '''self.root = Tk()
        self.root.title("Innovation")
        '''
        
    def make_valid_choices_from_int(self, j):
        '''Gets integer j and returns a set {1, 2, 3, ... , j}'''
        valid_choices = set()
        for i in range(j): valid_choices.add(i+1)
        return valid_choices

    def prompt(self, msg, valid_options):
        choice = None
        while choice not in valid_options:
            choice = intput(msg)
        return choice
        
    def str_prompt(self, msg, valid_options):
        choice = None
        while choice not in valid_options:
            choice = input(msg)
        return choice

    def choose_number_of_players(self):
        '''frame = Frame(self.root)
        frame.pack()
        
        for i in range(4):
            self.button = Button(frame, text="{0} player".format(str(i+1)), command=self.make_assign_number_of_players(i+1))
            self.button.pack(side=LEFT)'''
        number_of_players = self.prompt('Choose number of players (1-4): ', {1,2,3,4})      
        return number_of_players
               
    def assign_players(self, players):
        self.players = players
        
    def reveal(self, card_to_reveal):
        print('Revealing:')
        card_to_reveal.print_self()
        
    def get_player_name(self):
        name = ''
        while name == '':
            name = input('Enter Player\'s name (must be non-empty):')
        return name
        
    def get_player_action(self, player_name):
        print('{0}, points Choose an action:'.format(player_name))
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
        action = self.prompt('Choose an action (1-7): ', {1,2,3,4,5,6,7,99})
        print()
        os.system("cls")
        return action
    
    def get_color(self):
        color = self.prompt('Choose color: Red - 0, Blue - 1, Yellow - 2, Purple - 3, Green - 4' , {1,2,3,4,0})
        return color
       
    def may(self, action_desc):
        choice = self.str_prompt('You may choose to execute:\n' + action_desc +'\n Execute? (y/n)' , {'y','n'})
        if choice == 'y':
            return True
        elif choice == 'n':
            return False

    def player_choose_top_card(self, player):
        #TODO: What if all piles are empty?
        print('Your top cards:')
        j = 0
        tmp_dict = {}
        for i in range(5): 
            top_card = player.get_top_card_reference_from_pile(i)
            if top_card is not None:
                j += 1
                tmp_dict[j] = i
                print('choice {0}:'.format(str(j)))
                top_card.print_self()
                print()
        valid_choices = self.make_valid_choices_from_int(j)
        choice = self.prompt('Choose top card from valid choices: ' , valid_choices)
        return tmp_dict[choice]
    
    def choose_card_from_hand(self, hand_size):
        valid_choices = self.make_valid_choices_from_int(hand_size)
        card_index_choice = self.prompt('Choose a card from your hand (one of the above): ', valid_choices) - 1
        return card_index_choice
    
    def print_card_list(self, list):
        ''' This method prints a card list. '''
        assert len(list)>0 , 'list is empty'
        for i in range(len(list)):
            print('{0}. '.format(i+1),)
            list[i].print_self()
            print()
        print()
                
    def choose_card_from_list(self, list):
        self.print_card_list(list)
        valid_choices = self.make_valid_choices_from_int(len(list))    
        card_index_choice = self.prompt('Choose a card (one of the above): ', valid_choices)
        return list[card_index_choice - 1]

    def choose_color_from_list(self, list):
        #TODO: TEST and GUI
        if list == []: return None
        for i in range(len(list)):
            print('{0}. {1}'.format(i+1, list[i]),)
        valid_choices = self.make_valid_choices_from_int(len(list))
        valid_choices.add(0)
        choice = self.prompt('Choose a color (one of the above) or 0 for None: ', valid_choices)
        if choice == 0: return None
        return list[choice - 1]
    
    def choose_player(self, list_of_players):
        ''' This method recieves a list of players, takes a choice from current player and return a reference to the player chosen. A post condition is that list of players is not empty!'''
        for i in range(len(list)):
            print('{0}. {1}'.format(i+1, list[i].name),)
        valid_choices = self.make_valid_choices_from_int(len(list))
        choice = self.prompt('Choose a color (one of the above): ', valid_choices)
        return list_of_players[choice - 1]
        
        
        
        
    '''def make_assign_number_of_players(self, num):
        def assign_number_of_players():
            print('Players {0}'.format(str(num)))
            self.number_of_players = num
        return assign_number_of_players'''

        

