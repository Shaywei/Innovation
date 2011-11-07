
colors_dict = {'RED' : 0, 'BLUE' : 1, 'YELLOW' : 2, 'PURPLE' : 3 , 'GREEN' : 4}
color_numbers_dict = {0 : 'RED', 1 : 'BLUE' , 2 : 'YELLOW' , 3 : 'PURPLE' , 4 : 'GREEN'}
all_colors = ['RED', 'BLUE', 'YELLOW' , 'PURPLE' , 'GREEN' ]

def claim_special_achievement(player, name):
    if name in player.thegame.available_special_achievements:
        print('\n\n' + player.name + ' claimed: ' + name+ '\n\n')
        player.thegame.available_special_achievements.discard(name)
        player.achievements.add(name)
        player.achievements_number += 1
        player.check_for_victory()

def print_names(list):
    print(str([card.name for card in list]))
    
def players_other_then_me(my_player):
    return [player for player in my_player.thegame.players if player.turn_order_place != my_player.turn_order_place]

def something_happened(my_player):
    ''' This function should be called whenever compensation draw action should be triggered.
        It already makes sure that my_player is a sharer and not initiating player.'''
    if my_player.thegame.is_sharer == True : my_player.thegame.something_happened = True

def choose_card_from_hand(my_player , key=lambda card: True):
    ''' This method recieves a player and a key according which the player will have to choose a card from their hand.
        The method pops the card from the palyer's hand and then returns the card.
        If no cards in hand satisfy conditions in key, returns None'''
    cards_to_choose_from = my_player.hand.get_filtered_hand(key)   # Make a list of all the card satisfying key conditions
    if cards_to_choose_from == []: return None
    chosen_card_reference = my_player.choose_card_from_list(cards_to_choose_from) # Take player choice
    chosen_card = my_player.hand.remove_by_name(chosen_card_reference.name)
    return chosen_card

def choose_card_from_top_cards(player_to_choose_from, choosing_player , key=lambda card: True):
    ''' This method recieves two players and a key according which the choosing player will have to choose a card from their hand.
        The method pops the card from the player to choose from board (a top card) and then returns the card.
        If no cards in hand satisfy conditions in key, returns None'''
    cards_to_choose_from = []
    for i in range(5):
        top_card = player_to_choose_from.board[i].top_card
        if top_card is not None and key(top_card): cards_to_choose_from.append(top_card)
        if top_card is not None and key(top_card): cards_to_choose_from.append(top_card)
    if cards_to_choose_from == []: return None
    chosen_card_reference = choosing_player.choose_card_from_list(cards_to_choose_from) # Take player choice
    chosen_card = player_to_choose_from.board[colors_dict[chosen_card_reference.color]].transfer_top_card()
    return chosen_card



def choose_color_from_list(my_player, key=lambda pile: True):
    ''' This method recieves a player and a key according which the player will have to choose a pile of certain color.
        The method compiles a list according to the key and gets the choice from the player, returning string of said color.
        If no cards in hand satisfy conditions in key, returns None'''
    colors_to_choose_from = []
    for i in range(5):
        if key(my_player.board[i].pile): colors_to_choose_from.append(color_numbers_dict[i])
    if colors_to_choose_from == []: return None
    return my_player.choose_color_from_list(colors_to_choose_from)

def choose_card_from_score_pile(my_player , key=lambda card: True):
    ''' This method recieves a player and a key according which the player will have to choose a card from their score pile.
        The method pops the card from the palyer's score pile and then returns the card.
        If no cards in hand satisfy conditions in key, returns None'''
    # Make a list of all the card satisfying key conditions
    cards_to_choose_from = my_player.score_pile.get_filtered_score_pile(key)

    if cards_to_choose_from == []: return None

    chosen_card_reference = my_player.choose_card_from_list(cards_to_choose_from) # Take player choice
    chosen_card = my_player.score_pile.remove_by_name(chosen_card_reference.name)
    return chosen_card

def splay_color(my_player, color, splay_mode):
    ''' This method recieves a player, a color and a splay mode and if legal it splays
        the pile of that color for that player to the new splay mode.
        UPDATES SOMETHING HAPPNED!'''
    if len(my_player.board[colors_dict[color]].pile) > 1:
        my_player.board[colors_dict[color]].change_splay_mode(splay_mode)
        something_happened(my_player)

