def add(*vectors):
    by_coordinate = zip(*vectors)
    coordinate_sums = [sum(coords) for coords in by_coordinate]
    return tuple(coordinate_sums)


def scale(s, vector):
    return tuple(v * s for v in vector)

if __name__ == "__main__":
    print(add((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)))
    print(scale(5, (1, 2, 3)))
