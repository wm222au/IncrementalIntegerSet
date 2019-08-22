import math
import random
import cli.log
import xlsxwriter
import os.path
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


def generate_output(output, name, content):
    if output == "cli":
        print(tabulate(content, headers=["Id", "Number"]))
    elif output == "xlsx":
        create_xlsx_sheet(content, name)
    else:
        print("Only CLI and XLSX is available as output types at the moment")


def file_exists(name):
    return os.path.exists(name)


def get_available_file_name(name):
    fsCount = 1
    original_name = name
    name = name + '.xlsx'
    while file_exists(name):
        name = original_name + '-' + str(fsCount) + '.xlsx'
        fsCount += 1

    return name


def create_xlsx_sheet(content, name):
    name = get_available_file_name(name)
    workbook = xlsxwriter.Workbook(name)
    worksheet = workbook.add_worksheet()

    row = 0

    for col, data in enumerate(content):
        worksheet.write_row(row, 0, data)
        row += 1

    workbook.close()


@cli.log.LoggingApp
def incremental_integer_set(app):
    start = app.params.start
    end = app.params.end
    increments = app.params.increments
    starting_point = app.params.startpoint
    output = app.params.output
    name = app.params.name

    numbers = increment(start, end, increments, starting_point)

    generate_output(output, name, numbers)


incremental_integer_set.add_param("start", help="", default=1, type=int)
incremental_integer_set.add_param("end", help="", default=1, type=int)
incremental_integer_set.add_param("increments", help="", default=1, type=int)
incremental_integer_set.add_param("-S", "--startpoint", help="", default=1, type=int)
incremental_integer_set.add_param("-o", "--output", help="", default="cli", type=str)
incremental_integer_set.add_param("-n", "--name", help="", default="integer_set", type=str)

if __name__ == "__main__":
    incremental_integer_set.run()
