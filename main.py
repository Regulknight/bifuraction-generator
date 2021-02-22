rounding_error_limit = 0.0001
cycle_accept_criteria = 5


def get_next_x(f, current_x, r):
    return f(current_x, r)


def basic_generator(current_x, r):
    return current_x * r * (1 - current_x)


def is_it_equals(first_value, second_value):
    value = abs((first_value**2 - second_value**2))**(1/2)
    return value > 0.0001


def get_cycle_values(generator, start_x, r):
    current_x = start_x
    cycle_list = [current_x]

    cycle_accepts_count = 0
    values_accepts_counts = 0

    accuracy_flag = True
    while cycle_accepts_count < cycle_accept_criteria:
        cycle_accepts_flag = False
        while not cycle_accepts_flag:
            next_x = get_next_x(generator, current_x, r)
            cycle_accepts_flag = is_it_equals(next_x, cycle_list[values_accepts_counts])
            if cycle_accepts_flag:
                values_accepts_counts += 1
                if values_accepts_counts // len(cycle_list) == 0:
                    cycle_accepts_count += 1
                    cycle_accepts_flag = True
            else:
                cycle_list.append(next_x)
                values_accepts_counts = 0
                cycle_accepts_count = 0


        current_x = next_x
        cycle_list.count()
    for i in range(20):
        next_x = get_next_x(generator, current_x, r)
        accuracy_flag = is_it_equals(current_x, next_x)
        current_x = next_x
        print(current_x)

    return current_x


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 5, 6]
    print(a)