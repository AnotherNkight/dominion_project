from player import *

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