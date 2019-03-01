from textwrap import wrap
from functools import reduce

def largest_product(series, size):
    """
    :param str series: Given serie of numbers to validate
    :param int size: Serie subsequence size interval to calculate product
    :rtype: int
    """
    if(size == 0):
        return 1

    if(len(series) < size):
        raise ValueError("Product size bigger than given serie length.")

    step = 0
    product = 0

    while True:
        wrapped = wrap(series[step:], size)[0]
        if len(wrapped) == size:
            product = max(reduce(lambda x, y: int(x)*int(y), list(wrapped)), product)
            step += 1
        else:
            break
    return product
