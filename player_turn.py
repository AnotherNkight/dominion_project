from card import *
import random

class Player:
    def __init__(self, id, points, type):
        self.id = id
        self.points = points
        self.type = type
        self.curr_hand = []
        self.starting_deck = [Estate(), Estate(), Estate(), Copper(), Copper(), Copper(), Copper(), Copper(), Copper(), Copper()]
        self.deck_list = self.starting_deck.copy()
        random.shuffle(self.deck_list)
        self.discard_list = []
        self.curr_money = 0
        self.purchased_cards = []
        self.turn = 0
    def __repr__(self):
        return self.id

    #adds purchased card to discard and then calls discard () to discard hand
    def buy_card(self, card):
        self.discard_list.append(card)
        self.purchased_cards.append(card)
        self.discard()
        if isinstance(card, Province):
            text = "Player " + str(self.id) + " purchased a province on turn " + str(self.turn) + ". They now have " + str(
                len([i for i, x in enumerate(self.purchased_cards) if isinstance(x, Province)])) + " province(s).\n"
            with open("province_tracker.txt", "a") as f:
                f.write(text)

        return self.purchased_cards

    def discard(self):
        for i in range(len(self.curr_hand)):
            self.discard_list.append(self.curr_hand[0])
            self.curr_hand.remove(self.curr_hand[0])
        self.card_draw()
        return self.curr_hand, self.deck_list

    #replenishes hand if less than 5 cards
    #calls card_draw
    def deck_f(self):
        if len(self.curr_hand) < 5:
            #self.curr_hand, self.deck_list = self.card_draw()
            self.card_draw()
        return self.curr_hand

    # draw 5 cards
    # called by deck_f()
    def card_draw(self):
        for i in range(5 - len(self.curr_hand)):
            if len(self.deck_list) < 1:
                random.shuffle(self.discard_list)
                for i in range(len(self.discard_list)):
                    self.deck_list.append(self.discard_list[0])
                    self.discard_list.remove(self.discard_list[0])
                return self.deck_list, self.discard_list

            self.curr_hand.append(self.deck_list[0])
            self.deck_list.remove(self.deck_list[0])
        return self.curr_hand, self.deck_list, self.discard_list

    #draw function for action cards
    def action_card_draw(self, active_card):
        for i in range(active_card.card_draw):
            if len(self.deck_list) < 1:
                random.shuffle(self.discard_list)
                for i in range(len(self.discard_list)):
                    self.deck_list.append(self.discard_list[0])
                    self.discard_list.remove(self.discard_list[0])
                return self.deck_list, self.discard_list

            self.curr_hand.append(self.deck_list[0])
            self.deck_list.remove(self.deck_list[0])
        return self.curr_hand, self.deck_list, self.discard_list

    #evaluates amount of money in the current hand
    def buy_power(self):

        for i in range(len(self.curr_hand)):
            self.curr_money = self.curr_money + self.curr_hand[i].value
        return self.curr_money

    #find the player with the highest score
    def player_score(self):
        for i in range(0, len(self.discard_list)):
            self.points = self.points + self.discard_list[i].points
            #print("discard points: ", self.points)
        for i in range(0, len(self.curr_hand)):
            self.points = self.points + self.curr_hand[i].points
            #print("hand points: ", self.points)
        for i in range(0, len(self.deck_list)):
            self.points = self.points + self.deck_list[i].points
           #print("i: ", i, "length", len(self.deck_list), "deck points: ", self.points)
        return self.points

        # determines the best buy for active player

    def big_money(self, gold, silver, provinces, duchies, estates):
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

    def smithy_bm(self, gold, silver, provinces, duchies, estates, smithy):
        self.turn = self.turn + 1
        print("current money: ", self.curr_money)
        if self.curr_money >= 4 and len([i for i, x in enumerate(self.purchased_cards) if isinstance(x, Smithy)]) == 0 and len(smithy) > 0:
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

            #buy second smithy after 3 turns
            elif self.curr_money >= 4 and self.turn >= 3 and len([i for i, x in enumerate(self.purchased_cards) if isinstance(x, Smithy)]) == 1 and len(smithy) > 0:
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