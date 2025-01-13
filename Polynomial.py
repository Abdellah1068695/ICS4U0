class Polynomial:
    def __init__(self, coefficients):
        """
        Initializes the polynomial with the given coefficients.
        :param coefficients: List of coefficients [a_n, a_(n-1), ..., a_0].
        """
        # Remove leading zeros and store the coefficients
        while coefficients and coefficients[0] == 0:
            coefficients.pop(0)
        self.coefficients = coefficients
        self.order = len(coefficients) - 1  # Degree of the polynomial

    def get_order(self):
        """
        Returns the order (degree) of the polynomial.
        :return: int
        """
        return self.order

    def f(self, x):
        """
        Evaluates the polynomial at a given x.
        :param x: Float value of x.
        :return: Float value of f(x).
        """
        result = 0
        for i, coef in enumerate(reversed(self.coefficients)):
            result += coef * (x ** i)
        return result

    def __str__(self):
        """
        Returns a string representation of the polynomial.
        :return: str
        """
        terms = []
        n = self.order
        for i, coef in enumerate(self.coefficients):
            power = n - i
            if coef != 0:
                if power > 1:
                    terms.append("{}x^{}".format(coef, power))
                elif power == 1:
                    terms.append("{}x".format(coef))
                else:
                    terms.append("{}".format(coef))
        return " + ".join(terms).replace("+ -", "- ") if terms else "0"
