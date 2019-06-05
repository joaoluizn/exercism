""" Construct raindrop factors to a given number """
def raindrops(number):
    drop_list = [(3, 'Pling'), (5, 'Plang'), (7, 'Plong')]
    response = ''.join([drop for value, drop in drop_list if number % value == 0])
    return response or str(number)
