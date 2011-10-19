
colors_dict = {'RED' : 0, 'BLUE' : 1, 'YELLOW' : 2, 'PURPLE' : 3 , 'GREEN' : 4}

def agriculture0(my_player):
    if my_player.hand.get_size() == 0:
        pass #TODO: in GUI send msg to player.
    else:
        card_to_return = my_player.choose_card_from_hand()                  # Choose a card to return
        from_one_age_higher = card_to_return.age + 1                        # Calculate one age higher
        my_player.thegame.game_deck.return_card(card_to_return)             # Retrun the card
        card_to_score = my_player.thegame.draw(from_one_age_higher)         # Draw a card of one age higher
        my_player.score_card(card_to_score)                                 # And score it.
        
def archery0(my_player , demanding_player):
    my_player.hand.add_to_hand(my_player.draw_card(1))                      # Draw a 1
    max_age = my_player.hand.hand[len(my_player.hand.hand)-1].age           # Calculate max age
    cards_to_choose_from = my_player.hand.get_filtered_hand(lambda card: card.age == max_age)   # Make a list of all the card of maximum age
    chosen_card = my_player.choose_card_from_list(cards_to_choose_from) # Make victim choose a card from them.
    demanding_player.hand.add_to_hand(chosen_card)                               # Move the card to the demanding player's hand
    

def city_states0(my_player , demanding_player):
    if my_player.symbol_count[3] > 3:   
        top_cards_with_castles = []
        for i in range(5):
            top_card = my_player.board[i].get_top_card_reference()
            if top_card != None and 'CASTLE' in top_card.symbols: top_cards_with_castles.append(top_card)
        if len (top_cards_with_castles) == 0: print('No top cards with casles.')
        else:
            chosen_card = my_player.choose_card_from_list(top_cards_with_castles) # This is only a reference to the card to be removed.
            removed_card = my_player.board[colors_dict[chosen_card.color]].transfer_top_card()
            demanding_player.meld_card(removed_card)
            my_player.draw_card(1)
    else:
        print(my_player.get_name() + ' has less then 4 castles')

def clothing0(my_player):
    pass

def clothing1(my_player):
    pass

def code_of_laws0(my_player):
    pass

def domestication0(my_player):
    pass

def masonry0(my_player):
    pass

def metalworking0(my_player):
    pass

def mysticism0(my_player):
    pass

def oars0(my_player , demanding_player):
    pass

def oars1(my_player):
    pass

def pottery0(my_player):
    pass

def pottery1(my_player):
    pass

def sailing0(my_player):
    drawn_card = my_player.draw_card(1)
    my_player.meld_card(drawn_card)

def the_wheel0(my_player):
    my_player.hand.add_to_hand(my_player.draw_card(1))
    my_player.hand.add_to_hand(my_player.draw_card(1))

def tools0(my_player):
    pass

def tools1(my_player):
    pass

def writing0(my_player):
    my_player.hand.add_to_hand(my_player.draw_card(2))

def calendar0(my_player):
    pass

def canal_building0(my_player):
    pass

def currency0(my_player):
    pass

def construction0(my_player , demanding_player):
    pass

def construction1(my_player):
    pass

def fermenting0(my_player):
    pass

def mapmaking0(my_player , demanding_player):
    pass

def mapmaking1(my_player):
    pass

def mathematics0(my_player):
    pass

def monotheism0(my_player , demanding_player):
    pass

def monotheism1(my_player):
    pass

def philosophy0(my_player):
    pass

def philosophy1(my_player):
    pass

def road_building0(my_player):
    pass

def alchemy0(my_player):
    pass

def alchemy1(my_player):
    pass

def education0(my_player):
    pass

def compass0(my_player , demanding_player):
    pass

def engineering0(my_player , demanding_player):
    pass

def engineering1(my_player):
    pass

def feudalism0(my_player , demanding_player):
    pass

def feudalism1(my_player):
    pass

def machinery0(my_player , demanding_player):
    pass

def machinery1(my_player):
    pass

def medicine0(my_player , demanding_player):
    pass

def optics0(my_player):
    pass

def paper0(my_player):
    pass

def paper1(my_player):
    pass

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

