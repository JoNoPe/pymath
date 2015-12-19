__author__ = 'Noah'


class Term:
    def __init__(self):
        self.term = []
        # var, const, numbers
        # operators
        # functions, brackets
        # design custom functions as functions?

    def as_string(self):
        pass


class Equation:
    def __init__(self):
        self.left = Term()
        self.right = Term()

    def as_string(self):
        return self.left.as_string() + '=' + self.right.as_string()
