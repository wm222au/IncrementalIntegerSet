import random

def generateCLIOptions():
    print("CLI")

def increment(start, end, increments, starting_point=0, use_decimals=None):
    numbers=[]
    number_distance = (end - start) / increments # Get distance between every increment, e.g. in a range of 20 with 10 increments, distance is 2

    increment_number = number_distance

    for x in range(increments):
        new_number_distance = increment_number - number_distance
        current_number_distance = number_distance + abs(new_number_distance)
        increment_number = random.randint(0, current_number_distance)
        numbers.append(start + increment_number)

    return numbers


print(increment(2, 20, 10))
