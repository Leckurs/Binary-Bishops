
class Move:

    def __init__(self, initial, final):
        # initial and final are squares
        self.initial = initial
        self.final = final

    def __str__(self):
        """
        Returns the move in basic algebraic notation.
        Example: e2e4
        """
        return f"{self.initial}{self.final}"

    def __eq__(self, other):
        return self.initial == other.initial and self.final == other.final