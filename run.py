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


def generate_output(output, content):
    if output == "cli":
        print(tabulate(content, headers=["Id", "Number"]))
    elif output == "xlsx":
        create_xlsx_sheet(content)
    else:
        print("Only CLI and XLSX is available as output types at the moment")


def create_xlsx_sheet(content):
    print("NotImplementedYet")


@cli.log.LoggingApp
def incremental_integer_set(app):
    start = app.params.start
    end = app.params.end
    increments = app.params.increments
    starting_point = app.params.startpoint
    output = app.params.output

    numbers = increment(start, end, increments, starting_point)

    generate_output(output, numbers)


incremental_integer_set.add_param("start", help="", default=1, type=int)
incremental_integer_set.add_param("end", help="", default=1, type=int)
incremental_integer_set.add_param("increments", help="", default=1, type=int)
incremental_integer_set.add_param("-S", "--startpoint", help="", default=1, type=int)
incremental_integer_set.add_param("-o", "--output", help="", default="cli", type=str)

if __name__ == "__main__":
    incremental_integer_set.run()
