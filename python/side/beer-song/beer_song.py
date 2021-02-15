""" Beer Song solution """


def recite(start, take=1):
    answer = []
    stop_condition = start-take
    for value in range(start, stop_condition, -1):
        answer.append(__build_first_phrase(value))
        answer.append(__build_second_phrase(value))

        if value-1 != stop_condition:
            answer.append('')
    return answer


def __build_first_phrase(value):
    return f'{__get_value_phrase(value, True)} of beer on the wall, {__get_value_phrase(value)} of beer.'


def __build_second_phrase(value):
    if value == 0:
        phrase = f'Go to the store and buy some more, {__get_value_phrase(99)} of beer on the wall.'
    else:
        phrase = f'Take {__get_grab_beer_word(value)} down and pass it around, {__get_value_phrase(value-1)} of beer on the wall.'
    return phrase


def __get_value_phrase(value, camel=False):
    bottle_text = "bottle" if value == 1 else "bottles"
    quantity_text = value
    if value == 0:
        quantity_text = 'No more' if camel else 'no more'

    return f'{quantity_text} {bottle_text}'


def __get_grab_beer_word(value):
    return "it" if value == 1 else "one"
