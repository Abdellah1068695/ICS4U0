from Polynomial import Polynomial

def get_coefficients():
    coeffs = input("Enter the coefficients of the polynomial separated by commas: ")
    return list(map(float, coeffs.split(',')))

# Get coefficients from user
coefficients = get_coefficients()

# Define a polynomial
p5 = Polynomial(coefficients)
print("Polynomial:", p5)

# Print the order of the polynomial
print("Order of the polynomial:", p5.get_order())

# Evaluate the polynomial at x = 2
print("Value of the polynomial at x = 2:", p5.f(2))
