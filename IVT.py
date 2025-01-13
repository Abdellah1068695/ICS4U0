from Polynomial import Polynomial

class IVT:
    def __init__(self, polynomial):
        """
        Initializes the IVT solver with a Polynomial object.
        :param polynomial: An instance of the Polynomial class.
        """
        self.polynomial = polynomial

    def findZero(self, x1, x2, tolerance=0.0004):
        """
        Uses the Intermediate Value Theorem to find the zero of the polynomial
        between x1 and x2.
        :param x1: Float lower bound.
        :param x2: Float upper bound.
        :param tolerance: Accuracy for f(x0).
        :return: Float x0 if zero is found, else a string message.
        """
        if x1 == x2:
            return "x1 and x2 cannot be the same."
        if self.polynomial.f(x1) * self.polynomial.f(x2) > 0:
            return "f(x1) and f(x2) must have opposite signs."

        while True:
            x0 = (x1 + x2) / 2  # Midpoint
            f_x0 = self.polynomial.f(x0)

            if abs(f_x0) <= tolerance:
                return x0  # Zero found
            elif f_x0 > 0:
                x2 = x0  # Zero is between x1 and x0
            else:
                x1 = x0  # Zero is between x0 and x2

