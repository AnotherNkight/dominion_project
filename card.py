class Card:
   def __init__(self, name, value, points, cost, action, card_draw, add_money):
      self.name = name
      self.value = value
      self.points = points
      self.cost = cost     #unnecessary for current code, but nice to see costs of cards
      self.action = action
      self.card_draw = card_draw
      self.add_money = add_money
   def __repr__(self):
      return self.name

class Estate(Card):
   def __init__(self):
      Card.__init__(self, 'Estate', 0, 1, 2, 0, 0, 0)

class Duchy(Card):
   def __init__(self):
      Card.__init__(self, 'Duchy', 0, 3, 5, 0, 0, 0)

class Province(Card):
   def __init__(self):
      Card.__init__(self, 'Province', 0, 6, 8, 0, 0, 0)

class Copper(Card):
   def __init__(self):
      Card.__init__(self, 'Copper', 1, 0, 0, 0, 0, 0)

class Silver(Card):
   def __init__(self):
      Card.__init__(self, 'Silver', 2, 0, 3, 0, 0, 0)

class Gold(Card):
   def __init__(self):
      Card.__init__(self, 'Gold', 3, 0, 6, 0, 0, 0)

class Smithy(Card):
   def __init__(self):
      Card.__init__(self, 'Smithy', 0, 0, 4, 0, 3, 0)