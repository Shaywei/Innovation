'''
Created on 01/10/2011

@author: lost_dm

This class recieves a file_name (El-Ad's silghtly modified FAQ) and an empty game_deck
and parses the file to create a deck using the parse() function.
'''

import re
import card
import deck

class DeckParser:

    def __init__(self, game_deck):
        
        self.file_name = 'cards.txt'
        self.game_deck = game_deck
        
        age_pattern =   '''
                            ^                                       # Beginning of line
                            Age                                     # The word 'Age'
                            \s+                                     # Atleast one space, perhaps more
                            (\d+)                                   # Atleast one digit, perhaps more. This goes to groups().
                            $                                       # End of line.
                        '''
                        
        name_pattern =   '''
                            ^                                       # Beginning of line
                            ((\w+\s+)*\w+)                          # The actual name. This goes to groups().
                            $                                       # End of line.
                        '''

        color_and_symbols_pattern = '''
                            ^                                       # Beginning of line
                            ((Yellow|Red|Green|Blue|Purple))        # The color, first in groups().
                            [^\[]*\[([^\]]*)\]                      # Top left symbol, second in groups().  This matches anything that isn't [, then finds the first [, anything that isn't ] and finally a ]
                            [^\[]*\[([^\]]*)\]                      # Top left symbol, third in groups().         
                            [^\[]*\[([^\]]*)\]                      # Top left symbol, fourth in groups().                        
                            [^\[]*\[([^\]]*)\]                      # Top left symbol, fifth in groups().                        
                            (\d+)                                   # Atleast one digit, perhaps more. This goes to goups().
                            $                                       # End of line.
                        '''
                        
        dogma_pattern = '''
                            ^                                                    # Beginning of line
                            (\[(Leaf|Crown|Castle|Clock|Factory|Lightbulb)\])    # The symbol of the dogma, first in groups().
                            \s*:\s*                                              # Some spaces perhaps and : followed by some more spaces perhaps.               
                            (.*)                                                 # The description, second in goups().
                            $                                                    # End of line.
                        '''

        
        
    def parse(self):
    
        '''Initiallizing card attributes.'''
        age = -1
        card_name = ''
        color = ''
        symbols = ()
        dogmas = []

        with open(self.file_name) as a_file:
            for a_line in a_file:
                
                # We found an Age line.
                if a_line.startswith('Age'):
                    age = int(a_line[4:])
                    
                # We found the color and symbols line.            
                elif a_line.startswith(('Yellow','Red','Purple','Green','Blue')):
                    tmp_list = a_line.split('.')            # This will return: [<color> , <interseting stuff> , <empty string>] 
                    color = tmp_list[0].strip().upper() 
                    tmp_list = tmp_list[1]                  # Only interesting in the <interesting stuff>
                    tmp_list = tmp_list.split(']',3)        # <interesting stuff> are the symbols in [symbol1], [symbol2], [symbol3], [symbol4] format.
                    symbols = ['FLAVOR' if elem.startswith(' [Hex') \
                                or elem.startswith(', [Hex') \
                                else elem.strip('[, ]').upper() for elem in tmp_list] # To makes stuff nice and generic.
                    symbols = tuple(symbols)
                
                # We found a dogma line.
                elif a_line.startswith('['):    # This means it's a Dogma. 
                    tmp_list=a_line.split(':')
                    dogma_symbol = tmp_list[0].strip('[] ').upper()
                    dogma_desc = tmp_list[1].strip()
                    dogmas.append((dogma_symbol, dogma_desc))
                
                # We found a name line.
                elif a_line[0].isupper():
                    card_name = a_line.strip()
                
                # We found an empty line and it's after a card line.
                elif a_line == '\n' and symbols != ():   # The second condition should only happen between age lines.      
                    self.game_deck.add_card_to_deck(card.Card(card_name, age, color, symbols, dogmas), age)
                    card_name = ''
                    color = ''
                    symbols = ()
                    dogmas = []
                        
                    