def splay_color_with_choice(my_player, colors, splay_mode):
    ''' This method recieves a player, a list of colors and a splay mode and if legal it splays
        the pile of the color chosen fomr the list to the new splay mode. for said player.
        UPDATES SOMETHING HAPPNED!'''
    color_chosen = choose_color_from_list(my_player, lambda pile: len(pile) > 1 and pile[0].color in colors)
    if color_chosen is not None:
        my_player.board[colors_dict[color_chosen]].change_splay_mode(splay_mode)
        something_happened(my_player)

def choose_up_to_n_cards_from_hand(my_player, n , key=lambda card: True):
    ''' This method recieves a player, a number 'n' and a key.
        It allows the player to choose from his hand up to 'n' cards that satisfy condition in key.
        If 'n' is -1, there is no (practical) limit on the cards
        The method returns a list of all chosen cards or None if the list is empty.'''
    list_of_chosen_cards = []
    cards_to_choose_from = my_player.hand.get_filtered_hand(key)   # Make a list of all the card satisfying key conditions
    done = False
    count = 0
    if n == -1: count = -200
    while cards_to_choose_from != [] and not done and count < n:\
        #TODO: GUI.
        valid_choices = my_player.ui.make_valid_choices_from_int(len(cards_to_choose_from))
        valid_choices = [str(num) for num in valid_choices]
        valid_choices.append('done')
        my_player.ui.print_card_list(cards_to_choose_from)
        choice = my_player.ui.str_prompt('Choose a card from the list for dogma effect or \'done\' to finish', valid_choices)
        if choice == 'done': done = True
        else:
            choice = int(choice) - 1
            chosen_card = my_player.hand.remove_by_name(cards_to_choose_from[choice].name)
            list_of_chosen_cards.append(chosen_card)
            count += 1
            cards_to_choose_from = my_player.hand.get_filtered_hand(key)
    return list_of_chosen_cards

def different_ages_in_list(list):
    return len(set([card.age for card in list]))

def draw_and_meld_a(my_player, age, return_flag = False):
    ''' This method is self explenatory except for the fact that you can call it with a True flag
        and then it will return a reference for the draw card. This is useful for chekcing condition on the returned card.'''
    drawn_card = my_player.draw_card(age)
    my_player.meld_card(drawn_card)
    if return_flag == True: return drawn_card

def draw_and_tuck_a(my_player, age):
    drawn_card = my_player.draw_card(age)
    my_player.tuck_card(drawn_card)

def draw_and_score_a(my_player, age):
    drawn_card = my_player.draw_card(age)
    my_player.score_card_by_card(drawn_card)

def agriculture0(my_player):
    print_names(my_player.hand.hand)
    print('Hand size is: ' + str(my_player.hand.hand_size))
    print('Hand length is: ' + str(len(my_player.hand.hand)))
    if my_player.hand.get_size() == 0:
        pass #TODO: in GUI send msg to player.
    else:
        card_to_return = my_player.choose_card_from_hand()                  # Choose a card to return
        from_one_age_higher = card_to_return.age + 1                        # Calculate one age higher
        my_player.thegame.game_deck.return_card(card_to_return)             # Retrun the card
        my_player.score_card_by_age(from_one_age_higher)                    # And score it.
        something_happened(my_player)

def archery0(my_player , demanding_player):
    my_player.add_card_to_hand(my_player.draw_card(1))                      # Draw a 1
    max_age = my_player.hand.hand[len(my_player.hand.hand)-1].age           # Calculate max age
    chosen_card = choose_card_from_hand(my_player , lambda card: card.age == max_age)
    demanding_player.hand.add_to_hand(chosen_card)                               # Move the card to the demanding player's hand

def city_states0(my_player , demanding_player):
    if my_player.symbol_count[3] > 3:               # Has at least 4 castles on board.
        top_cards_with_castles = []
        for i in range(5):
            top_card = my_player.board[i].get_top_card_reference()
            if top_card != None and 'CASTLE' in top_card.symbols: top_cards_with_castles.append(top_card)
        if len (top_cards_with_castles) == 0: print('No top cards with casles.')
        else:
            print_names (top_cards_with_castles) # Debug
            chosen_card_reference = my_player.choose_card_from_list(top_cards_with_castles) # This is only a reference to the card to be removed.
            chosen_card = my_player.board[colors_dict[chosen_card_reference.color]].transfer_top_card()
            demanding_player.meld_card(chosen_card)
            my_player.draw_card(1)
    else:
        # TODO: GUI
        print(my_player.get_name() + ' has less then 4 castles')

