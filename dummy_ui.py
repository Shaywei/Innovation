'''
Created on 18/10/2011

@author: lost_dm

This class implements a UI for the game.
'''
import dummy_player
import os


    
class UI:
    def __init__(self, thegame):
        self.thegame = thegame
        self.players = []
        '''self.root = Tk()
        self.root.title("Innovation")
        '''
        
        # TODO: Use this
        self.may_array = []
        self.choice_array = []
        self.choices_length_array = []
        
    # TODO: Use this
    def set_arrays(self, may_array, choice_array, choices_length_array):
        self.may_array = may_array
        self.choice_array = choice_array
        self.choices_length_array = choices_length_array
    
    def make_choice(self):
        expected_num_of_choices = self.choices_length_array.pop(0)
        actual_num_of_choices = len(valid_options)
        assert actual_num_of_choices == expected_num_of_choices, 'Error with number of options for msg: ' + msg + '. Expected: ' + str(expected_num_of_choices) + ' actual: ' + str(actual_num_of_choices)
        choice = self.choice_array.pop(0)
        return choice
  
    def make_valid_choices_from_int(self, j):
        '''Gets integer j and returns a set {1, 2, 3, ... , j}'''
        valid_choices = set()
        for i in range(j): valid_choices.add(i+1)
        return valid_choices
        
    def reveal(self, card_to_reveal):
        print('Revealing:')
        card_to_reveal.print_self()
    
    def prompt(self, msg, valid_options):
        # TODO: Use this.    
        '''choice = self.make_choice
        return choice'''
        return 1
        
    def str_prompt(self, msg, valid_options):
        # TODO: Use this.    
        '''choice = self.make_choice
        return str(choice)'''
        return '1'

    def choose_number_of_players(self):
        '''frame = Frame(self.root)
        frame.pack()
        
        for i in range(4):
            self.button = Button(frame, text="{0} player".format(str(i+1)), command=self.make_assign_number_of_players(i+1))
            self.button.pack(side=LEFT)'''
            
        #number_of_players = prompt('Choose number of players (1-4): ', {1,2,3,4})      
        number_of_players = 3 # acting, victim and sharer
        
        return number_of_players
               
    def assign_players(self, players):
        self.players = players
    
    
    def get_player_name(self):
        name = 'DUMMY'
        #while name == '':
        #    name = input('Enter Player\'s name (must be non-empty):')
        return name 
              
    def may(self, action_desc):
        ''' assert len(self.may_array) > 0 , 'Making a \'may\' decision when no may answer avilable. action_desc: ' + action_desc
        choice = self.may_array.pop(0)
        return choice'''
        return True

    def player_choose_top_card(self, player):
        # TODO: Use this.
        for i in range(5): 
            top_card = player.get_top_card_reference_from_pile(i)
            if top_card is not None: return i
    
    def choose_card_from_hand(self, hand_size):
        return 0
        
    def choose_card_from_list(self, list):
        ''' This method prints the hand. '''
        assert len(list)>0 , 'list is empty'    
        #return list[0]
        return 0
        
    def choose_color_from_list(self, list):
        if list == []: return None
        return list[0]      
        
    def choose_player(self, list_of_players):
        ''' This method recieves a list of players, takes a choice from current player and return a reference to the player chosen. A post condition is that list of players is not empty!'''
        return list_of_players[0]
        
    def print_card_list(self, list):
        ''' This method prints a card list. '''
        assert len(list)>0 , 'list is empty'
        
    '''def make_assign_number_of_players(self, num):
        def assign_number_of_players():
            print('Players {0}'.format(str(num)))
            self.number_of_players = num
        return assign_number_of_players'''

        

