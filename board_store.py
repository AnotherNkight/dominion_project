from card import *

# board supply
number_of_provinces = 8
number_of_duchies = 8
number_of_estates = 21          #(24 - 3)
number_of_gold = 30
number_of_silver = 40
number_of_copper = 53           #(60 - 7)
number_of_smithies = 20         #check actual number

#store board stockpiles as lists
provinces = [Province() for _ in range(number_of_provinces)]
duchies = [Duchy() for _ in range(number_of_duchies)]
estates = [Estate() for _ in range(number_of_estates)]
gold = [Gold() for _ in range(number_of_gold)]
silver = [Silver() for _ in range(number_of_silver)]
copper = [Copper() for _ in range(number_of_copper)]
smithy = [Smithy() for _ in range(number_of_smithies)]