""" Verify if 3, 5 and 7 are factors of a given number """
def raindrops(number):
    factors = [k for k in [3,5,7] if number % k == 0]
    response = ''

    if 3 in factors:
        response += 'Pling'
    if 5 in factors:
        response += 'Plang'
    if 7 in factors: 
        response += 'Plong'

    if not response:
        response = f'{number}'

    return response
