import math
import random

def generate_number(range_start, range_end, odds):
    number = 0
    chance = random.uniform(0, 1)
    if odds >= 1 or odds >= chance:
        number = random.randint(math.floor(range_start), math.ceil(range_end))

    return number


def simulate(start, end, increments, starting_point, flex):
    if end < start:
        return list(reversed(increment(end, start, increments, starting_point, flex)))
    else:
        return increment(start, end, increments, starting_point, flex)


def increment(start, end, increments, starting_point, flex):
    numbers = []
    pot = end - start
    number_distance = float(pot) / increments  # Get distance between every increment, e.g. in a range of 20 with 10 increments, distance is 2

    for x in range(increments):
        last_number = start if x < 1 else numbers[x - 1][1]
        increment_number = generate_number(1, number_distance * 2, number_distance)
        increment_number = pot if increment_number > pot else increment_number
        numbers.append([x + starting_point, last_number + increment_number])
        pot = pot - increment_number

    return numbers