def clothing0(my_player):
    cards_in_hand_of_different_color_from_cards_on_baord = []
    for i in range(5):
        if my_player.board[i].top_card is None:
            cards_in_hand_of_this_color = my_player.hand.get_filtered_hand(lambda card: card.color == color_numbers_dict[i])
            cards_in_hand_of_different_color_from_cards_on_baord.extend(cards_in_hand_of_this_color)
    if cards_in_hand_of_different_color_from_cards_on_baord != []:
        chosen_card = my_player.choose_card_from_list(cards_in_hand_of_different_color_from_cards_on_baord)
        my_player.meld_card(chosen_card)
        something_happened(my_player)

def clothing1(my_player):
    players = my_player.thegame.players
    #TODO : Name is not a good ID!!!
    visibility_matrix = [0,0,0,0,0]
    for i in range(5):
        for player in players_other_then_me(my_player):
            if len(player.board[i].pile) != 0:
                visibility_matrix[i] = 1
        if visibility_matrix[i] == 0 and len(my_player.board[i].pile) != 0:
            my_player.score_card_by_age(1)
            something_happened(my_player)

def code_of_laws0(my_player):
    cards_in_hand_of_same_color_as_a_color_on_board = []
    for i in range(5):
        if len(my_player.board[i].pile) != 0:
            cards_in_hand_of_this_color = my_player.hand.get_filtered_hand(lambda card: card.color == color_numbers_dict[i])
            cards_in_hand_of_same_color_as_a_color_on_board.extend(cards_in_hand_of_this_color)
    if cards_in_hand_of_same_color_as_a_color_on_board != []:
        chosen_card_reference = my_player.choose_card_from_list(cards_in_hand_of_same_color_as_a_color_on_board)
        color = chosen_card_reference.color
        chosen_card = my_player.hand.remove_by_name(chosen_card_reference.name)
        my_player.board[colors_dict[color]].tuck(chosen_card)
        my_player.board[colors_dict[color]].change_splay_mode('Left')
        something_happened(my_player)

def domestication0(my_player):
    something_happened(my_player)
    if my_player.hand.hand_size == 0:
        my_player.hand.add_to_hand(my_player.draw_card(1))
    else:
        min_age = my_player.hand.hand[0].age           # Calculate min age
        chosen_card = choose_card_from_hand(my_player , lambda card: card.age == min_age)
        my_player.meld_card(chosen_card)
        my_player.hand.add_to_hand(my_player.draw_card(1))

def masonry0(my_player):
    cards_with_castles = choose_up_to_n_cards_from_hand(my_player, -1, lambda card: 'CASTLE' in card.symbols)
    num_of_cards_chosen = len(cards_with_castles)
    if num_of_cards_chosen > 0:
        for card in cards_with_castles: my_player.meld_card(card)
        something_happened(my_player)
        if num_of_cards_chosen > 3: claim_special_achievement(my_player,'Monument')

def metalworking0(my_player):
    something_happened(my_player)
    exit_conditions = False
    while not exit_conditions:
        drawn_card = my_player.draw_card(1)
        #TODO: GUI (should reveal card)
        drawn_card.print_self()
        if 'CASTLE' in drawn_card.symbols: my_player.score_card_by_card(drawn_card)
        else:
            my_player.add_card_to_hand(drawn_card)
            exit_conditions = True

def mysticism0(my_player):
    something_happened(my_player)
    drawn_card = my_player.draw_card(1)
    color = drawn_card.color
    if len(my_player.board[colors_dict[color]].pile) != 0: my_player.meld_card(drawn_card)
    else: my_player.add_card_to_hand(drawn_card)

def oars0(my_player , demanding_player):
    chosen_card = choose_card_from_hand(my_player, lambda card: "CROWN" in card.symbols)
    if chosen_card is not None:
        demanding_player.score_card_by_card(chosen_card)
        my_player.add_card_to_hand(my_player.draw_card(1))                      # Draw a 1
        my_player.thegame.dogma_data = True # A card was transferred.

