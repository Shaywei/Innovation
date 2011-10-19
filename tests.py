import deck_parser
import deck
import player
import pile
import hand
import score_pile
import ui
import unittest
import card
import dummy_game
import dummy_player
import dummy_ui
import random

card_names = { 'Agriculture' , 'Archery' , 'City States' , 'Clothing' , 'Code of Laws' , 'Domestication' , 'Masonry' , 'Metalworking' , 'Mysticism' , 'Oars' , 'Pottery' , 'Sailing' , 'The Wheel' , 'Tools' , 'Writing' , 'Calendar' , 'Canal Building' , 'Currency' , 'Construction' , 'Fermenting' , 'Mapmaking' , 'Mathematics' , 'Monotheism' , 'Philosophy' , 'Road Building' , 'Alchemy' , 'Education' , 'Compass' , 'Engineering' , 'Feudalism' , 'Machinery' , 'Medicine' , 'Optics' , 'Paper' , 'Translation' , 'Anatomy' , 'Colonialism' , 'Enterprise' , 'Experimentation' , 'Gunpowder' , 'Invention' , 'Navigation' , 'Perspective' , 'Printing Press' , 'Reformation' , 'Astronomy' , 'Banking' , 'Chemistry' , 'Coal' , 'Measurement' , 'Physics' , 'Societies' , 'Statistics' , 'Steam Engine' , 'The Pirate Code' , 'Atomic Theory' , 'Canning' , 'Classification' , 'Democracy' , 'Emancipation' , 'Encyclopedia' , 'Industrialization' , 'Machine Tools' , 'Metric System' , 'Vaccination' , 'Bicycle' , 'Combustion' , 'Electricity' , 'Evolution' , 'Explosives' , 'Lighting' , 'Publications' , 'Railroad' , 'Refrigeration' , 'Sanitation' , 'Antibiotics' , 'Corporations' , 'Empiricism' , 'Flight' , 'Mass Media' , 'Mobility' , 'Quantum Theory' , 'Rocketry' , 'Skyscrapers' , 'Socialism' , 'Collaboration' , 'Composites' , 'Computers' , 'Ecology' , 'Fission' , 'Genetics' , 'Satellites' , 'Services' , 'Specialization' , 'Suburbia' , 'A.I.' , 'Bioengineering' , 'Databases' , 'Globalization' , 'Miniaturization' , 'Robotics' , 'Self Service' , 'Software' , 'Stem Cells' , 'The Internet' }

def name0(): pass
test_card = card.Card('name',1,'RED', ('CROWN', 'LEAF', 'CASTLE', 'FLAVOR') , ['CROWN' , 'description' , 'mandatory', name0])

card_type = type(test_card)
function_type = type(name0)
string_type = type('bla')

valid_symbols ={'CROWN', 'LEAF', 'CASTLE', 'CLOCK', 'FACTORY', 'LIGHTBULB' , 'FLAVOR'}
valid_dogma_types = { 'demand' , 'mandatory' , 'may' }

