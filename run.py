import math
import random
import cli.log
from tabulate import tabulate


def generate_number(range_start, range_end, odds):
    number = 0
    chance = random.uniform(0, 1)
    if odds >= 1 or odds >= chance:
        number = random.randint(math.floor(range_start), math.ceil(range_end))

    return number

def increment(start, end, increments, starting_point):
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

@cli.log.LoggingApp
def IncrementalIntegerSet(app):
    start = app.params.start
    end = app.params.end
    increments = app.params.increments
    starting_point = app.params.starting_point

    numbers = increment(start, end, increments, starting_point)

    print(tabulate(numbers, headers=["Id", "Number"]))


IncrementalIntegerSet.add_param("start", help="", default=1, type=int)
IncrementalIntegerSet.add_param("end", help="", default=1, type=int)
IncrementalIntegerSet.add_param("increments", help="", default=1, type=int)
IncrementalIntegerSet.add_param("starting_point", help="", default=1, type=int)

if __name__ == "__main__":
    IncrementalIntegerSet.run()
