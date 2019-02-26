from math import sqrt


def add(*vectors):
    by_coordinate = zip(*vectors)
    coordinate_sums = [sum(coords) for coords in by_coordinate]
    return tuple(coordinate_sums)


def scale(s, vector):
    return tuple(v * s for v in vector)


def length(v):
    return sqrt(sum([coord ** 2 for coord in v]))


def dot(vector1, vector2):
    return sum([v1 * v2 for v1, v2 in zip(vector1, vector2)])

if __name__ == "__main__":
    print(add((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)))
    print(scale(5, (1, 2, 3)))
    print(length((3, 4, 12)))  # == 13
    print(dot((1, 2, -1), (3, 0, 3)))  # == 0
