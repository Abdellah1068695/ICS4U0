from Polynomial import Polynomial
# driver
P = Polynomial([0, 0, 1, 2, 0, 3, 0, 0])
print(P)
for i in range(10):
    print(i, P.f(i))
print(P.get_order())
