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


def get_cycle_values(generator, start_x, r):
    current_x = start_x
    cycle_list = [current_x]

    cycle_accepts_flag = False
    while not cycle_accepts_flag:
        next_x = get_next_x(generator, current_x, r)
        print(next_x)
        cycle_list.append(next_x)
        for i in range(1, len(cycle_list)//cycle_accept_criteria):
            cycle = cycle_list[-i:]
            place_to_cycle_search = cycle_list[-cycle_accept_criteria*i:]

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

    return cycle_list


if __name__ == '__main__':
    print(get_cycle_values(basic_generator, 0.4, 3.8))
