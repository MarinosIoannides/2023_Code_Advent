"""
Day 4 Code
-----------

Part 1
-------
    Scratchcards have 5 numbers on them
    Only some are winning numbers
    Each winning number multiplies the score by 2
    What is the score sum for this stack of scractchards?
"""

file_path = "./day_4/"
file_name = "day_4_input.txt"

file_string = file_path + file_name

with open(file_string) as open_file:
    lines = [line for line in open_file.read().splitlines()]

def calc_score(line):
    score, winners = line.split(" | ")
    card, score = score.split(": ")
    winners = list(winners.split(" "))
    score = list(score.split(" "))
    score = [number for number in score if number != '']
    total = 0
    for number in score:
        if number in winners:
            total = total * 2 + 1 if total != 0 else 1
    return total

def total_score(all_lines):
    return sum(calc_score(line) for line in all_lines)

"""
Part 2
-------
    A winning number copies the next scratchcard in the sequence 
    Points are also scored as normal
"""
def calc_dup_score(input):
    score_dict = {}
    for line in input:
        score, winners = line.split(" | ")
        card, score = score.split(": ")
        card_num = int(card.replace("Card ", ""))
        winners = list(winners.split(" "))
        score = list(score.split(" "))
        score = [number for number in score if number != '']

        right = sum(1 for number in score if number in winners)
        score_dict[card_num] = right

    occurence_dict = dict.fromkeys(score_dict.keys(), 1)
    for card in occurence_dict.keys():
        score = score_dict[card]
        for occurence in range(occurence_dict[card]):
            for increment in range(score):
                occurence_dict[card + increment+1] += 1
    return sum(occurence_dict.values())

print(calc_dup_score(lines))