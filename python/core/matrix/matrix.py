class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = [k.split() for k in matrix_string.split('\n')]

    def row(self, index) -> list:
        """ Get row of desired index """
        return list(map(int, self.rows[index-1]))

    def column(self, index) -> list:
        """ Get column of desired index """
        return [int(k[index-1]) for k in self.rows]

