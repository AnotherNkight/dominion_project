from card import *
from curses import *

#creates ascii version of victory cards, called by add_v_cards()
def ascii_victory_card(current_card):

    # create an empty list
    lines = []

    # Create card structure
    lines.append('┌──────────┐')
    lines.append(f'│{current_card.name:^10}│')  # puts card name in center of 10 characters (=width of card)

    for _ in range(3):
        lines.append('│          │')

    lines.append(f'│{current_card.points:^10}│')  # .format(current_card.points))

    for _ in range(3):
        lines.append('│          │')

    lines.append('│{}   {}     │'.format(current_card.cost, 'V'))
    lines.append('└──────────┘')

    #return '\n'.join(lines)
    return lines

#creates ascii version of treasure cards, called by add_m_cards()
def ascii_money_card(current_card):

    # create an empty list
    lines = []

    # Create card structure
    lines.append('┌──────────┐')
    lines.append(f'│{current_card.value:<2}{current_card.name:^6}{current_card.value:>2}│')  # puts card name in center of 10 characters (=width of card)

    for _ in range(3):
        lines.append('│          │')

    lines.append(f'│{current_card.value:^10}│')  # .format(current_card.points))

    for _ in range(3):
        lines.append('│          │')

    lines.append('│{}   {}     │'.format(current_card.cost, 'T'))
    lines.append('└──────────┘')

    #return '\n'.join(lines)
    return lines

#stores ascii images of all victory cards in a list
ascii_victory_card_list = []
def add_v_cards():
    victory_card_list = [Estate(), Duchy(), Province()]
    for card in victory_card_list:
        current_card = card
        ascii_victory_card_list.append(ascii_victory_card(current_card))

    return ascii_victory_card_list

#stores ascii images of all treasure cards in a list
ascii_money_card_list = []
def add_m_cards():
    money_card_list = [Copper(), Silver(), Gold()]
    for card in money_card_list:
        current_card = card
        ascii_money_card_list.append(ascii_money_card(current_card))

    return ascii_money_card_list

#uses join() on each segment of the ascii card so it can be displayed on the screen (as a string)
def string_convert(list):

    return '\n'.join(list)

def get_color(screen):
    screen.init_color()
    screen.init_pair(1,1,1,1)

#adds the string images of the ascii cards to the screen to create a board
def display_cards(screen):

    num_rows, num_cols = screen.getmaxyx()
    half_length_of_cards = int(90 / 2)  #approx. half the length of space used by cards
    middle_column = int(num_cols / 2)
    row = middle_column - half_length_of_cards - 12

    for y in range(len(ascii_victory_card_list)):

        row = row + 12                                              #controls how far across, adding a card width after each card

        for i, line in enumerate(ascii_victory_card_list[y]):

            x = 5 + i                                               #controls how far down, moving 1 line further with each iteration
            #print("i's value: ", i)
            new_section = ascii_victory_card_list[y]
            string_convert(new_section[i])                          #calls function to convert each line of card to a str so it can be displayed in the window
            #print("line converted: ", new_section[i], "x: ", x, "row: ", row)
            screen.addstr(x, row, new_section[i])

    #buffer between victory and treasure cards
    row = row + 12

    for y in range(len(ascii_money_card_list)):

        row = row + 12  # resuming from last row counter

        for i, line in enumerate(ascii_money_card_list[y]):
            x = 5 + i  # controls how far down, moving 1 line further with each iteration
            #print("i's value: ", i)
            new_section = ascii_money_card_list[y]
            string_convert(new_section[i])  # calls function to convert each line of card to a str so it can be displayed in the window
            #print("line converted: ", new_section[i], "x: ", x, "row: ", row)
            screen.addstr(x, row, new_section[i])

    screen.refresh()
    screen.getch()
'''
add_v_cards()
add_m_cards()
wrapper(display_cards)
'''