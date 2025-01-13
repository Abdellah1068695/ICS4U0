from IVT import IVT

if __name__ == "__main__":
    # Define a polynomial
    coefficients = [1, -6, 11, -6]  # f(x) = x^3 - 6x^2 + 11x - 6
    polynomial = Polynomial(coefficients)
    print("Polynomial:", polynomial)

    # Initialize the IVT solver
    ivt_solver = IVT(polynomial)

    # Define the interval [x1, x2]
    x1 = 1.0
    x2 = 3.0

    # Find the zero
    result = ivt_solver.findZero(x1, x2)
    print(f"Estimated zero between {x1} and {x2}: {result}")

