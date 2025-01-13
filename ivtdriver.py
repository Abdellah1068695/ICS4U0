from IVT import *

def get_coefficients():
    coeffs = input("Enter the coefficients of the polynomial separated by commas: ")
    return list(map(float, coeffs.split(',')))

def get_interval():
    x1 = float(input("Enter the lower bound (x1): "))
    x2 = float(input("Enter the upper bound (x2): "))
    return x1, x2

# Get coefficients and interval from user
coefficients = get_coefficients()
x1, x2 = get_interval()

# Define a polynomial
P = Polynomial(coefficients)
print("Polynomial:", P)

# Initialize the IVT solver
ivt_solver = IVT(P)

# Find the zero
result = ivt_solver.findZero(x1, x2)
print(f"Estimated zero between {x1} and {x2}: {result}")
