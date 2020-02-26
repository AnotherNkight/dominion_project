# from player import *
# from itertools import cycle
# from strategies import *
from play_game import *

'''
DONE
Fairly rotates between players with randomized 'start' player
Accurately calculates score for multiple players
Keeps track of which player purchased provinces on which turn and who won the game in external .txt file
player 'type' allows specification of which strategy player should use
Implemented Smithy Big Money strategy variation
Analysis of which turns provinces were purchased on
Human Player Strategy

ERRORS


ADD
Analysis of which turns provinces were purchased on
Human Player incorrect input checking
'''

#Record that it's a new game
with open("province_tracker.txt", "a") as f:
    f.write("\nNEW GAME \n\n")

#execute game
play_game(player_master_list)

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