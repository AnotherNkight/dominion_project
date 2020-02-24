from players_in_game import *
from itertools import cycle

#determine random starting player
active_player_index = random.randint(0, len(player_master_list))

for active_player in cycle(player_master_list[active_player_index:] + player_master_list[:active_player_index]):

    #choose player logic & whether human or AI

    if active_player.type == 'big money':
        active_player.big_money(gold, silver, provinces, duchies, estates)

    if active_player.type == 'Smithy - BM':
        active_player.smithy_bm(gold, silver, provinces, duchies, estates, smithy)

    if len(provinces) == 0:
        break


def big_money(gold, silver, provinces, duchies, estates):
    self.turn = self.turn + 1
    ##print("current money: ", self.curr_money)
    if self.curr_money >= 8:
        if len(gold) < 1 and len(silver) < 5:
            ##print("REMAINDER GOLD: ", len(gold), "REMAINDER SILVER: ", len(silver))
            self.buy_card(gold.pop())
            ##print("gold")
            # active player buy gold
        else:
            self.buy_card(provinces.pop())
            ##print("province")
        return gold, provinces, self.discard_list
    # return gold, provinces, self.discard_list

    # active player buy province
    # province - 1
    # turns + 1
    elif 8 > self.curr_money >= 6:
        if len(provinces) <= 4 and len(duchies) > 0:
            ##print("REMAINDER PROVINCE: ", len(provinces))
            self.buy_card(duchies.pop())
            ##print("duchy")
            # active player buy duchy
        else:
            self.buy_card(gold.pop())
           ##print("gold")
            # active player buy gold
        return duchies, gold, self.discard_list
    # return duchies, gold, self.discard_list

    elif self.curr_money == 5:
        if len(provinces) <= 5 and len(duchies) > 0:
            ##print("REMAINDER PROVINCES: ", len(provinces))
            self.buy_card(duchies.pop())
            ##print("duchy")
            # active player buy duchy
        else:
            self.buy_card(silver.pop())
            ##print("silver")
        # active player buy silver
        return duchies, silver, self.discard_list
    # return duchies, silver, self.discard_list

    elif 5 > self.curr_money >= 3:
        if len(provinces) <= 2:
            ##print("REMAINDER PROVINCES: ", len(provinces))
            self.buy_card(estates.pop())
            ##print("Estate")
            # active player buy estate
        else:
            self.buy_card(silver.pop())
            ##print("silver")
        # active player buy silver
        return estates, silver, self.discard_list
    # return estates, silver, self.discard_list

    elif self.curr_money == 2:
        if len(provinces) <= 3:
            ##print("REMAINDER PROVINCES: ", len(provinces))
            self.buy_card(estates.pop())
            ##print("estate")
        #   active player buy estate
        else:
            self.discard()
            ##print("discard")
        return estates, self.curr_hand, self.deck_list, self.discard_list

    else:
        self.discard()
        ##print("discard")

    return self.curr_money, gold, silver, provinces, duchies, self.curr_hand, self.deck_list, self.discard_list

