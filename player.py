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

            self.curr_hand.append(self.deck_list[0])
            self.deck_list.remove(self.deck_list[0])
        return self.curr_hand, self.deck_list, self.discard_list

    #draw function for action cards
    def action_card_draw(self, active_card):
        for i in range(active_card.card_draw):
            ##print('IN DRAW FUNCTION. DRAW # CARDS: ', active_card.card_draw)
            if len(self.deck_list) < 1:
                ##print('SHUFFLING')
                random.shuffle(self.discard_list)
                for i in range(len(self.discard_list)):
                    self.deck_list.append(self.discard_list[0])
                    self.discard_list.remove(self.discard_list[0])

            ##print('CARD TO BE ADDED: ', self.deck_list[0])
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