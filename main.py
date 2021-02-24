import datetime
import json
import time
import numpy

rounding_error_limit = 0.0001
cycle_accept_criteria = 5
cycle_maximum_size = 10000


def get_next_x(f, current_x, r):
    return f(current_x, r)


def basic_generator(current_x, r):
    return current_x * r * (1 - current_x)


def is_it_equals(first_value, second_value):
    value = abs((first_value**2 - second_value**2))**(1/2)
    return value < 0.01


def is_equals_arrays(first_array, second_array):
    if len(first_array) != len(second_array):
        return False

    for i in range(len(first_array)):
        if not is_it_equals(first_array[i], second_array[i]):
            return False

    return True


calculation_map = {}


def add_to_calc_map(key, value, map=calculation_map):
    map.update({key: value})


def get_cycle_values(generator, start_x, r):

    current_x = start_x
    add_to_calc_map("start_x", current_x)
    add_to_calc_map("r", r)

    cycle_list = [current_x]

    iteration_counter = 0
    while True:
        add_to_calc_map("iteration_counter", iteration_counter)
        add_to_calc_map("current_x", current_x)
        next_x = get_next_x(generator, current_x, r)
        cycle_list.append(next_x)
        add_to_calc_map("cycle_list", cycle_list)
        for i in range(1, len(cycle_list)//cycle_accept_criteria):
            add_to_calc_map("tfs", get_human_time_from_start(start_time))

            json_object = json.dumps(calculation_map, indent=4)
            print(json_object)

            cycle = cycle_list[-i:]
            place_to_cycle_search = cycle_list[-cycle_accept_criteria*i:]
            add_to_calc_map("cycle", cycle)
            cycle_attempt_count = 0
            for j in range(cycle_accept_criteria):
                first_cycle_attempt = place_to_cycle_search[:i]
                place_to_cycle_search = place_to_cycle_search[i:]
                if is_equals_arrays(cycle, first_cycle_attempt):
                    cycle_attempt_count += 1
                    if cycle_attempt_count == cycle_accept_criteria:
                        return cycle

        if len(cycle_list) > cycle_maximum_size * cycle_accept_criteria:
            return cycle_list

        current_x = next_x
        iteration_counter += 1


def get_human_time_from_start(start_time):
    time_from_start = time.time_ns() - start_time
    dt = datetime.datetime.fromtimestamp(time_from_start/1e9)
    return '{}{:03.0f}'.format(dt.strftime('%Y-%m-%dT%H:%M:%S.%f'), time_from_start % 1e3)


if __name__ == '__main__':
    start_time = time.time_ns()
    for r in numpy.arange(2.6, 3.8, 0.01):
        get_cycle_values(basic_generator, 0.4, r)

    print("That's all")





