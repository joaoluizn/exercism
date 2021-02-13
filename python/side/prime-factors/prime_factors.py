""" Prime Factors Solution """


def prime_factors(natural_number) -> list:
    """ Gets the prime factors for a given integer

    Args:
        natural_number (int): The value to be analyzed.

    Returns:
        list: A list containin prime factors for a given number.
    """
    response = []

    factor = 2
    while natural_number != 1:
        if natural_number % factor == 0:
            response.append(factor)
            natural_number /= factor
        else:
            factor += 1
    return response
