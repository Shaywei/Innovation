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

colors_dict = {'RED' : 0, 'BLUE' : 1, 'YELLOW' : 2, 'PURPLE' : 3 , 'GREEN' : 4}

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
        self.dummy_acting_player.name = 'Acting Player'
        self.dummy_victim = self.thegame.players[1]
        self.dummy_victim.turn_order_place = 1
        self.dummy_victim.name = 'Victim'
        self.dummy_sharer = self.thegame.players[2]
        self.dummy_sharer.turn_order_place = 2
        self.dummy_sharer.name = 'Sharer'        

    # These methods are to help set up each of the tests 
        
    def pop_card_from_deck_by_name_and_age(self, name, age):
        age_deck = self.thegame.game_deck.deck[age - 1]
        names_list = [card.name for card in age_deck]       
        index = names_list.index(name)
        card_to_draw = self.thegame.game_deck.deck[age-1].pop(index)
        return card_to_draw

    def get_card_from_deck_by_name_and_age(self, name, age):
        age_deck = self.thegame.game_deck.deck[age - 1]
        names_list = [card.name for card in age_deck]       
        index = names_list.index(name)
        card = self.thegame.game_deck.deck[age-1].pop(index)
        return card
        
    def draw_from_deck_by_name_and_age(self, player, name, age):
        card_to_draw = self.get_card_from_deck_by_name_and_age(name, age)
        player.hand.add_to_hand(card_to_draw)

    def draw_cards_by_list(self, player, list_of_pairs):
        ''' draws the cards in list of pairs: (card_name , age_of_card) to players hand'''
        for card_name , age_of_card in list_of_pairs: self.draw_from_deck_by_name_and_age(player, card_name , age_of_card)
        
    def score_cards_by_list(self, player, list_of_pairs):
        '''Draws cards from the game deck by list of pairs: (card_name , age_of_card) and adds them to players score pile'''
        for card_name , age_of_card in list_of_pairs:
            card = self.get_card_from_deck_by_name_and_age(card_name, age_of_card)
            player.score_card_by_card(card)
        
    def meld_card_from_deck_by_name_and_age(self, player, name, age):
        card_to_meld = self.pop_card_from_deck_by_name_and_age(name, age)
        player.hand.add_to_hand(card_to_meld)
        player.meld_card_from_hand_by_name(name)    

    def meld_cards_by_list(self, player, list_of_pairs):
        ''' Melds the cards in list of pairs (card_name , age_of_card) to players board'''
        for card_name , age_of_card in list_of_pairs: self.meld_card_from_deck_by_name_and_age(player, card_name , age_of_card)
        
    def private_setup(self, name, age):
        card_to_meld = self.pop_card_from_deck_by_name_and_age(name, age)
        color = card_to_meld.color
        self.dummy_acting_player.hand.add_to_hand(card_to_meld)
        self.dummy_acting_player.meld_card_from_hand_by_name(name)
        self.dummy_acting_player.dogma_by_color(color)
      
    # Home made Asserts to make things neat and tidy.
    
    def assert_hand_size(self, player, size):
        self.assertEqual(player.hand.hand_size, size, player.name+ '\'s hand is not of size ' + str(size) + ' but rather ' + str(player.hand.hand_size))
        
    def assert_hand_contains(self, player, list_of_cards_to_check):
        answer = True
        names_of_cards_in_players_hand = [card.name for card in player.hand.hand]
        for name in list_of_cards_to_check: 
            self.assertTrue(name in names_of_cards_in_players_hand,  player.name+ '\'s hand doesnt contain: ' + name + ' but contains: ' + str([names_of_cards_in_players_hand]))

    def assert_hand_not_contains(self, player, list_of_cards_to_check):
        answer = True
        names_of_cards_in_players_hand = [card.name for card in player.hand.hand]
        problematic_name = ''
        for name in list_of_cards_to_check: 
            if name in names_of_cards_in_players_hand: 
                answer = False
                problematic_name = name
        self.assertTrue(answer, problematic_name + ' is in the hand of: ' + player.name)   
            
    def assert_player_has_achievement(self, player, achievement_name):
        self.assertTrue(achievement_name not in self.thegame.available_special_achievements , achievement_name + ' is still available.')
        self.assertTrue(achievement_name in player.achievements , achievement_name + ' is not claimed by '+player.name)
    
    def assert_score_pile_contains(self, player, list_of_cards_to_check):
        answer = True
        names_of_cards_in_players_score_pile = [card.name for card in player.score_pile.score_pile]
        for name in list_of_cards_to_check: 
            self.assertTrue(name in names_of_cards_in_players_score_pile,  player.name+ '\'s hand doesnt contain: ' + name + ' but contains: ' + str([names_of_cards_in_players_score_pile]))
        
    def assert_melded(self, player, list_of_card_names):
        answer = True
        problematic_name = ''
        for name in list_of_card_names: 
            if not player.check_if_melded(name): 
                answer = False
                problematic_name = name
        self.assertTrue(answer, problematic_name + ' is not melded for ' + player.name)
        
    def assert_melded_numbers(self, player, pairs):
        for age,expected_number in pairs: 
            actual_number = player.number_melded_by_age(age)
            self.assertEqual(expected_number,actual_number, player.name + ' doesnt have '+str(expected_number)+ ' cards melded of age ' +str(age)+' but rather: ' + str(actual_number))
        
    def assert_not_melded(self, player, list_of_card_names):
        answer = True
        problematic_name = ''
        for name in list_of_card_names: 
            if player.check_if_melded(name): 
                answer = False
                problematic_name = name                
        self.assertTrue(answer, problematic_name + ' is melded for ' + player.name)      
        
    def assert_top_card(self, player, name, color):
        top_card = player.board[colors_dict[color]].top_card
        top_card_name = 'TOP CARD IS NONE'       
        if top_card is not None: top_card_name = top_card.name        
        self.assertEqual(top_card_name, name, name +' Is not top card for '+player.name+' but rather: ' + top_card_name)
    
    def assert_score(self, player, score):
        self.assertEqual(player.score_pile.score, score,  player.name+ '\'s score is not: ' + str(score) + ' but rather ' + str(player.score_pile.score))
    
    def assert_splay_mode(self, player, color, mode):
        actual_splay_mode = player.board[colors_dict[color.upper()]].splay_mode
        self.assertEqual(actual_splay_mode, mode.upper(), '{0}\'s {1} pile is splayed {2} rather then {3}'.format(player.name, color,actual_splay_mode, mode))
    
    def assert_splay_mode_by_list(self, list):
        for player, color, mode in list: self.assert_splay_mode(player, color, mode)
    
    def assert_highest_age_in_hand(self, player, age):
        if player.hand.hand_size == 0: player_highest_age = 0
        else: player_highest_age = player.hand.hand[len(player.hand.hand) -1].age
        self.assertEqual(player_highest_age, age,  player.name+ '\'s highest age is not: ' + str(age) + ' but rather:s ' + str(player_highest_age))

    def assert_highest_age_melded(self, player, age):
        player_highest_age_melded = 0
        for i in range(5):
            top_card = player.board[i].top_card
            if top_card is not None: player_highest_age_melded = max(top_card.age, player_highest_age_melded)
        self.assertEqual(player_highest_age_melded, age,  player.name+ '\'s highest melded age is not: ' + str(age) + ' but rather: ' + str(player_highest_age_melded))

    def assert_smybol_count(self, player, symbol_count):
        self.assertEqual(player.symbol_count , symbol_count,  player.name+ '\'s symbol count is not: ' + str(symbol_count) + ' but rather: ' + str(player.symbol_count))
   
    def assert_hand_size_by_list(self, list_of_pairs):
        for player, size in list_of_pairs:
            self.assert_hand_size(player, size)

    def assert_melded_by_list(self, list_of_pairs):
        for player, list in list_of_pairs:
            self.assert_melded(player, list)
            
    def assert_not_melded_by_list(self, list_of_pairs):
        for player, list in list_of_pairs:
            self.assert_not_melded(player, list)

    def assert_score_by_list(self, list_of_pairs):
        for player, score in list_of_pairs:
            self.assert_score(player, score)
            
    def assert_highest_age_in_hand_by_list(self, list_of_pairs):
        for player, age in list_of_pairs:
            self.assert_highest_age_in_hand(player, age)

    def assert_highest_age_melded_by_list(self, list_of_pairs):
        for player, age in list_of_pairs:
            self.assert_highest_age_melded(player, age)

    # Tests Tests Tests !!!
    '''
    def test_agriculture(self):
        
        orginal_age5_deck_count = len(self.thegame.game_deck.deck[4])
        
        # Should have a card to score.
        self.draw_from_deck_by_name_and_age(self.dummy_acting_player, 'Gunpowder' , 4)        
        
        self.private_setup('Agriculture',1)
        
        # Asserts that the score is 5.
        self.assert_score(self.dummy_acting_player , 5)
        
        # Asserts that a card of age 5 was removed.
        self.assertEqual(len(self.thegame.game_deck.deck[4]),  orginal_age5_deck_count - 1 , 'Not exactly 1 card removed from age5 deck')
        
        # Asserts that hand is now empty.
        self.assert_hand_size(self.dummy_acting_player, 0)

    def test_agriculture_share(self):

        orginal_age5_deck_count = len(self.thegame.game_deck.deck[4])

        # To have symbols in order to share the dogma.
        self.meld_card_from_deck_by_name_and_age(self.dummy_victim, 'Pottery', 1)   

        self.draw_from_deck_by_name_and_age(self.dummy_victim, 'Gunpowder' , 4)        
        self.private_setup('Agriculture',1)

        # Asserts that the score is 5.
        self.assert_score(self.dummy_victim , 5)
        
        # Asserts that a card of age 5 was removed.
        self.assertEqual(len(self.thegame.game_deck.deck[4]),  orginal_age5_deck_count - 1 , 'Not exactly 1 card removed from age5 deck')
        
        # Asserts that hand is now empty.
        self.assert_hand_size(self.dummy_victim, 0)
        
        # Asserting acting player drew a compensation card.
        self.assert_hand_size(self.dummy_acting_player, 1)
    
    def test_archery(self): 
    
        # To test Archery
        age_seven_card = self.thegame.game_deck.deck[6].pop()
        self.dummy_victim.hand.add_to_hand(age_seven_card)    
        
        self.private_setup('Archery',1)
        
        # Asserting that the age 7 card was transferred:
        self.assert_highest_age_in_hand(self.dummy_acting_player, 7)
        
        # Asserting that victim has only 1 card.
        self.assert_hand_size(self.dummy_victim, 1)
        
        # Asserting that victim drew a 1.
        self.assert_highest_age_in_hand(self.dummy_victim, 1)
    
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
        
        # To give one common color (red)
        self.meld_cards_by_list(self.dummy_acting_player, [('Oars' , 1),('City States' , 1)])
        self.meld_cards_by_list(self.dummy_victim, [('Construction', 2)])
        
        # To make sure you don't meld and existing color. And that there are three different colors after melding Experimentation (you should score 3).
        self.draw_cards_by_list(self.dummy_acting_player, [('Gunpowder' , 4),('Experimentation' , 4)])

        self.private_setup('Clothing',1)   

        # The expected cards are melded
        self.assert_melded(self.dummy_acting_player, ['City States', 'Oars', 'Experimentation', 'Clothing'])
        self.assert_melded(self.dummy_victim, ['Construction'])
        self.assertTrue(not self.dummy_acting_player.check_if_melded('Gunpowder') , 'Gunpowder melded')
        
        # To make sure scoring is as it should be.        
        self.assert_score(self.dummy_acting_player , 3)
    
    def test_clothing_share(self):        
        
        # To have symbols in order to share the dogma.
        self.meld_card_from_deck_by_name_and_age(self.dummy_victim, 'Agriculture', 1)   
        
        # To give one common color (red)
        self.meld_card_from_deck_by_name_and_age(self.dummy_victim, 'Oars' , 1)
        self.meld_card_from_deck_by_name_and_age(self.dummy_acting_player, 'Construction', 2)
        
        # To make sure you don't meld an existing color. And that there are three different colors after melding Experimentation (you should score 3).
        self.draw_from_deck_by_name_and_age(self.dummy_victim, 'Gunpowder' , 4)
        self.draw_from_deck_by_name_and_age(self.dummy_victim, 'Experimentation' , 4)
        self.meld_card_from_deck_by_name_and_age(self.dummy_victim, 'City States' , 1)
        
        self.private_setup('Clothing',1)   

        # To make sure scoring is as it should be.
        self.assert_score(self.dummy_victim, 3 )
        self.assert_score(self.dummy_acting_player , 1)
        
        # The expected cards are melded
        self.assert_melded(self.dummy_victim, ['City States', 'Oars', 'Agriculture', 'Experimentation']) 
        self.assert_melded(self.dummy_acting_player, ['Construction', 'Clothing'])
        self.assertTrue(not self.dummy_victim.check_if_melded('Gunpowder') , 'Gunpowder melded')
        
                
        # Asserting acting player drew a compensation card.
        self.assert_hand_size(self.dummy_acting_player , 1)
    
    def test_code_of_laws(self):
        # To have a card to meld.
        self.draw_from_deck_by_name_and_age(self.dummy_acting_player, 'Specialization' , 9)
        
        self.private_setup('Code of Laws',1)
        
        purple_pile_names = [card.name for card in self.dummy_acting_player.board[3].pile]
        
        # Asserting that indeed Specialization was tucked.
        self.assertEqual(purple_pile_names, ['Specialization', 'Code of Laws'] , str(purple_pile_names))
        
        # Asserting that the splay added the factory on emancipation.
        self.assert_smybol_count(self.dummy_acting_player, [2,1,0,0,1,0])
        
        # Asserting that hand is now empty.
        self.assert_hand_size(self.dummy_acting_player, 0)

    def test_code_of_laws_share(self):

        # To have symbols in order to share the dogma.
        self.meld_card_from_deck_by_name_and_age(self.dummy_victim, 'City States', 1)   

        # To have a card to meld.
        self.draw_from_deck_by_name_and_age(self.dummy_victim, 'Specialization' , 9)
        self.private_setup('Code of Laws',1)
        
        purple_pile_names = [card.name for card in self.dummy_victim.board[3].pile]
        
        # Asserting that indeed Specialization was tucked.
        self.assertEqual(purple_pile_names, ['Specialization', 'City States'] , str(purple_pile_names))
        
        # Asserting that the splay added the factory on emancipation.
        self.assert_smybol_count(self.dummy_victim, [2,0,0,1,1,0])
        
        # Asserting that hand is now empty.
        self.assert_hand_size(self.dummy_victim, 0)
        
        # Asserting acting player drew a compensation card. 
        self.assert_hand_size(self.dummy_acting_player, 1)
       
    def test_domestication(self):
        # To have a card to meld.
        self.draw_cards_by_list(self.dummy_acting_player, [('Emancipation' , 6),('Archery' , 1)])
        
        self.private_setup('Domestication',1)
                
        # Asserting that indeed Emancipation wasnt melded melded and that a 1 (Agriculture) was drew:
        self.assert_hand_contains(self.dummy_acting_player, ['Agriculture' , 'Emancipation'])
        
        # Asserting that Archery was melded.
        self.assertEqual(self.dummy_acting_player.board[0].top_card.name , 'Archery' ,'Wrong top card: ' + self.dummy_acting_player.board[0].top_card.name)

    def test_domestication_share(self):
        # To have symbols in order to share the dogma.
        self.meld_card_from_deck_by_name_and_age(self.dummy_victim, 'Mysticism', 1)
        
        # To have a card to meld.
        self.draw_from_deck_by_name_and_age(self.dummy_victim, 'Emancipation' , 6)
        self.draw_from_deck_by_name_and_age(self.dummy_victim, 'Archery' , 1)
        
        self.private_setup('Domestication',1)
        
        hand_cards_names = [card.name for card in self.dummy_victim.hand.hand]
        
        # Asserting that indeed Emancipation wasnt melded melded and that a 1 (Agriculture) was drew:
        self.assertEqual(hand_cards_names, ['Agriculture' , 'Emancipation'] , str(hand_cards_names))
        
        # Asserting that Archery was melded.
        self.assertEqual(self.dummy_victim.board[0].top_card.name , 'Archery' ,'Wrong top card: ' + self.dummy_victim.board[0].top_card.name)

        # Asserting acting player drew a card. Should have two cards - one from the dogma effect and one from compensation.
        self.assertEqual(self.dummy_acting_player.hand.hand_size , 2 , 'No card was drawn')
            
    def test_masonry(self):
    
        # To have a card to meld.
        self.draw_cards_by_list(self.dummy_acting_player, [('City States' , 1), ('Archery' , 1), ('Domestication' , 1), ('Metalworking' , 1)])
    
        self.private_setup('Masonry',1)
        
        # Asserting hand is empty.
        self.assertEqual(self.dummy_acting_player.hand.hand, [] , 'Hand isnt empty')
        
        # Asserting the cards were melded.
        self.assert_melded(self.dummy_acting_player, ['City States', 'Archery' , 'Domestication' , 'Metalworking'])
        
        # Asserting Monument was achieved and removed from game.
        self.assert_player_has_achievement(self.dummy_acting_player, 'Monument')
               
    def test_masonry_share(self):

        # To have symbols in order to share the dogma.
        self.meld_card_from_deck_by_name_and_age(self.dummy_victim, 'Mysticism', 1)
        
        # To have a card to meld.
        self.draw_from_deck_by_name_and_age(self.dummy_victim, 'City States' , 1)
        self.draw_from_deck_by_name_and_age(self.dummy_victim, 'Archery' , 1)
        self.draw_from_deck_by_name_and_age(self.dummy_victim, 'Domestication' , 1)
        self.draw_from_deck_by_name_and_age(self.dummy_victim, 'Metalworking' , 1)        
    
        self.private_setup('Masonry',1)
        
        # Asserting hand is empty.
        self.assertEqual(self.dummy_victim.hand.hand, [] , 'Hand isnt empty')
        
        # Asserting the cards were melded.
        self.assertTrue(self.dummy_victim.check_if_melded('City States'), 'City States not melded')
        self.assertTrue(self.dummy_victim.check_if_melded('Archery'), 'Archery not melded')
        self.assertTrue(self.dummy_victim.check_if_melded('Domestication'), 'Domestication not melded')
        self.assertTrue(self.dummy_victim.check_if_melded('Metalworking'), 'Metalworking not melded')
        
        # Asserting Monument was achieved and removed from game.
        self.assertTrue('Monument' not in self.thegame.available_special_achievements , 'Monument wasnt removed from available achievements')
        self.assertTrue('Monument' in self.dummy_victim.achievements , 'Monument wasnt added to player')
        self.assertEqual(self.dummy_victim.achievements_number , 1, 'Number of achievements isnt 1')

        # Asserting acting player drew a card.
        self.assertEqual(self.dummy_acting_player.hand.hand_size , 1 , 'No card was drawn')
    
    def test_metalworking(self):
        # discard all age 1 cards without castles.

        for card in self.thegame.game_deck.deck[0][:]:   # Copy the list. NEVER MODIFY SOMETHING YOU ITERATE OVER...
            if 'CASTLE' not in card.symbols: self.thegame.game_deck.deck[0].remove(card)
                
        self.private_setup('Metalworking',1)
        
        """There are 9 cards with 'CASTLE' symbol on them, one of which is metalworking which is melded. The first card on the age2 deck is calender and doesn't have a castle."""
        
        # Asserting score is correct.
        self.assertEqual(self.dummy_acting_player.score_pile.score , 8, 'Score incorrect')
        
        # Asserting only cards with castles were scored.
        for card in self.dummy_acting_player.score_pile.score_pile: self.assertTrue('CASTLE' in card.symbols, 'Card without castle was scored')
        
        # Asserting that age 1 deck is empty after all cards were scored.
        self.assertEqual(self.thegame.game_deck.deck[0], [], 'Age 1 deck isnt empty')      
        
        # Asserting that hand has exactly one card and that it is calander
        self.assertEqual(self.dummy_acting_player.hand.hand_size, 1, 'Hand contains more then one card')
        self.assertEqual(self.dummy_acting_player.hand.hand[0].name, 'Calendar', 'Hand doesnt contain calander.')

    def test_metalworking_share(self):
        
        # discard all age 1 cards without castles.
        for card in self.thegame.game_deck.deck[0][:]:
            if 'CASTLE' not in card.symbols: self.thegame.game_deck.deck[0].remove(card)

        # To have symbols in order to share the dogma.
        self.meld_card_from_deck_by_name_and_age(self.dummy_victim, 'Masonry', 1)
            
        self.private_setup('Metalworking',1)
        
        """There are 9 cards with 'CASTLE' symbol on them, two of which are metalworking and masonry which are melded. The first card on the age2 deck is calender and doesn't have a castle."""
        
        # Asserting score is correct.
        self.assertEqual(self.dummy_victim.score_pile.score , 7, 'Score incorrect')
        
        # Asserting only cards with castles were scored.
        for card in self.dummy_victim.score_pile.score_pile: self.assertTrue('CASTLE' in card.symbols, 'Card without castle was scored')
        
        # Asserting that age 1 deck is empty after all cards were scored.
        self.assertEqual(self.thegame.game_deck.deck[0], [], 'Age 1 deck isnt empty')      
        
        # Asserting that hand has exactly one card and that it is calander
        self.assertEqual(self.dummy_victim.hand.hand_size, 1, 'Hand contains more then one card')
        self.assertEqual(self.dummy_victim.hand.hand[0].name, 'Calendar', 'Hand doesnt contain calander.')
        
        # Asserting acting player drew a card. (he should have one from the dogma as well)
        self.assertEqual(self.dummy_acting_player.hand.hand_size , 2 , 'No card was drawn')
    
    def test_mysticism_test1(self):
        # In this test we draw a card of the same color as a color on the board (We draw Agriculture and have Domestication)
 
        # To have a Yellow card for when we draw Agriculture during the dogma.
        self.meld_card_from_deck_by_name_and_age(self.dummy_acting_player, 'Domestication', 1)
        
        self.private_setup('Mysticism',1)
        
        # Asserting the cards were melded.
        self.assertTrue(self.dummy_acting_player.check_if_melded('Mysticism'), 'Mysticism not melded')
        self.assertTrue(self.dummy_acting_player.check_if_melded('Domestication'), 'Domestication not melded')
        self.assertTrue(self.dummy_acting_player.check_if_melded('Agriculture'), 'Agriculture not melded')

        # Asserting hand is empty.
        self.assertEqual(self.dummy_acting_player.hand.hand_size , 0 , 'Hand not empty')
        
    def test_mysticism_test1_share(self):
        # In this test we draw a card of the same color as a color on the board (We draw Agriculture and have Masonry)    
        
        # To have symbols in order to share the dogma and to have a Yellow card for when we draw Agriculture during the dogma.
        self.meld_card_from_deck_by_name_and_age(self.dummy_victim, 'Masonry', 1)

        self.private_setup('Mysticism',1)        

        # Asserting the cards were melded.
        self.assertTrue(self.dummy_victim.check_if_melded('Masonry'), 'Mysticism not melded')
        self.assertTrue(self.dummy_victim.check_if_melded('Agriculture'), 'Agriculture not melded')
        self.assertEqual(self.dummy_victim.board[2].top_card.name, 'Agriculture', 'Agricuturle not top card')
        
        # Asserting hand is empty.
        self.assertEqual(self.dummy_victim.hand.hand_size , 0 , 'Hand not empty')
        
        # Asserting acting player drew a card. (he should have one from the dogma as well)
        self.assertEqual(self.dummy_acting_player.hand.hand_size , 2 , 'No card was drawn')
        
    def test_mysticism_test2(self):
        """ In this test we draw a card of a different color from colors on the board (We draw Agriculture and Only have Green - The Wheel)"""
        
        self.private_setup('Mysticism',1)
        
        # Asserting acting player drew Agriculture to hand.
        self.assertEqual(self.dummy_acting_player.hand.hand_size , 1 , 'No card was drawn')
        self.assertEqual(self.dummy_acting_player.hand.hand[0].name , 'Agriculture' , 'No card was drawn')
        
    def test_mysticism_test2_share(self):
        """In this test we draw a card of a different color from colors on the board (We draw Agriculture and Only have red - Metalworking)"""


        # To have symbols in order to share the dogma and to have a Yellow card for when we draw Agriculture during the dogma.
        self.meld_card_from_deck_by_name_and_age(self.dummy_victim, 'The Wheel', 1)
    
        self.private_setup('Mysticism',1)        

        # Asserting acting player drew Agriculture to hand.
        self.assertEqual(self.dummy_victim.hand.hand_size , 1 , 'No card was drawn')
        self.assertEqual(self.dummy_victim.hand.hand[0].name , 'Agriculture' , 'No card was drawn')
        
        # Asserting acting player drew a card. (he should have one from the dogma as well)
        self.assertEqual(self.dummy_acting_player.hand.hand_size , 2 , 'No card was drawn')
        
    def test_oars(self):
        
        # So that victim will have a card to give.
        self.draw_from_deck_by_name_and_age(self.dummy_victim, 'City States' , 1)

        self.private_setup('Oars',1)
        
        # Check that City States was transferred.
        self.assertEqual(self.dummy_victim.hand.hand_size, 1 , 'Hand doesnt contain just one card')
        self.assertEqual(self.dummy_victim.hand.hand[0].name, 'Agriculture' , 'Hand doesnt contain Agriculture')
        
        # Check that City States was scored.
        self.assert_score(self.dummy_acting_player, 1 )
        self.assert_score_pile_contains(self.dummy_acting_player, ['City States'])        
        
    def test_oars_share(self):
        """ Not exactly share per-se. In this test we have a player who is sharing the second action while no card was transferred"""
        # To have symbols in order to share the dogma.
        self.meld_card_from_deck_by_name_and_age(self.dummy_victim, 'Masonry', 1)
        
        self.private_setup('Oars',1)
        
        # Check that victim drew one card.
        self.assert_hand_size(self.dummy_victim, 1)
        self.assert_hand_contains(self.dummy_victim , ['Agriculture'])
        
        # Check that dummy_acting_player drew two - one from dogma and one from compensation.
        self.assert_hand_size(self.dummy_acting_player , 2)
        self.assert_hand_contains(self.dummy_acting_player , ['Archery' , 'City States'])
    
    def test_pottery(self):
        # Giving sharer symbols
        self.meld_card_from_deck_by_name_and_age(self.dummy_sharer, 'Agriculture', 1)
        
        # Sharer should have 3 cards to return (giving him 4).
        self.draw_cards_by_list(self.dummy_sharer, [('City States', 1), ('Education', 3), ('Specialization', 9),('Bioengineering', 10) ])

        # adcting player should have 1 card to return.
        self.draw_cards_by_list(self.dummy_acting_player, [('Astronomy', 5)])
        
        self.private_setup('Pottery',1)

        # Asserting hands contain right amounts. 
        #Sharer should have 1 because he returned 3 and drew 1. Acting should have 2 because he returned 1 and drew 1 + compensation.
        self.assert_hand_size_by_list([(self.dummy_sharer , 2),(self.dummy_acting_player, 2)])
        
        # Asserting right scores
        self.assert_score_by_list([(self.dummy_sharer , 3),(self.dummy_acting_player, 1)])
        
    def test_sailing(self):
                
        self.meld_card_from_deck_by_name_and_age(self.dummy_sharer, 'Code of Laws', 1)
        
        #TODO: WHY THE HELL DO I NEED TO REVERSE THE DECK TWICE?!?!
        #TODO: WHY THE HELL DO I NEED TO REVERSE THE DECK TWICE?!?!
        #TODO: WHY THE HELL DO I NEED TO REVERSE THE DECK TWICE?!?!
        #TODO: WHY THE HELL DO I NEED TO REVERSE THE DECK TWICE?!?!
        #TODO: WHY THE HELL DO I NEED TO REVERSE THE DECK TWICE?!?!
        #TODO: WHY THE HELL DO I NEED TO REVERSE THE DECK TWICE?!?!        
        self.thegame.game_deck.deck[0].reverse()
        card_melded_by_sharer = self.thegame.game_deck.deck[0][:][0].name       
        card_melded_by_acting_player = self.thegame.game_deck.deck[0][:][1].name
        self.thegame.game_deck.deck[0].reverse()

        print(str([card_melded_by_acting_player,card_melded_by_sharer]))
        self.private_setup('Sailing',1)
        print(str([card.name for card in self.thegame.game_deck.deck[0]]))
        
        self.assert_melded(self.dummy_acting_player, [card_melded_by_acting_player])
        self.assert_melded(self.dummy_sharer, [card_melded_by_sharer])
        
    def test_the_wheel(self):
    
        # Giving sharer symbols    
        self.meld_card_from_deck_by_name_and_age(self.dummy_sharer, 'Masonry', 1)
    
        self.private_setup('The Wheel',1)
        
        # Asserting that the right amount of draws were made.
        self.assert_hand_size(self.dummy_acting_player , 3)
        self.assert_hand_size(self.dummy_sharer , 2)
        
    def test_tools(self):
        # Giving sharer symbols
        self.meld_card_from_deck_by_name_and_age(self.dummy_sharer, 'Writing', 1)
        
        self.draw_cards_by_list(self.dummy_sharer, [('Agriculture', 1), ('Archery', 1), ('Clothing', 1)])
        self.draw_cards_by_list(self.dummy_acting_player, [('Education', 3)])        
        
        self.private_setup('Tools',1)
        
        # Asserting hands contain right amounts.
        self.assert_hand_size(self.dummy_sharer , 0)
        self.assert_hand_size(self.dummy_acting_player , 4)
        
        # Asserting the right ages were drawn
        self.assert_highest_age_melded(self.dummy_sharer,3)
        self.assert_highest_age_in_hand(self.dummy_acting_player,1)

    def test_writing(self):
        # Giving sharer symbols
        self.meld_card_from_deck_by_name_and_age(self.dummy_sharer, 'Philosophy', 2)
        
        self.private_setup('Writing',1)
        
        # Asserting hands contain right amounts.
        self.assert_hand_size(self.dummy_sharer , 1)
        self.assert_hand_size(self.dummy_acting_player , 2)
        
        # Asserting they both drew a 2
        self.assert_highest_age_in_hand(self.dummy_sharer,2)
        self.assert_highest_age_in_hand(self.dummy_acting_player,2)
        
    def test_calendar(self):
        # Giving sharer symbols
        self.meld_card_from_deck_by_name_and_age(self.dummy_sharer, 'Agriculture', 1)
        
        # Sharer should have 0 cards in his hand and one in his score pile.
        self.score_cards_by_list(self.dummy_sharer, [('Masonry', 1)])
        
        # acting player should have 1 card in his hand and two in his score pile.
        self.draw_cards_by_list(self.dummy_acting_player, [('Metalworking', 1)])
        self.score_cards_by_list(self.dummy_acting_player, [('City States', 1),('Code of Laws',1)])
        
        self.private_setup('Calendar',2)

        # Asserting hands contain right amounts. 
        # Sharer should have two because he started with empty hand and drew 2.
        # Acting shuold have 4 because he started with 1, drew 2 and got compensation.
        self.assert_hand_size_by_list([(self.dummy_sharer , 2),(self.dummy_acting_player, 4)])
        
        # Asserting highest age in hand is 3.
        self.assert_highest_age_in_hand_by_list([(self.dummy_sharer , 3),(self.dummy_acting_player, 3)])

    def test_canal_building(self):
    
        # Giving sharer symbols
        self.meld_card_from_deck_by_name_and_age(self.dummy_sharer, 'Sailing', 1)
    
    
        self.draw_cards_by_list(self.dummy_acting_player, [('Astronomy', 5), ('Education',3),('Banking',5)])
        self.score_cards_by_list(self.dummy_acting_player, [('City States', 1),('Calendar',2)])

        self.draw_cards_by_list(self.dummy_sharer, [('Specialization', 9)])

        self.private_setup('Canal Building',2)
        
        self.assert_hand_contains(self.dummy_acting_player, ['Calendar','Education'])        
        self.assert_hand_size_by_list([(self.dummy_sharer , 0),(self.dummy_acting_player, 3)])
        self.assert_score_by_list([(self.dummy_sharer , 9),(self.dummy_acting_player, 11)])
        self.assert_score_pile_contains(self.dummy_acting_player, ['Astronomy','City States','Banking'])
        self.assert_score_pile_contains(self.dummy_sharer, ['Specialization'])

    def test_currency(self):
    
        # Giving sharer symbols
        self.meld_card_from_deck_by_name_and_age(self.dummy_sharer, 'Sailing', 1)

        self.draw_cards_by_list(self.dummy_acting_player, [('Agriculture', 1), ('Masonry', 1),('The Wheel', 1),('Education',3),('Optics',3),('Calendar',2),('Gunpowder',4)])
        self.draw_cards_by_list(self.dummy_sharer, [('Banking', 5)])        
        
        self.private_setup('Currency',2)
        
        self.assert_hand_size_by_list([(self.dummy_sharer , 0),(self.dummy_acting_player, 1)])
        self.assert_score_by_list([(self.dummy_sharer , 2),(self.dummy_acting_player, 8)])
        
    def test_construction1(self):

        # Acting player missing purple, Sharer has all top 5 cards.
        self.meld_cards_by_list(self.dummy_acting_player, [('Agriculture', 1), ('Metalworking', 1),('Tools', 1)])
        self.meld_cards_by_list(self.dummy_sharer, [('Masonry', 1), ('Archery', 1),('Writing', 1),('City States',1),('The Wheel',1)])
        
        # Victim has hand of 3, out of which he relinquishes 2.
        self.draw_cards_by_list(self.dummy_victim, [('Optics',3),('Calendar',2),('Gunpowder',4)])

        self.private_setup('Construction',2)
        
        self.assert_hand_size_by_list([(self.dummy_sharer , 0),(self.dummy_acting_player, 3),(self.dummy_victim , 1)])
        
        self.assert_player_has_achievement(self.dummy_sharer, 'Empire')
    
    def test_construction2(self):
    

        # Acting player missing purple, Sharer has all top 5 cards.
        self.meld_cards_by_list(self.dummy_acting_player, [('Agriculture', 1), ('Sailing', 1),('Tools', 1),('Code of Laws',1)])
        self.meld_cards_by_list(self.dummy_sharer, [('Masonry', 1), ('Archery', 1),('Writing', 1),('City States',1),('The Wheel',1)])
        
        # Victim has hand of 3, out of which he relinquishes 2.
        self.draw_cards_by_list(self.dummy_victim, [('Optics',3)])

        self.private_setup('Construction',2)
        
        self.assert_hand_size_by_list([(self.dummy_sharer , 0),(self.dummy_acting_player, 2),(self.dummy_victim , 0)])
        
        self.assertEqual(len(self.thegame.available_special_achievements),5, 'Not all special achievements are accounted for.')
        
    def test_fermenting(self):
        
        # Acting player has 5 leaves (along with Fermenting), Sharer has 6.
        self.meld_cards_by_list(self.dummy_acting_player, [('Clothing', 1)])
        self.meld_cards_by_list(self.dummy_sharer, [('Agriculture', 1), ('Pottery', 1)])
    
        self.private_setup('Fermenting',2)

        self.assert_hand_size_by_list([(self.dummy_sharer , 3),(self.dummy_acting_player, 3),(self.dummy_victim , 0)])
        
    def test_mapmaking1(self):
        # In this test, Sharer is victim as well.
        
        self.score_cards_by_list(self.dummy_sharer, [('Calendar',2)])
        self.score_cards_by_list(self.dummy_victim, [('Agriculture',1),('Education',3)])
        
        self.private_setup('Mapmaking',2)
        
        self.assert_score_by_list([(self.dummy_sharer , 2),(self.dummy_acting_player, 2),(self.dummy_victim , 3)])
        
    def test_mapmaking2(self):
        # In this test, Sharer is victim as well.        
        self.score_cards_by_list(self.dummy_sharer, [('City States',1),('Masonry',1)])
        self.score_cards_by_list(self.dummy_victim, [('Agriculture',1),('Writing',1),('Education',3)])
        
        self.private_setup('Mapmaking',2)
        
        self.assert_score_by_list([(self.dummy_sharer , 1),(self.dummy_acting_player, 3),(self.dummy_victim , 4)])
        
    def test_mapmaking3(self):
        # In this test, Sharer is victim as well.        
        self.score_cards_by_list(self.dummy_sharer, [('Fermenting',2)])
        self.score_cards_by_list(self.dummy_victim, [('Education',3)])
        
        self.private_setup('Mapmaking',2)
        
        self.assert_score_by_list([(self.dummy_sharer , 2),(self.dummy_acting_player, 0),(self.dummy_victim , 3)]) 

    def test_mapmaking4(self):
        # Giving sharer symbols
        self.meld_card_from_deck_by_name_and_age(self.dummy_sharer, 'Sailing', 1)

        self.score_cards_by_list(self.dummy_victim, [('Agriculture',1),('Writing',1),('Education',3)])
        
        self.private_setup('Mapmaking',2)
        
        self.assert_score_by_list([(self.dummy_sharer , 1),(self.dummy_acting_player, 2),(self.dummy_victim , 4)])        
    
    def test_mathematics(self):
    
        # Giving sharer symbols
        self.meld_card_from_deck_by_name_and_age(self.dummy_sharer, 'Writing', 1)

        self.draw_cards_by_list(self.dummy_acting_player, [('Education', 3)])
        self.draw_cards_by_list(self.dummy_sharer, [('Industrialization', 6)])
        
        self.private_setup('Mathematics',2)

        self.assert_hand_size_by_list([(self.dummy_sharer , 0),(self.dummy_acting_player, 1),(self.dummy_victim , 0)])
        
        self.assert_highest_age_melded_by_list([(self.dummy_sharer , 7),(self.dummy_acting_player, 4),(self.dummy_victim, 0)])
    
    def test_monotheism1(self):
        # Giving sharer symbols
        self.meld_card_from_deck_by_name_and_age(self.dummy_sharer, 'Construction', 2)
        
        self.meld_cards_by_list(self.dummy_victim, [('Writing', 1),('Canal Building',2)])
        
        self.private_setup('Monotheism',2)
        
        self.assert_melded_by_list([(self.dummy_victim, ['Agriculture']),(self.dummy_sharer, ['Archery']),(self.dummy_acting_player, ['City States'])])
        
        self.assert_not_melded(self.dummy_victim, 'Canal Building')
        self.assert_top_card(self.dummy_acting_player, 'Monotheism' , 'PURPLE')
        
        self.assert_hand_size_by_list([(self.dummy_sharer , 0),(self.dummy_acting_player, 1),(self.dummy_victim , 0)])
        
    def test_monotheism2(self):
        # Giving sharer symbols
        self.meld_card_from_deck_by_name_and_age(self.dummy_sharer, 'Construction', 2)
                
        self.private_setup('Monotheism',2)
        
        self.assert_melded_by_list([(self.dummy_sharer, ['Agriculture']),(self.dummy_acting_player, ['Archery'])])
        
        self.assert_top_card(self.dummy_acting_player, 'Monotheism' , 'PURPLE')
        self.assert_top_card(self.dummy_sharer, 'Agriculture' , 'YELLOW')
        self.assert_top_card(self.dummy_acting_player, 'Archery' , 'RED')
        
        self.assert_hand_size_by_list([(self.dummy_sharer , 0),(self.dummy_acting_player, 1),(self.dummy_victim , 0)])
    
    def test_philosophy(self):
        # Victim is also sharer in this test.

        # Giving shareres symbols
        self.meld_card_from_deck_by_name_and_age(self.dummy_sharer, 'Education', 3)
        self.meld_card_from_deck_by_name_and_age(self.dummy_victim, 'Experimentation', 4)

        # Those will be scored by the second action
        self.draw_cards_by_list(self.dummy_acting_player, [('Industrialization', 6)])
        self.draw_cards_by_list(self.dummy_sharer, [('Agriculture', 1)])
        
        # Yellow should be splayed left
        self.meld_cards_by_list(self.dummy_acting_player, [('Oars', 1), ('Masonry', 1),('Domestication', 1)])        
        
        # Nothing should be splayed.
        self.meld_cards_by_list(self.dummy_sharer, [('Metalworking', 1), ('Compass', 3),('Machinery', 3),('Writing', 1)])        
        
        self.private_setup('Philosophy',2)
        
        print(str(self.dummy_acting_player.symbol_count))
        print(str(self.dummy_sharer.symbol_count))
        print(str(self.dummy_victim.symbol_count))
        
        self.assert_score_by_list([(self.dummy_sharer , 1),(self.dummy_acting_player, 6),(self.dummy_victim , 0)])        
        
        # Checking that every pile is in the right splay mode.
        self.assert_splay_mode_by_list([(self.dummy_acting_player, 'Blue', 'none'),(self.dummy_acting_player, 'red', 'none'),(self.dummy_acting_player, 'green', 'none'),(self.dummy_acting_player, 'purple', 'none'),(self.dummy_acting_player, 'yellow', 'left'),(self.dummy_sharer, 'Blue', 'none'),(self.dummy_sharer, 'red', 'none'),(self.dummy_sharer, 'green', 'none'),(self.dummy_sharer, 'purple', 'none'),(self.dummy_sharer, 'yellow', 'none'),(self.dummy_victim, 'Blue', 'none'),(self.dummy_victim, 'yellow', 'none'),(self.dummy_victim, 'green', 'none'),(self.dummy_victim, 'purple', 'none'),(self.dummy_victim, 'red', 'none'),])
    
    def test_road_building(self):
        # Giving shareres symbols
        self.meld_card_from_deck_by_name_and_age(self.dummy_sharer, 'Masonry', 1)
        
        # To have cards to meld.
        self.draw_cards_by_list(self.dummy_acting_player, [('Archery', 1),('Agriculture', 1)])
        self.draw_cards_by_list(self.dummy_sharer, [('City States', 1),('Code of Laws', 1)])

        #To have a card to steal
        self.meld_cards_by_list(self.dummy_acting_player, [('Currency', 2)])
        self.meld_cards_by_list(self.dummy_victim, [('Sailing', 1)])
        
        self.private_setup('Road Building',2)
        
        self.assert_not_melded_by_list([(self.dummy_acting_player, ['Archery','Currency' ]),(self.dummy_victim, ['Sailing','The Wheel'])])
        
        self.assert_melded_by_list([(self.dummy_acting_player, ['Agriculture','Road Building','Sailing']),(self.dummy_sharer, ['City States','Code of Laws','Code of Laws','Currency'])])
    
    def test_alchemy(self):
        
        # Both should have 6 castles. Sharer draws Red and loses all hand, active draws two non reds, melds one scores the other.
        
        # Giving shareres symbols
        self.meld_cards_by_list(self.dummy_sharer, [('Monotheism',2),('Road Building',2), ('Agriculture', 1)])
        
        # raising to 6 castles
        self.meld_cards_by_list(self.dummy_acting_player, [('Construction',2),('Mapmaking',2)])
        
        self.private_setup('Alchemy',3)
        
        self.assert_melded(self.dummy_acting_player, ['Enterprise'])
        self.assert_score(self.dummy_acting_player, 4)
        
        self.assert_score(self.dummy_sharer, 0)
        self.assert_hand_size(self.dummy_acting_player, 1)
        self.assert_hand_size(self.dummy_sharer, 0)
    
    def test_compass1(self):
        
        # Victim should have to move Agriculture and take nothing. Sharer will move nothing.
        
        self.meld_cards_by_list(self.dummy_victim, [('Clothing',1),('Agriculture',1)])    
        self.meld_cards_by_list(self.dummy_sharer, [('Measurement',5)])
        
        self.private_setup('Compass',3)
        
        self.assert_melded(self.dummy_victim, ['Clothing'])
        self.assert_melded(self.dummy_acting_player, ['Agriculture'])
        self.assert_melded(self.dummy_sharer, ['Measurement'])
        self.assert_not_melded(self.dummy_victim, ['Agriculture'])
      
    def test_compass2(self):
        
        # Victim should have to move Agriculture and take nothing. Sharer will move nothing.
        
        self.meld_cards_by_list(self.dummy_victim, [('Clothing',1),('Agriculture',1)])    
        self.meld_cards_by_list(self.dummy_acting_player, [('Archery',1),('Metalworking',1)])
        
        self.private_setup('Compass',3)   

        self.assert_melded(self.dummy_victim, ['Clothing','Metalworking'])
        self.assert_melded(self.dummy_acting_player, ['Agriculture','Compass'])
        self.assert_melded(self.dummy_sharer, ['Archery'])
        self.assert_not_melded(self.dummy_victim, ['Agriculture'])
        self.assert_not_melded(self.dummy_acting_player, ['Archery','Metalworking'])
       
    def test_education(self):
        
        # Active should end up with 14 points, sharer with 0.
        
        # Giving shareres symbols
        self.meld_card_from_deck_by_name_and_age(self.dummy_sharer, 'Philosophy', 2)
        
        # Putting cards in score piles.
        self.score_cards_by_list(self.dummy_sharer, [('Stem Cells',10)])
        self.score_cards_by_list(self.dummy_acting_player, [('Industrialization',6),('Atomic Theory',6)])
        
        self.private_setup('Education',3)
        
        self.assert_score(self.dummy_sharer, 0)
        self.assert_score(self.dummy_acting_player, 6)
        self.assert_highest_age_in_hand(self.dummy_acting_player, 8)
        self.assert_highest_age_in_hand(self.dummy_sharer, 2)
        self.assert_hand_size(self.dummy_acting_player, 2)
        self.assert_hand_size(self.dummy_sharer, 1)
    
    def test_engineering(self):
        # Giving shareres symbols
        self.meld_cards_by_list(self.dummy_sharer, [('Masonry',1),('Archery',1)])
        self.meld_cards_by_list(self.dummy_acting_player, [('Oars',1),('Monotheism',2)])
        
        # Giving victim cards i transfer
        self.meld_cards_by_list(self.dummy_victim, [('City States',1),('Clothing',1), ('Domestication', 1),('Tools', 1)])


        self.private_setup('Engineering',3)
        
        self.assert_not_melded(self.dummy_victim, ['City States','Domestication','Tools'])
        self.assert_score(self.dummy_acting_player, 3)
        self.assert_splay_mode(self.dummy_acting_player, 'RED', 'LEFT')
    
    def test_feudalism(self):
	
        # Giving shareres symbols
        self.meld_cards_by_list(self.dummy_sharer, [('Masonry',1)])	
        
        # To splay
        self.meld_cards_by_list(self.dummy_sharer, [('City States',1),('Code of Laws',1)])	

        # Giving victim a card with castle
        self.draw_cards_by_list(self.dummy_victim, [('Tools',1),('Agriculture',1)])	
        
        self.private_setup('Feudalism',3)

        self.assert_hand_not_contains(self.dummy_victim, ['Tools'])      
        self.assert_hand_contains(self.dummy_acting_player, ['Tools'])
        self.assert_hand_contains(self.dummy_victim, ['Agriculture'])
        self.assert_splay_mode(self.dummy_sharer, 'PURPLE', 'LEFT')
        self.assert_splay_mode(self.dummy_sharer, 'Yellow', 'None')
        self.assert_splay_mode(self.dummy_acting_player, 'PURPLE', 'None')
        self.assert_splay_mode(self.dummy_acting_player, 'Yellow', 'None')
        self.assert_hand_size(self.dummy_acting_player, 2)
        
    def test_machinery(self):
        
        # Giving shareres symbols
        self.meld_cards_by_list(self.dummy_sharer, [('Agriculture',1)])
        
        # To splay
        self.meld_cards_by_list(self.dummy_sharer, [('Archery',1),('Metalworking',1)])
        
        # Giving sharer card with castle to score
        self.draw_cards_by_list(self.dummy_sharer, [('Oars',1)])
        
        # Giving victim cards
        self.draw_cards_by_list(self.dummy_victim, [('Tools',1),('Monotheism',2), ('Industrialization', 6)])
        
        self.draw_cards_by_list(self.dummy_acting_player, [('Specialization',9), ('Collaboration', 9), ('Bicycle', 7)])
        
        self.private_setup('Machinery',3)
        
        # Test demand
        self.assert_hand_not_contains(self.dummy_victim, ['Tools', 'Monotheism', 'Industrialization'])      
        self.assert_hand_not_contains(self.dummy_acting_player, ['Specialization', 'Collaboration'])
        self.assert_hand_contains(self.dummy_acting_player, ['Bicycle', 'Tools', 'Industrialization'])
        self.assert_hand_contains(self.dummy_victim, ['Specialization', 'Collaboration'])
        self.assert_splay_mode(self.dummy_sharer, 'RED', 'LEFT')
        self.assert_splay_mode(self.dummy_acting_player, 'RED', 'None')
        self.assert_hand_size(self.dummy_acting_player, 4)
        
        # Test non-demand
        self.assert_hand_not_contains(self.dummy_sharer, ['Oars'])
        self.assert_score_pile_contains(self.dummy_sharer, ['Oars'])
        self.assert_score(self.dummy_sharer, 1)
        self.assert_hand_not_contains(self.dummy_acting_player, ['Monotheism'])
        self.assert_score_pile_contains(self.dummy_acting_player, ['Monotheism'])
        self.assert_score(self.dummy_acting_player, 2)
        
    def test_medicine1(self):
        # In this test both sharer and victim are victims.
        
        # Sharer should have 0 cards in his hand and one in his score pile.
        self.score_cards_by_list(self.dummy_victim, [('Industrialization', 6),('Agriculture',1)])
        
        # Sharer should have 0 cards in his hand and one in his score pile.
        self.score_cards_by_list(self.dummy_sharer, [('Specialization', 9),('Masonry',1)])
        
        self.private_setup('Medicine',3)
    
        self.assert_score_by_list([(self.dummy_sharer, 7),(self.dummy_victim,1),(self.dummy_acting_player, 9)])
        
    def test_medicine2(self):
        # In this test both sharer and victim are victims.
        
        # Sharer should have 0 cards in his hand and one in his score pile.
        self.score_cards_by_list(self.dummy_victim, [('Industrialization', 6),('Agriculture',1)])
        
        # Sharer should have 0 cards in his hand and one in his score pile.
        self.score_cards_by_list(self.dummy_sharer, [('Specialization', 9),('Masonry',1)])
        
        # Sharer should have 0 cards in his hand and one in his score pile.
        self.score_cards_by_list(self.dummy_acting_player, [('Gunpowder', 4),('Writing',1)])        
        self.private_setup('Medicine',3)
    
        self.assert_score_by_list([(self.dummy_sharer, 5),(self.dummy_victim,2),(self.dummy_acting_player, 15)])
        
    def test_optics1(self):
        # In this test sharer draws a card without a crown and then transfer 9 points to acting. Acting draws a card with a crown and scores a 4.

        # Giving shareres symbols
        self.meld_cards_by_list(self.dummy_sharer, [('Translation',3)])
        
        # Sharer should have a card to transfer since he's not going to draw a card with a Crown.
        self.score_cards_by_list(self.dummy_sharer, [('Specialization', 9)])
        
        self.private_setup('Optics',3)
        
        self.assert_score_by_list([(self.dummy_sharer, 0),(self.dummy_victim,0),(self.dummy_acting_player, 13 )])
        self.assert_melded(self.dummy_sharer, ['Alchemy'])
        self.assert_melded(self.dummy_acting_player, ['Compass'])
        
    def test_optics2(self):
        # In this test sharer draws a card without a crown but doesn't transfer anything. Acting draws a card with a crown and scores a 4.

        # Giving shareres symbols
        self.meld_cards_by_list(self.dummy_sharer, [('Translation',3)])
        
        # Everyone should have the same points
        self.score_cards_by_list(self.dummy_sharer, [('Agriculture', 1)])
        self.score_cards_by_list(self.dummy_victim, [('Metalworking', 1)])
        self.score_cards_by_list(self.dummy_acting_player, [('Masonry', 1)])
        
        self.private_setup('Optics',3)
        
        self.assert_score_by_list([(self.dummy_sharer, 1),(self.dummy_victim,1),(self.dummy_acting_player, 5)])
        self.assert_melded(self.dummy_sharer, ['Alchemy'])
        self.assert_melded(self.dummy_acting_player, ['Compass'])
     
    def test_paper(self):
        
        # Giving sharer symbols + piles to splay
        self.meld_cards_by_list(self.dummy_sharer, [('Tools',1),('Writing',1),('Oars',1),('Archery',1),('The Wheel',1),('Sailing',1)])
        
        #Splaying red pile left.
        self.dummy_sharer.board[0].change_splay_mode('LEFT')
                
        self.private_setup('Paper',3)
        
        self.assert_splay_mode_by_list([(self.dummy_acting_player, 'Blue', 'none'),(self.dummy_acting_player, 'red', 'none'),(self.dummy_acting_player, 'green', 'none'),(self.dummy_acting_player, 'purple', 'none'),(self.dummy_acting_player, 'yellow', 'none'),(self.dummy_sharer, 'Blue', 'left'),(self.dummy_sharer, 'red', 'left'),(self.dummy_sharer, 'green', 'none'),(self.dummy_sharer, 'purple', 'none'),(self.dummy_sharer, 'yellow', 'none'),(self.dummy_victim, 'Blue', 'none'),(self.dummy_victim, 'yellow', 'none'),(self.dummy_victim, 'green', 'none'),(self.dummy_victim, 'purple', 'none'),(self.dummy_victim, 'red', 'none'),])
        
        self.assert_hand_contains(self.dummy_sharer, ['Anatomy', 'Colonialism'])
        self.assert_hand_size(self.dummy_sharer, 2)
        self.assert_hand_size(self.dummy_acting_player, 1)
     

    def test_translation(self):

        # Giving sharer symbols + piles to splay
        self.meld_cards_by_list(self.dummy_sharer, [('Optics',3)])

        self.score_cards_by_list(self.dummy_sharer, [('City States', 1),('Clothing', 1),('Domestication', 1),('Tools', 1)])
        self.score_cards_by_list(self.dummy_acting_player, [('Oars', 1),('Canal Building', 2),('Sailing', 1),('Enterprise', 4)])
        
    
        self.private_setup('Translation',3)
        
        self.assert_score_by_list([(self.dummy_sharer, 0),(self.dummy_victim,0),(self.dummy_acting_player, 0)])
        self.assert_player_has_achievement(self.dummy_acting_player, 'World')
       
    def test_anatomy1(self):
        # In this dogma, sharer is a victim too. Sharer should only return Clothing and victim should return both Archery and City States.
        self.meld_cards_by_list(self.dummy_sharer, [('Optics',3)])
        self.meld_cards_by_list(self.dummy_victim, [('Archery',1)])
        self.score_cards_by_list(self.dummy_sharer, [('Clothing', 1)])
        self.score_cards_by_list(self.dummy_victim, [('City States', 1)])
        
        self.private_setup('Anatomy',4)
        
        self.assert_score_by_list([(self.dummy_sharer, 0),(self.dummy_victim,0),(self.dummy_acting_player, 0)])
        self.assert_melded(self.dummy_sharer, ['Optics'])
        self.assert_not_melded(self.dummy_victim, ['Archery'])
    '''
    def test_anatomy2(self):
        # In this dogma, sharer is a victim too. Sharer should only return Clothing and victim should return both Archery and City States.
        self.meld_cards_by_list(self.dummy_victim, [('Archery',1)])
        self.score_cards_by_list(self.dummy_sharer, [('Clothing', 1)])

        
        self.private_setup('Anatomy',4)
        
        self.assert_score_by_list([(self.dummy_sharer, 0),(self.dummy_victim,0),(self.dummy_acting_player, 0)])
        self.assert_melded(self.dummy_victim, ['Archery'])        
        
parsing_suite = unittest.TestLoader().loadTestsFromTestCase(TestDeckParsing)
dogma_suite = unittest.TestLoader().loadTestsFromTestCase(TestDogmas)
all_suit = unittest.TestSuite()
all_suit.addTest(parsing_suite)
all_suit.addTest(dogma_suite)
unittest.TextTestRunner(verbosity=2).run(all_suit)
