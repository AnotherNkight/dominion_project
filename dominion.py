import random
from player_turn import *
from itertools import cycle

'''
DONE
Fairly rotates between players with randomized 'start' player
Accurately calculates score for multiple players
Keeps track of which player purchased provinces on which turn and who won the game in external .txt file
player 'type' allows specification of which strategy player should use
Implemented Smithy Big Money strategy variation

ERRORS
Hand sizes on player for SBM may not always be accurate?

ADD
Analysis of which turns provinces were purchased on
Human Player UI
'''

#Record that it's a new game
with open("province_tracker.txt", "a") as f:
    f.write("\nNEW GAME \n\n")


player_master_list = []
'''
player_1 = Player('1', 0, 'big money')
player_master_list.append(player_1)
'''
player_2 = Player('2', 0, 'big money')
player_master_list.append(player_2)

player_3 = Player('3', 0, 'Smithy - BM')
player_master_list.append(player_3)

#after all players have been added to master list. Used to find winner
winner_list = player_master_list.copy()

# board supply
number_of_provinces = 12
number_of_duchies = 12
number_of_estates = 21          #(24 - 3)
number_of_gold = 30
number_of_silver = 40
number_of_copper = 53           #(60 - 7)
number_of_smithies = 20         #check actual number

#store board stockpiles as lists
provinces = [Province() for i in range(number_of_provinces)]
duchies = [Duchy() for i in range(number_of_duchies)]
estates = [Estate() for i in range(number_of_estates)]
gold = [Gold() for i in range(number_of_gold)]
silver = [Silver() for i in range(number_of_silver)]
copper = [Copper() for i in range(number_of_copper)]
smithy = [Smithy() for i in range(number_of_smithies)]

#determine random starting player
active_player_index = random.randint(0, len(player_master_list))

for active_player in cycle(player_master_list[active_player_index:] + player_master_list[:active_player_index]):

    #display active player
    print("BEGINNING OF PLAYER ", active_player, "TURN")

    #draw starting hand
    active_player.deck_f()
    for i in range(len(active_player.curr_hand)):
        if active_player.curr_hand[i].card_draw != 0:
            active_card = active_player.curr_hand[i]
            active_player.action_card_draw(active_card)
            break

    #set current money to 0
    active_player.curr_money = 0

    #count money in current player's hand
    active_player.buy_power()

    print("Current Hand Size: ", len(active_player.curr_hand))

    #choose player logic & whether human or AI

    if active_player.type == 'big money':
        active_player.big_money(gold, silver, provinces, duchies, estates)

    if active_player.type == 'Smithy - BM':
        active_player.smithy_bm(gold, silver, provinces, duchies, estates, smithy)


    print("Provinces remaining at the end of player ", active_player, "'s turn: ", len(provinces))
    print("END OF PLAYER ", active_player, "'S TURN.\n")

    if len(provinces) == 0:
        break

#find winner for more than 2 player game
for i in range(len(winner_list)):
    for j in range(0, (len(winner_list)) - i - 1):
        if winner_list[j].player_score() > winner_list[j+1].player_score():
            winner_list[j], winner_list[j + 1] = winner_list[j + 1], winner_list[j]
        winner_list[j].points = 0
        winner_list[j + 1].points = 0
print("The game is over. The final points are: \n")
for i in range(len(winner_list)):
    print("Player ", winner_list[i], " with ", winner_list[i].player_score(), "points\n")
    winner_list[i].points = 0

#update final score and winner to .txt file
with open("province_tracker.txt", "a") as f:
    for i in range(len(winner_list)):
        f.write("Player " + str(winner_list[i]) + " with " + str(winner_list[i].player_score()) + " points\n")