def oars1(my_player):
    if my_player.thegame.dogma_data is None:
        my_player.add_card_to_hand(my_player.draw_card(1)) # Draw a 1
        something_happened(my_player)

def pottery0(my_player):
    cards_to_return = choose_up_to_n_cards_from_hand(my_player, 3, lambda card: True)
    age_of_card_to_score = len(cards_to_return)
    if age_of_card_to_score != 0:
        for card in cards_to_return: my_player.return_card(card)
        my_player.score_card_by_age(age_of_card_to_score)
        something_happened(my_player)

def pottery1(my_player):
    my_player.add_card_to_hand(my_player.draw_card(1))
    something_happened(my_player)

def sailing0(my_player):
    drawn_card = my_player.draw_card(1)
    my_player.meld_card(drawn_card)
    something_happened(my_player)

def the_wheel0(my_player):
    my_player.hand.add_to_hand(my_player.draw_card(1))
    my_player.hand.add_to_hand(my_player.draw_card(1))
    something_happened(my_player)

def tools0(my_player):
    if my_player.hand.hand_size > 2:
        cards_to_return = []
        for i in range(3):
            cards_to_return.append(choose_card_from_hand(my_player, lambda card: True))
        for card in cards_to_return: my_player.return_card(card)
        draw_and_meld_a(my_player, 3)
        something_happened(my_player)

def tools1(my_player):
    chosen_card = choose_card_from_hand(my_player, lambda card: card.age == 3)
    if chosen_card is not None:
        something_happened(my_player)
        my_player.return_card(chosen_card)
        for i in range(3):
            my_player.hand.add_to_hand(my_player.draw_card(1))

def writing0(my_player):
    my_player.hand.add_to_hand(my_player.draw_card(2))
    something_happened(my_player)

def calendar0(my_player):
    if len(my_player.score_pile.score_pile) > my_player.hand.hand_size:
        my_player.draw_to_hand(3)
        my_player.draw_to_hand(3)
        something_happened(my_player)

def canal_building0(my_player):
    if my_player.hand.hand_size > 0:
        max_age_in_hand = my_player.hand.hand[len(my_player.hand.hand)-1].age
        cards_of_highest_age_in_hand = my_player.hand.get_filtered_hand(lambda card: card.age == max_age_in_hand)
    else:
        cards_of_highest_age_in_hand = []
    if my_player.score_pile.score_pile_size > 0:
        cards_of_highest_age_in_score_pile = my_player.score_pile.get_filtered_score_pile(lambda card: card.age == my_player.score_pile.max_age_in_score_pile)
    else:
        cards_of_highest_age_in_score_pile = []
    for card_name in [card.name for card in cards_of_highest_age_in_hand]:
        card = my_player.hand.remove_by_name(card_name)
        my_player.score_card_by_card(card)
        something_happened(my_player)
    for card_name in [card.name for card in cards_of_highest_age_in_score_pile]:
        card = my_player.score_pile.remove_by_name(card_name)
        my_player.add_card_to_hand(card)
        something_happened(my_player)

def currency0(my_player):
    cards_chosen_to_return = choose_up_to_n_cards_from_hand(my_player, -1, (lambda card: True))
    count_of_different_ages_returned = different_ages_in_list(cards_chosen_to_return)
    for i in range(count_of_different_ages_returned):
        my_player.score_card_by_age(2)
        something_happened(my_player)

def construction0(my_player , demanding_player):
    for i in range(2):
        chosen_card = choose_card_from_hand(my_player)
        if chosen_card is not None: demanding_player.add_card_to_hand(chosen_card)

def construction1(my_player):
    num_of_top_cards = 0
    other_players_have_five_top_cards = False
    for i in range(5):
        if my_player.board[i].top_card is not None: num_of_top_cards += 1
    if num_of_top_cards == 5:
        for player in players_other_then_me(my_player):
            count = 0
            for i in range(5):
                if player.board[i].top_card is not None: count += 1
            if count == 5: other_players_have_five_top_cards = True
        if not other_players_have_five_top_cards: claim_special_achievement(my_player, 'Empire')
        something_happened(my_player)

