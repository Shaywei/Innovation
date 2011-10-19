'''
Created on 01/10/2011

@author: lost_dm
'''

class Card:
    ''' This is a game card object.
        It has the following attributes:
                                            name - The card's name
                                            color - In ('RED', 'PURPLE', 'YELLOW', 'GREEN', 'BLUE').
                                            age - In range(1,10)
                                            symbols - A list of length 4. Index 0 is top left symbol .. index 3 is right symbol. 
                                                      Each entry is on of ('CROWN', 'LEAF', 'CASTLE', 'CLOCK', 'FACTORY', 'LIGHTBULB' and 'FLAVOR').
                                            dogmas - A list of Dogmas. Each dogma is pair of (<symbol>, <desc>).
        It has the following methods:
                                            activate() - Activates one dogma at a time.
        '''
    def __init__(self, name, age, color, symbols, dogmas):
        self.name = name
        self.age = age
        self.color = color
        self.symbols = symbols
        self.dogmas = dogmas
#        import name.lower() from dogmas
#        self.dogma_function = name.lower().replace(' ', '_')

    def print_self(self):
        print(self.name + ' (' + str(self.age) + ', '+ self.color +')')
        print('Symbols: ' + str(self.symbols))
        for dogma in self.dogmas:
            print(dogma[0] + ': ' + dogma[1] + ' ' + str(dogma[2]))
        print()
        
    def get_color(self):
        return self.color
    
    def get_age(self):
        return self.age
        
    def get_symbols(self):
       return self.symbols      
        
    def get_name(self):
        return self.name

    
    def dogma(self):
        pass
        
                                            