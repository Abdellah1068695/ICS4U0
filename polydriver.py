from Polynomial import Polynomial

def get_coefficients():
    coeffs = input("Enter the coefficients of the polynomial separated by commas: ")
    return list(map(float, coeffs.split(',')))

# Get coefficients from user
coefficients = get_coefficients()

# Define a polynomial
p = Polynomial(coefficients)
print("Polynomial:", p)

# Print the order of the polynomial
print("Order of the polynomial:", p.get_order())

# Evaluate the polynomial at x = 2
for i in range(10):
 print("x =", i,"f(x) =", p.f(i))