def fermenting0(my_player):
    something_happened(my_player)
    num_of_leaves = my_player.symbol_count[1]
    num_of_cards_to_draw = num_of_leaves//2
    for i in range(num_of_cards_to_draw):
        my_player.draw_to_hand(2)

def mapmaking0(my_player , demanding_player):
    chosen_card = choose_card_from_score_pile(my_player, lambda card: card.age == 1)
    if chosen_card is not None:
        demanding_player.score_card_by_card(chosen_card)
        my_player.thegame.dogma_data = True

def mapmaking1(my_player):
    if my_player.thegame.dogma_data == True:
        my_player.score_card_by_age(1)

def mathematics0(my_player):
    chosen_card = choose_card_from_hand(my_player)
    if chosen_card is not None:
        age_of_chosen_card = chosen_card.age
        my_player.return_card(chosen_card)
        drawn_card = my_player.draw_card(age_of_chosen_card +1)
        my_player.meld_card(drawn_card)
        something_happened(my_player)

def monotheism0(my_player , demanding_player):
    top_cards_to_choose_from = []
    for i in range(5):
        victim_player_top_card = my_player.board[i].top_card
        demanding_player_top_card = demanding_player.board[i].top_card
        if demanding_player_top_card is None and victim_player_top_card is not None:
            top_cards_to_choose_from.append(victim_player_top_card)
    if top_cards_to_choose_from != []:
        top_cards_to_choose_from.sort()
        top_card_to_transfer_reference = my_player.choose_card_from_list(top_cards_to_choose_from)
        color = top_card_to_transfer_reference.color
        top_card_to_transfer = my_player.board[colors_dict[color]].transfer_top_card()
        demanding_player.score_card_by_card(top_card_to_transfer)
        draw_and_tuck_a(my_player, 1)

def monotheism1(my_player):
    something_happened(my_player)
    draw_and_tuck_a(my_player, 1)

def philosophy0(my_player):
    splay_color_with_choice(my_player, all_colors, 'LEFT')

def philosophy1(my_player):
    card_to_score = choose_card_from_hand(my_player)
    if card_to_score is not None:
        my_player.score_card_by_card(card_to_score)
        something_happened(my_player)

def road_building0(my_player):
    # TODO: GUI.
    if my_player.hand.hand_size != 0:
        something_happened(my_player)
        cards_to_meld = []
        while cards_to_meld == []: cards_to_meld = choose_up_to_n_cards_from_hand(my_player, 2)
        for card in cards_to_meld: my_player.meld_card(card)
        if len(cards_to_meld) == 2:
            chosen_player = my_player.choose_player_from_list(lambda player: player.turn_order_place != my_player.turn_order_place)
            assert chosen_player is not None, 'No player was selcted, recieved None.'
            print (chosen_player.name.upper())
            chosen_player_top_green_card = chosen_player.board[4].transfer_top_card()
            if chosen_player_top_green_card is not None: my_player.meld_card(chosen_player_top_green_card)
            my_top_red_card = my_player.board[0].transfer_top_card()
            if my_top_red_card is not None: chosen_player.meld_card(my_top_red_card)

def alchemy0(my_player):
    something_happened(my_player)
    num_of_cards_to_reveal = my_player.symbol_count[3] // 3
    revealed_cards = []
    revealed_red = False
    for i in range(num_of_cards_to_reveal):
        revealed_card = my_player.thegame.reveal(4)
        if revealed_card.color.upper() == 'RED': revealed_red = True
        revealed_cards.append(revealed_card)
    if revealed_red:
        for card in revealed_cards:
            my_player.thegame.return_card(card)
        for i in range(len(my_player.hand.hand)):
            my_player.thegame.return_card(my_player.hand.remove_by_index(i))
    else:
        for card in revealed_cards:
            my_player.hand.add_to_hand(card)

def alchemy1(my_player):
    my_player.meld_action()
    my_player.score_card_from_hand()

def compass0(my_player , demanding_player):
    victim_card_to_transfer = choose_card_from_top_cards(my_player, my_player, lambda card: card.color != "GREEN" and "LEAF" in card.symbols)
    if victim_card_to_transfer is not None: demanding_player.meld_card(victim_card_to_transfer)
    demanding_player_card_to_transfer = choose_card_from_top_cards(demanding_player, my_player, lambda card: "LEAF" not in card.symbols)
    if demanding_player_card_to_transfer is not None: my_player.meld_card(demanding_player_card_to_transfer)

