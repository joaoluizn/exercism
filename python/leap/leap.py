def is_leap_year(year):
    """
    :param int year: Given year to verify if its leap
    :rtype: bool
    """
    # More legible solution
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    else:
        return False
    # Alternative solution in one line
    # return True if year % 400 == 0 else False if year % 100 == 0 else True if year % 4 == 0 else False
