from strategies import *

#add player objects for players participating in game to this file.

player_master_list = []
'''
player_1 = Player('1', 0, 'big money')
player_master_list.append(player_1)
'''
player_2 = big_money('2')
player_master_list.append(player_2)

player_3 = smithy_big_money('3')
player_master_list.append(player_3)

player_4 = user('4')
player_master_list.append(player_4)

#after all players have been added to master list. Used to find winner
winner_list = player_master_list.copy()