from itertools import cycle
from board_store import *

def play_game(player_master_list):

    # determine random starting player
    active_player_index = random.randint(0, len(player_master_list))

    for active_player in cycle(player_master_list[active_player_index:] + player_master_list[:active_player_index]):

        #display active player
        print("BEGINNING OF PLAYER ", active_player, "TURN")

        #draw starting hand
        active_player.deck_f()
        print("BEFORE DRAW: ", active_player.curr_hand)
        for i in range(len(active_player.curr_hand)):
            if active_player.curr_hand[i].card_draw != 0:
                print("ADDITIONAL CARD DRAW: ", active_player.curr_hand[i].card_draw)
                active_card = active_player.curr_hand[i]
                active_player.action_card_draw(active_card)
                print("CURRENT HAND SIZE: ", len(active_player.curr_hand))
                break

        print("AFTER DRAW: ", active_player.curr_hand)

        #set current money to 0
        active_player.curr_money = 0

        #count money in current player's hand
        active_player.buy_power()

        print("Current Hand Size: ", len(active_player.curr_hand))
        active_player.strategy(gold, silver, provinces, duchies, estates, smithy)

        print("Provinces remaining at the end of player ", active_player, "'s turn: ", len(provinces))
        print("END OF PLAYER ", active_player, "'S TURN.\n")

        #ends game when province pile runs out
        if len(provinces) == 0:
            break