class TestDeckParsing(unittest.TestCase):
    
    def setUp(self):
        self.game_deck = deck.Deck()
        self.parser = deck_parser.DeckParser(self.game_deck)
        self.parser.parse()

    def test_only_cards(self):
        # make sure deck contains only cards
        for i in range(len(self.game_deck.deck)):
            for j in range(len(self.game_deck.deck[i])):
                error = 'card: ' + str(j+1) + ' in age: ' + str(i+1) +' is not of type Card.'
                self.assertIsInstance(self.game_deck.deck[i][j], card_type , error)
    
    def test_valid_names(self):
        # make sure the card name is valid
        for i in range(len(self.game_deck.deck)):
            for j in range(len(self.game_deck.deck[i])):
                card_name = self.game_deck.deck[i][j].get_name()
                error = 'Not valid name in card: ' + str(j+1) + ' in age: ' +str(i+1)+'. Card name is: ' + card_name
                self.assertTrue(card_name in card_names, error)

    def test_all_names_exist(self):
        # make sure the card name is valid
        tmp_card_names = set()
        for name in card_names:
            tmp_card_names.add(name)
        for i in range(len(self.game_deck.deck)):
            for j in range(len(self.game_deck.deck[i])):
                card_name = self.game_deck.deck[i][j].get_name()
                tmp_card_names.remove(card_name)
        self.assertEqual(tmp_card_names, set() , 'Removed all cards and still name list isnt empty.')

    def test_four_symbols(self):
        # make sure all cards have exactly 4 symbols
        for i in range(len(self.game_deck.deck)):
            for j in range(len(self.game_deck.deck[i])):
                card_symbols = self.game_deck.deck[i][j].get_symbols()
                error = 'Not exactly 4 symbols in card: ' + str(j+1) + ' in age: ' +str(i+1)
                self.assertEqual(len(card_symbols), 4, error)
                
    def test_valid_symbols(self):
        # make sure all symbols of all cards are valid
        for i in range(len(self.game_deck.deck)):
            for j in range(len(self.game_deck.deck[i])):
                card_symbols = self.game_deck.deck[i][j].get_symbols()
                for symbol in card_symbols:
                    error = 'wrong symbol in card number: ' + str(j+1) + ' in age: ' +str(i+1)
                    self.assertTrue(symbol in valid_symbols, error)

    def test_one_flavor(self):
        # make sure each card has exactly one flavor symbol
        count = 0
        for i in range(len(self.game_deck.deck)):
            for j in range(len(self.game_deck.deck[i])):
                card_symbols = self.game_deck.deck[i][j].get_symbols()
                for symbol in card_symbols:
                    if symbol == 'FLAVOR': count += 1          
                error = 'Not exactly one \'FLAVOR\' symbol in card number: ' + str(j+1) + ' in age: ' +str(i+1)
                self.assertEqual(count , 1, error)
                count = 0
                
    def test_at_least_one_dogma(self):
        # make sure each card has at least one dogma
        for i in range(len(self.game_deck.deck)):
            for j in range(len(self.game_deck.deck[i])):
                card_dogmas = self.game_deck.deck[i][j].dogmas
                error = 'No dogmas for card: ' + str(j+1) + ' in age: ' +str(i+1)
                self.assertTrue(len(card_dogmas)> 0, error)

    def test_dogmas_contain_4tuples(self):
        # make sure each dogma of every card is valid
        for i in range(len(self.game_deck.deck)):
            for j in range(len(self.game_deck.deck[i])):
                card_dogmas = self.game_deck.deck[i][j].dogmas
                error = 'Not exactly a 4-tuple dogma in card number: ' + str(j+1) + ' in age: ' +str(i+1)
                for dogma in card_dogmas:   
                    self.assertEqual(len(dogma), 4, error)

    def test_valid_dogmas_symbols(self):
        # make sure each dogma of every card is valid
        for i in range(len(self.game_deck.deck)):
            for j in range(len(self.game_deck.deck[i])):
                card_dogmas = self.game_deck.deck[i][j].dogmas
                error = 'Not a valid symbol in dogmas for card: ' + str(j+1) + ' in age: ' +str(i+1)
                for dogma in card_dogmas:
                    symbol = dogma[0]
                    self.assertTrue(symbol in valid_symbols and symbol != 'FLAVOR', error)            

    def test_valid_dogmas_description(self):
        # make sure each dogma of every card is valid
        for i in range(len(self.game_deck.deck)):
            for j in range(len(self.game_deck.deck[i])):
                card_dogmas = self.game_deck.deck[i][j].dogmas
                error = 'Dogma description not a string in dogmas for card: ' + str(j+1) + ' in age: ' +str(i+1)
                for dogma in card_dogmas:
                    dogma_desc = dogma[1]
                    self.assertIsInstance(dogma_desc, string_type, error)   

    def test_valid_dogmas_types(self):
        # make sure each dogma of every card is valid
        for i in range(len(self.game_deck.deck)):
            for j in range(len(self.game_deck.deck[i])):
                card_dogmas = self.game_deck.deck[i][j].dogmas
                error = 'Not a valid dogma type in dogmas for card: ' + str(j+1) + ' in age: ' +str(i+1)
                for dogma in card_dogmas:
                    dogma_type = dogma[2]
                    self.assertTrue(dogma_type in valid_dogma_types, error)
                    
    def test_dogmas_contain_function(self):
        # make sure each dogma of every card is valid
        for i in range(len(self.game_deck.deck)):
            for j in range(len(self.game_deck.deck[i])):
                card_dogmas = self.game_deck.deck[i][j].dogmas
                error = 'Not a function type in dogmas for card: ' + str(j+1) + ' in age: ' +str(i+1)
                for dogma in card_dogmas:
                    dogma_func = dogma[3]
                    self.assertEqual(type(dogma_func), function_type, error)  
                    
