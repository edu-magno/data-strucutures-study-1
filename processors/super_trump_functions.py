from superheros import SUPER_HEROS
import random

def get_players_deck(card_list):
    half_deck = int(len(card_list) / 2)
    deck_len = len(card_list) 
    
    deck_initial = 0
    if len(card_list) % 2 != 0:
        return None
    
    random.shuffle(card_list)
    
    print(half_deck)
    player_a = card_list[deck_initial: half_deck]
    player_b = card_list[half_deck: deck_len ]
    return (player_a, player_b,)



def compare_cards(card_of_player_a, card_of_player_b, score):
    pass

def play(card_list, score):
    pass