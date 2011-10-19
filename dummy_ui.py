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

    def choose_number_of_players(self):
        '''frame = Frame(self.root)
        frame.pack()
        
        for i in range(4):
            self.button = Button(frame, text="{0} player".format(str(i+1)), command=self.make_assign_number_of_players(i+1))
            self.button.pack(side=LEFT)'''
            
        #number_of_players = prompt('Choose number of players (1-4): ', {1,2,3,4})      
        number_of_players = 2 #dummy and victim
        
        return number_of_players
               
    def assign_players(self, players):
        self.players = players
    
    
    def get_player_name(self):
        name = 'DUMMY'
        #while name == '':
        #    name = input('Enter Player\'s name (must be non-empty):')
        return name 
       
    def get_red_color(self):
        color = 0
        return color
    def get_blue_color(self):
        color = 1
        return color
    def get_yellow_color(self):
        color = 2
        return color        
    def get_purple_color(self):
        color =3
        return color        
    def get_gree_color(self):
        color = 4
        return color        
       
    def may(self, action_desc):
            return True

    def player_choose_top_card(self, player):
        for i in range(5): 
            top_card = player.get_top_card_reference_from_pile(i)
            if top_card is not None: return i
    
    def choose_card_from_hand(self, hand_size):
        return 1
        
    def choose_card_from_list(self, list):
        ''' This method prints the hand. '''
        assert len(list)>0 , 'list is empty'    
        return list[0]

        
    '''def make_assign_number_of_players(self, num):
        def assign_number_of_players():
            print('Players {0}'.format(str(num)))
            self.number_of_players = num
        return assign_number_of_players'''

        

