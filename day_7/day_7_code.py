"""
Day 7 Code
----------

Part 1
-------
    Find the total winnings of the hands in the inputs.

Card Ranks
    Five of a kind, where all five cards have the same label: AAAAA
    Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    High card, where all cards' labels are distinct: 23456
"""
import polars as pl

file_path = "./day_7/"
file_name = "day_7_input.txt"

file_string = file_path + file_name

CARD_RANKS = [
    "A", "K", "Q", "J", "T", 
    "9", "8", "7", "6", "5", "4", "3", "2", 
    ]

with open(file_string) as open_file:
    lines = [line for line in open_file.read().splitlines()]

def determine_kind(cards):
    if len(set(cards)) == 1:
        return 0
    elif len(set(cards)) == 2:
        if cards.count(cards[0]) == 1 or cards.count(cards[0]) == 4:
            return 1
        else:
            return 2
    elif len(set(cards)) == 3:
        for card in cards:
            if cards.count(card) == 3:
                return 3
        return 4
    elif len(set(cards)) == 4:
        return 5
    elif len(set(cards)) == 5:
        return 6

cards = [line.split(" ")[0] for line in lines] 
data_dict = {
    "cards": [line.split(" ")[0] for line in lines],
    "bets": [int(line.split(" ")[1]) for line in lines],
    "kind": [determine_kind(card) for card in cards],
}    
for digit in range(5):
    data_dict[f"digit {digit}"] = [CARD_RANKS.index(card[digit]) for card in cards]

unwanted = ["cards", "bets"]
dataframe = pl.DataFrame(data_dict)

relevant_columns = [column for column in dataframe.columns if column not in unwanted]

dataframe = dataframe.sort(by = relevant_columns, descending = True)

start = 0
p = 1
for row in dataframe.rows():
    start += p* row[1]
    p += 1

"""
Part 2
-------
    There are Jokers, which become whatever card would make the hand stronger
    They are the weaker hand to make up for it
"""
JOKER_RANKS = [
    "A", "K", "Q", "T", 
    "9", "8", "7", "6", "5", "4", "3", "2", "J"
    ]

def with_jokers(cards):
    if "J" not in cards:
        return determine_kind(cards)
    elif len(set(cards)) == 1:
        return determine_kind(cards)
    else:
        card_counts = {item: cards.count(item) for item in cards}
        no_j = card_counts.copy()
        del no_j["J"]
        max_card = max(no_j, key=no_j.get)
    for rounds in range(card_counts["J"]):
        cards = cards +max_card
    good_cards = [card for card in cards if card != "J"]
    return determine_kind(good_cards)


data_dict = {
    "cards": [line.split(" ")[0] for line in lines],
    "bets": [int(line.split(" ")[1]) for line in lines],
    "kind": [with_jokers(card) for card in cards],
}    
for digit in range(5):
    data_dict[f"digit {digit}"] = [JOKER_RANKS.index(card[digit]) for card in cards]

unwanted = ["cards", "bets"]
dataframe = pl.DataFrame(data_dict)

relevant_columns = [column for column in dataframe.columns if column not in unwanted]

dataframe = dataframe.sort(by = relevant_columns, descending = True)

start = 0
p = 1
for row in dataframe.rows():
    start += p* row[1]
    p += 1

    


