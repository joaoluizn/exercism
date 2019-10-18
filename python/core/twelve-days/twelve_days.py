""" Twelve days - Solution """

ordinals = [
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelfth'
]
gifts = [
    "twelve Drummers Drumming, ",
    "eleven Pipers Piping, ",
    "ten Lords-a-Leaping, ",
    "nine Ladies Dancing, ",
    "eight Maids-a-Milking, ",
    "seven Swans-a-Swimming, ",
    "six Geese-a-Laying, ",
    "five Gold Rings, ",
    "four Calling Birds, ",
    "three French Hens, ",
    "two Turtle Doves, ",
    "and a Partridge in a Pear Tree.",
]

def recite(start_verse: str, end_verse: str) -> str:
    """ Build twelve days music verses """
    response = []
    for verse in range(start_verse, end_verse+1):
        first_part = f'On the {ordinals[verse-1]} day of Christmas my true love gave to me: '
        if verse == 1:
            second_part = gifts[-1][4:]
        else:
            second_part = ''.join(gifts[verse*-1:])
        response.append(f'{first_part}{second_part}')
    return response
