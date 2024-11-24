import math


def find_solutions(a, b, c):
    if a == 0 or b == 0:
        raise ValueError("Invalid coefficients! a and b must be non-negative!")

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return "No real solutions"

    discriminant_root = math.sqrt(discriminant)

    x1 = (-b + discriminant_root) / (2 * a)
    x2 = (-b - discriminant_root) / (2 * a)

    if x1 == x2:
        return x1

    return [x1, x2]