class TestDogmas(unittest.TestCase):

    def setUp(self):
        self.thegame = dummy_game.Game()
        self.dummy_acting_player = self.thegame.players[0]
        self.dummy_victim = self.thegame.players[1]                  
    
    def pop_card_from_deck_by_name_and_age(self, name, age):
        age_deck = self.thegame.game_deck.deck[age - 1]
        names_list = [card.name for card in age_deck]       
        index = names_list.index(name)
        card_to_draw = self.thegame.game_deck.deck[age-1].pop(index)
        return card_to_draw

    def meld_card_from_deck_by_name_and_age(self, player, name, age):
        card_to_meld = self.pop_card_from_deck_by_name_and_age(name, age)
        player.hand.add_to_hand(card_to_meld)
        player.meld_card_from_hand_by_name(name)
    
        
    def private_setup(self, name, age):
        card_to_meld = self.pop_card_from_deck_by_name_and_age(name, age)
        color = card_to_meld.color
        self.dummy_acting_player.hand.add_to_hand(card_to_meld)
        self.dummy_acting_player.meld_card_from_hand_by_name(name)
        self.dummy_acting_player.dogma_by_color(color)
    
    
    def test_agriculture(self):
        self.private_setup('Agriculture',1)
        self.assertTrue(self.dummy_acting_player.score_pile.score == 2 , 'score is: ' + str(self.dummy_acting_player.score_pile.score) + ' rather then 2')

    def test_archery(self): 
    
        # To test Archery
        age_seven_card = self.thegame.game_deck.deck[6].pop()
        self.dummy_victim.hand.add_to_hand(age_seven_card)    
        
        self.private_setup('Archery',1)

        dummy_acting_player_max_age_in_hand = self.dummy_acting_player.hand.hand[len(self.dummy_acting_player.hand.hand) -1].age
        
        self.assertTrue(dummy_acting_player_max_age_in_hand == 7 , 'highest age is: ' + str(self.dummy_acting_player.hand.hand[len(self.dummy_acting_player.hand.hand) -1].age) + ' rather then 7')
        self.assertEqual(self.dummy_victim.hand.hand_size, 1, str(self.dummy_victim.hand.hand))
        self.assertEqual(self.dummy_victim.hand.hand[0].age, 1)
        
    def test_city_states(self):
        # To satisfy 'City States' condition.
        self.meld_card_from_deck_by_name_and_age(self.dummy_victim, 'Construction', 2)
        self.meld_card_from_deck_by_name_and_age(self.dummy_victim, 'Fermenting', 2)
        
        # To give acting player castle advantage.
        self.meld_card_from_deck_by_name_and_age(self.dummy_acting_player, 'Oars' , 1)
        self.meld_card_from_deck_by_name_and_age(self.dummy_acting_player, 'Masonry' , 1)

        self.private_setup('City States',1)

        
        top_cards_num = 0
        for i in range(5): 
            if self.dummy_victim.board[i].top_card != None: top_cards_num += 1
        self.assertEqual(top_cards_num, 1, 'No cards was removed from victim')
        self.assertEqual(self.dummy_acting_player.board[2].top_card.name == 'Fermenting' or self.dummy_acting_player.board[0].top_card.name == 'Construction' , 1, 'Card wasnt transfer to demanders board.')


    def test_clothing(self):        
        self.private_setup('Clothing',1)
        
        # To give one common color (red)
        self.meld_card_from_deck_by_name_and_age(self.dummy_acting_player, 'Oars' , 1)
        self.meld_card_from_deck_by_name_and_age(self.dummy_victim, 'Construction', 2)
        
        #TODO: Write actual test.

    def test_code_of_laws(self):
        self.private_setup('Code of Laws',1)
        
        

                    
parsing_suite = unittest.TestLoader().loadTestsFromTestCase(TestDeckParsing)
dogma_suite = unittest.TestLoader().loadTestsFromTestCase(TestDogmas)
all_suit = unittest.TestSuite()
all_suit.addTest(parsing_suite)
all_suit.addTest(dogma_suite)
unittest.TextTestRunner(verbosity=2).run(all_suit)
