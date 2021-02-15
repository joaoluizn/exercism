""" Beer Song solution """


def recite(start, take=1):
    answer = []
    stop_condition = start-take
    for value in range(start, start-take, -1):
        answer.append(__build_first_phrase(value))
        answer.append(__build_second_phrase(value))

        if value-1 != stop_condition:
            answer.append('')
    return answer


def __build_first_phrase(value):
    return f'{__get_value_phrase(value, True)} of beer on the wall, {__get_value_phrase(value)} of beer.'


def __build_second_phrase(value):
    phrase = f'Take {__get_take_bottle_word(value)} down and pass it around, {__get_value_phrase(value-1)} of beer on the wall.'
    if value == 0:
        phrase = __build_refil_phrase()
    return phrase


def __get_take_bottle_word(value):
    return "it" if value == 1 else "one"


def __build_refil_phrase():
    return f'Go to the store and buy some more, {__get_value_phrase(99)} of beer on the wall.'


def __get_value_phrase(value, camel=False):
    text = value
    if value == 0:
        text = 'No more' if camel else 'no more'
    return f'{text} {__get_plural_or_singular_bottle(value)}'


def __get_plural_or_singular_bottle(value):
    return 'bottle' if value == 1 else 'bottles'