def education0(my_player):
    if len(my_player.score_pile.score_pile) > 0:
        card_to_return = choose_card_from_score_pile(my_player, lambda card: card.age == my_player.score_pile.max_age_in_score_pile)
        age_to_draw = my_player.score_pile.max_age_in_score_pile + 2
        my_player.thegame.return_card(card_to_return)
        my_player.draw_to_hand(age_to_draw)
        something_happened(my_player)


def engineering0(my_player , demanding_player):
    for i in range(5):
        top_card= my_player.board[i].top_card
        if top_card is not None and 'CASTLE' in top_card.symbols:
            top_card = my_player.board[i].transfer_top_card()
            demanding_player.score_card_by_card(top_card)

def engineering1(my_player):
    splay_color(my_player, 'RED' , 'LEFT')

def feudalism0(my_player , demanding_player):
    card_to_transfer = choose_card_from_hand(my_player, lambda card: 'CASTLE' in card.symbols)
    if card_to_transfer is not None: demanding_player.add_card_to_hand(card_to_transfer)

def feudalism1(my_player):
    splay_color_with_choice(my_player, ['YELLOW', 'PURPLE'], 'LEFT')

def machinery0(my_player , demanding_player):
    highest_age = demanding_player.hand.max_age
    highest_cards = demanding_player.hand.pop_filtered_hand(lambda card: card.age == highest_age)
    victims_cards = my_player.hand.pop_filtered_hand(lambda card: True)
    for card in victims_cards:
        demanding_player.add_card_to_hand(card)
    for card in highest_cards:
        my_player.add_card_to_hand(card)


def machinery1(my_player):
    card_to_score = choose_card_from_hand(my_player, lambda card: 'CASTLE' in card.symbols)
    if card_to_score is not None:
        my_player.score_card_by_card(card_to_score)
        something_happened(my_player)
    splay_color(my_player, 'RED', 'LEFT')

def medicine0(my_player , demanding_player):
    victim_highest_age = my_player.score_pile.max_age_in_score_pile
    victim_card = choose_card_from_score_pile(my_player , key=lambda card: card.age == victim_highest_age)
    demander_lowest_age = demanding_player.score_pile.min_age_in_score_pile
    demander_card = choose_card_from_score_pile(demanding_player , key=lambda card: card.age == demander_lowest_age)
    if victim_card is not None: demanding_player.score_card_by_card(victim_card)
    if demander_card is not None: my_player.score_card_by_card(demander_card)

def optics0(my_player):
    melded_card = draw_and_meld_a(my_player, 3,return_flag = True)
    if 'CROWN' in melded_card.symbols: 
        draw_and_score_a(my_player,4)
    else:
        lowest_score_for_other_players = min([player.score_pile.score for player in players_other_then_me(my_player)])
        if my_player.score_pile.score > lowest_score_for_other_players:
            player_to_move_to = my_player.choose_player_from_list(lambda player: player.turn_order_place != my_player.turn_order_place and player.score_pile.score == lowest_score_for_other_players)
            if player_to_move_to is not None:
                card_to_move = choose_card_from_score_pile(my_player)
                player_to_move_to.score_card_by_card(card_to_move)
    something_happened(my_player)

def paper0(my_player):
    splay_color_with_choice(my_player, ['BLUE', 'GREEN'], 'LEFT')

def paper1(my_player):
    num_of_cards_to_draw = 0
    for i in range(5): 
        if my_player.board[i].splay_mode == 'LEFT': num_of_cards_to_draw += 1
    for i in range(num_of_cards_to_draw):
        my_player.draw_to_hand(4)
    

def translation0(my_player):
    pass

def translation1(my_player):
    pass

def anatomy0(my_player , demanding_player):
    pass

def colonialism0(my_player):
    pass

def enterprise0(my_player , demanding_player):
    pass

def enterprise1(my_player):
    pass

def experimentation0(my_player):
    pass

def gunpowder0(my_player , demanding_player):
    pass

