class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = [list(map(int, k.split())) for k in matrix_string.splitlines()]

    def row(self, index) -> list:
        """ Get row of desired index """
        return self.rows[index-1]

    def column(self, index) -> list:
        """ Get column of desired index """
        return [k[index-1] for k in self.rows]

