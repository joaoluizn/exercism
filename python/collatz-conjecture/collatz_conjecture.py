""" Collatz Conjecture Steps calculator """

def steps(number):
    """ Calculate the number of steps to complete the Collatz Cojecture for a given number """
    step_counter = 0

    while number != 1:
        if number <= 0:
            raise ValueError("Only positive integers are allowed")

        if number % 2 == 0:
            number = number / 2

        else:
            number = (3 * number) + 1
        step_counter += 1
    return step_counter
