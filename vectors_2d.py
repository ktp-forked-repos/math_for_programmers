from math import sqrt, sin, cos, pi, atan2

dino_vectors = [
    (6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4),
    (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0), (0, -3),
    (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)
]


# def add(v1, v2):
#     return (v1[0] + v2[0], v1[1] + v2[1])


def add(*vectors):
    return (sum(v[0] for v in vectors), sum(v[1] for v in vectors))


def length(v1):
    return sqrt(v1[0]**2 + v1[1]**2)


def scale(c, vectors):
    return [(v[0] * c, v[1] * c) for v in vectors]


def subtract(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])


def transpose(t, vectors):
    return [add(t, v) for v in vectors]


def to_cartesian(polar_vector):
    length, angle = polar_vector[0], polar_vector[1]
    return (length * cos(angle), length * sin(angle))


def to_polar(cartesian_vector):
    x, y = cartesian_vector[0], cartesian_vector[1]
    angle = atan2(y, x)
    return (length(cartesian_vector), angle)


def rotate(angle, vectors):
    polars = [to_polar(v) for v in vectors]
    rotated_polars = [(l, a+angle) for l, a in polars]
    return [to_cartesian(v) for v in rotated_polars]


def to_radians(angle):
    return (angle/180.0) * pi

if __name__ == "__main__":
    print(add((1, 2), (3, 4)))
    print(to_cartesian((5, to_radians(37))))
    print(scale(3, [(1, 2), (3, 4), (5, 6)]))
