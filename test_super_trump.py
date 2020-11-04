from processors.super_trump_functions import *
from processors.superheros import SUPER_HEROS


def test_get_players_deck():
    result = get_players_deck(SUPER_HEROS)

    expected_len_of_result = 2
    expetect_len_of_deck = 8

    assert expected_len_of_result == len(result)
    assert expetect_len_of_deck == len(result[0])
    assert expetect_len_of_deck == len(result[1])


def test_compare_cards():
    card_of_player_a = {'name': 'the thing',
                        'intelligence': 3,
                        'power': 6,
                        'strenght': 10,
                        'agility': 2,
                        'vitality': 10}

    card_of_player_b = {'name': 'super man',
                        'intelligence': 7,
                        'power': 10,
                        'strenght': 10,
                        'agility': 10,
                        'vitality': 10}

    result = compare_cards(card_of_player_a, card_of_player_b, (0, 0))
    expected = (0, 1)

    assert expected == result


def test_play():
    result = play(SUPER_HEROS, (0, 0))
    expected_len_of_result = 2

    assert expected_len_of_result == len(result)
