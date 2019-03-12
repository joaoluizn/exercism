def is_armstrong(number):
    """
    :param str number: Given number to validate armstrong theory
    :rtype: bool
    """
    str_number = str(number)
    int_list = [int(x) for x in list(str_number)]
    return number == sum([k**len(str_number) for k in int_list])
