def is_leap_year(year):
    """
    :param int year: Given year to verify if its leap
    :rtype: bool
    """
    # Simple logical minimization fom below code
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    # More legible solution
    # if year % 4 == 0:
    #     if year % 100 == 0:
    #         if year % 400 == 0:
    #             return True
    #         return False
    #     return True
    # else:
    #     return False

    # Alternative solution in one line using ternary - More Complex
    # return True if year % 400 == 0 else False if year % 100 == 0 else True if year % 4 == 0 else False
