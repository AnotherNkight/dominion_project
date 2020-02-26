from player import *
from board_store import *

class big_money(Player):
    def __init__(self, id):
        Player.__init__(self, id, 0, "big money")
        #self.id

    def strategy(self, gold, silver, provinces, duchies, estates, smithy):
        self.turn = self.turn + 1
        print("current money: ", self.curr_money)
        if self.curr_money >= 8:
            if len(gold) < 1 and len(silver) < 5:
                print("REMAINDER GOLD: ", len(gold), "REMAINDER SILVER: ", len(silver))
                self.buy_card(gold.pop())
                print("gold")
                # active player buy gold
            else:
                self.buy_card(provinces.pop())
                print("province")
            return gold, provinces, self.discard_list
        # return gold, provinces, self.discard_list

        # active player buy province
        # province - 1
        # turns + 1
        elif 8 > self.curr_money >= 6:
            if len(provinces) <= 4 and len(duchies) > 0:
                print("REMAINDER PROVINCE: ", len(provinces))
                self.buy_card(duchies.pop())
                print("duchy")
                # active player buy duchy
            else:
                self.buy_card(gold.pop())
                print("gold")
                # active player buy gold
            return duchies, gold, self.discard_list
        # return duchies, gold, self.discard_list

        elif self.curr_money == 5:
            if len(provinces) <= 5 and len(duchies) > 0:
                print("REMAINDER PROVINCES: ", len(provinces))
                self.buy_card(duchies.pop())
                print("duchy")
                # active player buy duchy
            else:
                self.buy_card(silver.pop())
                print("silver")
            # active player buy silver
            return duchies, silver, self.discard_list
        # return duchies, silver, self.discard_list

        elif 5 > self.curr_money >= 3:
            if len(provinces) <= 2:
                print("REMAINDER PROVINCES: ", len(provinces))
                self.buy_card(estates.pop())
                print("Estate")
                # active player buy estate
            else:
                self.buy_card(silver.pop())
                print("silver")
            # active player buy silver
            return estates, silver, self.discard_list
        # return estates, silver, self.discard_list

        elif self.curr_money == 2:
            if len(provinces) <= 3:
                print("REMAINDER PROVINCES: ", len(provinces))
                self.buy_card(estates.pop())
                print("estate")
            #   active player buy estate
            else:
                self.discard()
                print("discard")
            return estates, self.curr_hand, self.deck_list, self.discard_list

        else:
            self.discard()
            print("discard")

        return self.curr_money, gold, silver, provinces, duchies, self.curr_hand, self.deck_list, self.discard_list

class smithy_big_money(Player):
    def __init__(self, id):
        Player.__init__(self, id, 0, "smithy big money")
        #self.id

    def strategy(self, gold, silver, provinces, duchies, estates, smithy):
        self.turn = self.turn + 1
        print("current money: ", self.curr_money)
        if self.curr_money >= 4 and len \
            ([i for i, x in enumerate(self.purchased_cards) if isinstance(x, Smithy)]) == 0 and len(smithy) > 0:
            self.buy_card(smithy.pop())
        else:
            if self.curr_money >= 8:
                if len(gold) < 1 and len(silver) < 5:
                    print("REMAINDER GOLD: ", len(gold), "REMAINDER SILVER: ", len(silver))
                    self.buy_card(gold.pop())
                    print("gold")
                    # active player buy gold
                else:
                    self.buy_card(provinces.pop())
                    print("province")
                return gold, provinces, self.discard_list
            # return gold, provinces, self.discard_list

            # active player buy province
            elif 8 > self.curr_money >= 6:
                if len(provinces) <= 4 and len(duchies) > 0:
                    print("REMAINDER PROVINCE: ", len(provinces))
                    self.buy_card(duchies.pop())
                    print("duchy")
                    # active player buy duchy
                else:
                    self.buy_card(gold.pop())
                    print("gold")
                    # active player buy gold
                return duchies, gold, self.discard_list
            # return duchies, gold, self.discard_list

            # buy second smithy after 3 turns
            elif self.curr_money >= 4 and self.turn >= 3 and len \
                    ([i for i, x in enumerate(self.purchased_cards) if isinstance(x, Smithy)]) == 1 and len(smithy) > 0:
                self.buy_card(smithy.pop())

            elif self.curr_money == 5:
                if len(provinces) <= 5 and len(duchies) > 0:
                    print("REMAINDER PROVINCES: ", len(provinces))
                    self.buy_card(duchies.pop())
                    print("duchy")
                    # active player buy duchy
                else:
                    self.buy_card(silver.pop())
                    print("silver")
                # active player buy silver
                return duchies, silver, self.discard_list
            # return duchies, silver, self.discard_list

            elif 5 > self.curr_money >= 3:
                if len(provinces) <= 2:
                    print("REMAINDER PROVINCES: ", len(provinces))
                    self.buy_card(estates.pop())
                    print("Estate")
                    # active player buy estate
                else:
                    self.buy_card(silver.pop())
                    print("silver")
                # active player buy silver
                return estates, silver, self.discard_list
            # return estates, silver, self.discard_list

            elif self.curr_money == 2:
                if len(provinces) <= 3:
                    print("REMAINDER PROVINCES: ", len(provinces))
                    self.buy_card(estates.pop())
                    print("estate")
                #   active player buy estate
                else:
                    self.discard()
                    print("discard")
                return estates, self.curr_hand, self.deck_list, self.discard_list

            else:
                self.discard()
                print("discard")

            return self.curr_money, gold, silver, provinces, duchies, self.curr_hand, self.deck_list, self.discard_list

class user(Player):
    def __init__(self, id):
        Player.__init__(self, id, 0, "user")
        #self.id

    def strategy(self, gold, silver, provinces, duchies, estates ,smithy):
        self.turn = self.turn + 1
        print("You are on turn ", self.turn)
        print("your current hand is: ", self.curr_hand)
        print("your current money: ", self.curr_money)
        print("What would you like to purchase? (estate, duchy, province, copper, silver, gold, smithy, or discard")
        x = input()
        if x == 'estate' or 'duchy' or 'province' or 'copper' or 'silver' or 'gold' or 'smithy' or 'discard':
            if x == 'estate' and self.curr_money >= 2:
                self.buy_card(estates.pop())
                return estates, self.discard_list
            elif x == 'duchy' and self.curr_money >= 5:
                self.buy_card(duchies.pop())
                return duchies, self.discard_list
            elif x == 'province' and self.curr_money >= 8:
                self.buy_card(provinces.pop())
                return provinces, self.discard_list
            elif x == 'copper' and self.curr_money >= 0:
                self.buy_card(copper.pop())
                return copper, self.discard_list
            elif x == 'silver' and self.curr_money >= 3:
                self.buy_card(silver.pop())
                return silver, self.discard_list
            elif x == 'gold' and self.curr_money >= 6:
                self.buy_card(gold.pop())
                return gold, self.discard_list
            elif x == 'smithy' and self.curr_money >= 4:
                self.buy_card(smithy.pop())
                return smithy, self.discard_list
            elif x == 'discard':
                self.discard()
                return self.discard_list, self.curr_hand, self.deck_list