def gunpowder1(my_player):
    pass

def invention0(my_player):
    pass

def invention1(my_player):
    pass

def navigation0(my_player , demanding_player):
    pass

def perspective0(my_player):
    pass

def printing_press0(my_player):
    pass

def printing_press1(my_player):
    pass

def reformation0(my_player):
    pass

def reformation1(my_player):
    pass

def astronomy0(my_player):
    pass

def astronomy1(my_player):
    pass

def banking0(my_player , demanding_player):
    pass

def banking1(my_player):
    pass

def chemistry0(my_player):
    pass

def chemistry1(my_player):
    pass

def coal0(my_player):
    pass

def coal1(my_player):
    pass

def coal2(my_player):
    pass

def measurement0(my_player):
    pass

def physics0(my_player):
    pass

def societies0(my_player , demanding_player):
    pass

def statistics0(my_player , demanding_player):
    pass

def statistics1(my_player):
    pass

def steam_engine0(my_player):
    pass

def the_pirate_code0(my_player , demanding_player):
    pass

def the_pirate_code1(my_player):
    pass

def atomic_theory0(my_player):
    pass

def atomic_theory1(my_player):
    pass

def canning0(my_player):
    pass

def canning1(my_player):
    pass

def classification0(my_player):
    pass

def democracy0(my_player):
    pass

def emancipation0(my_player , demanding_player):
    pass

def emancipation1(my_player):
    pass

def encyclopedia0(my_player):
    pass

def industrialization0(my_player):
    pass

def industrialization1(my_player):
    pass

def machine_tools0(my_player):
    pass

def metric_system0(my_player):
    pass

def metric_system1(my_player):
    pass

def vaccination0(my_player , demanding_player):
    pass

def vaccination1(my_player):
    pass

def bicycle0(my_player):
    pass

def combustion0(my_player , demanding_player):
    pass

def electricity0(my_player):
    pass

def evolution0(my_player):
    pass

def explosives0(my_player , demanding_player):
    pass

def lighting0(my_player):
    pass

def publications0(my_player):
    pass

def publications1(my_player):
    pass

def railroad0(my_player):
    pass

def railroad1(my_player):
    pass

def refrigeration0(my_player , demanding_player):
    pass

def refrigeration1(my_player):
    pass

def sanitation0(my_player , demanding_player):
    pass

def antibiotics0(my_player):
    pass

def corporations0(my_player , demanding_player):
    pass

def corporations1(my_player):
    pass

def empiricism0(my_player):
    pass

def empiricism1(my_player):
    pass

def flight0(my_player):
    pass

def flight1(my_player):
    pass

def mass_media0(my_player):
    pass

def mass_media1(my_player):
    pass

def mobility0(my_player , demanding_player):
    pass

def quantum_theory0(my_player):
    pass

def rocketry0(my_player):
    pass

def skyscrapers0(my_player , demanding_player):
    pass

def socialism0(my_player):
    pass

def collaboration0(my_player , demanding_player):
    pass

def collaboration1(my_player):
    pass

def composites0(my_player , demanding_player):
    pass

def computers0(my_player):
    pass

def computers1(my_player):
    pass

def ecology0(my_player):
    pass

def fission0(my_player , demanding_player):
    pass

def fission1(my_player):
    pass

def genetics0(my_player):
    pass

def satellites0(my_player):
    pass

def satellites1(my_player):
    pass

def satellites2(my_player):
    pass

def services0(my_player , demanding_player):
    pass

def specialization0(my_player):
    pass

def specialization1(my_player):
    pass

def suburbia0(my_player):
    pass

def ai0(my_player):
    pass

def ai1(my_player):
    pass

def bioengineering0(my_player):
    pass

def bioengineering1(my_player):
    pass

def databases0(my_player , demanding_player):
    pass

def globalization0(my_player , demanding_player):
    pass

def globalization1(my_player):
    pass

def miniaturization0(my_player):
    pass

def robotics0(my_player):
    pass

def self_service0(my_player):
    pass

def self_service1(my_player):
    pass

def software0(my_player):
    pass

def software1(my_player):
    pass

def stem_cells0(my_player):
    pass

def the_internet0(my_player):
    pass

def the_internet1(my_player):
    pass

def the_internet2(my_player):
    pass

