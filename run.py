import random
import cli.log
from tabulate import tabulate


def increment(start, end, increments, starting_point):
    numbers = []
    pot = end - start
    number_distance = pot / increments  # Get distance between every increment, e.g. in a range of 20 with 10 increments, distance is 2
    number_distance = number_distance if number_distance > 0 else 1

    increment_number = number_distance

    for x in range(increments):
        last_number = start if x < 1 else numbers[x - 1][1]
        current_number_distance = increment_number - number_distance
        temp_actual_number_distance = number_distance + abs(current_number_distance)
        actual_number_distance = temp_actual_number_distance if temp_actual_number_distance < pot else pot
        temp_number = random.randint(0, actual_number_distance)
        increment_number = 0 if temp_number < 0 else temp_number
        pot = pot - increment_number
        numbers.append([x + starting_point, last_number + increment_number])

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
