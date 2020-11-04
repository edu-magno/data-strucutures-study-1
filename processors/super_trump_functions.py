from superheros import SUPER_HEROS
import random

def get_players_deck(card_list):
    half_deck = int(len(card_list) / 2)
    deck_len = len(card_list) 
    
    deck_initial = 0
    if len(card_list) % 2 != 0:
        return None
    
    random.shuffle(card_list)
    
    player_a = card_list[deck_initial: half_deck]
    player_b = card_list[half_deck: deck_len ]
    return (player_a, player_b,)

t = get_players_deck(SUPER_HEROS)
a = t[0]
b = t[1]


def compare_cards(card_of_player_a, card_of_player_b, score):
    count_a = 0
    count_b = 0

    name_card_a = card_of_player_a.get('name')
    name_card_b = card_of_player_b.get('name')
    

    for (key_a, value_a), (key_b, value_b) in zip(card_of_player_a.items(), card_of_player_b.items()):
        
        if key_a != 'name' and key_b != 'name':
            if value_a > value_b:
                print(f'{name_card_a} have more {key_a}')
                count_a += 1
            if value_a < value_b:
                print(f'{name_card_b} have more {key_b}')
                count_b += 1
            if value_a == value_b:
                print(f'{name_card_a} and {name_card_b} have the same {key_a}')
                continue
    # for x in range(len(card_of_player_a)):
        
    if count_a > count_b:
        score = (1,0)
        return score
    if count_a < count_b:
        score = (0,1)
        return score
    
    return score

compare = compare_cards({'name': 'dr. strange', 'intelligence': 11, 'power': 10, 'strenght': 6, 'agility': 5, 'vitality': 8},{'name': 'beast', 'intelligence': 10, 'power': 9, 'strenght': 6, 'agility': 5, 'vitality': 10},(0,0))
print(compare)
def play(card_list, score):
    pass