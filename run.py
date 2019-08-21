import random

def generateCLIOptions():
    print("CLI")

def increment(start, end, increments, starting_point=0, use_decimals=None):
    numbers=[]
    number_distance = (end - start) / increments # Get distance between every increment, e.g. in a range of 20 with 10 increments, distance is 2

    increment_number = number_distance

    for x in range(increments):
        last_number = start if x < 1 else numbers[x - 1]
        current_number_distance = increment_number - number_distance
        actual_number_distance = number_distance + abs(current_number_distance)
        increment_number = random.randint(current_number_distance, actual_number_distance)
        numbers.append(last_number + increment_number)

    return numbers


print(increment(2, 20, 10))
