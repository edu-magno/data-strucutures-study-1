import random


def get_players_deck(card_list):
    half_deck = int(len(card_list) / 2)
    deck_len = len(card_list)

    deck_initial = 0
    if len(card_list) % 2 != 0:
        return None

    random.shuffle(card_list)

    player_a = card_list[deck_initial: half_deck]
    player_b = card_list[half_deck: deck_len]
    return (player_a, player_b,)


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
        score = (1, 0)
        return score
    if count_a < count_b:
        score = (0, 1)
        return score

    return score


def play(card_list, score):
    shuffle_cards = get_players_deck(card_list)
    count_win_a = 0
    count_win_b = 0
    deck_player_a = shuffle_cards[0]
    deck_player_b = shuffle_cards[1]

    for card in range(len(deck_player_a)):
        result_of_card_battle = compare_cards(
            deck_player_a[card], deck_player_b[card], (0, 0))
        if result_of_card_battle == (1, 0):
            count_win_a += 1
        if result_of_card_battle == (0, 1):
            count_win_b += 1

    if count_win_a > count_win_b:
        print('Player A Win')
    if count_win_a < count_win_b:
        print('Player B win')
    if count_win_a == count_win_b:
        print('Draw')
    score = (count_win_a, count_win_b)
    return score
