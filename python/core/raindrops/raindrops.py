""" Raindrops - Solution """

def raindrops(number: int) -> str:
    """
    :param number: Number to be analyzed
    """
    drop_list = [(3, 'Pling'), (5, 'Plang'), (7, 'Plong')]
    response = ''.join([drop for value, drop in drop_list if number % value == 0])
    return response or str(number)
