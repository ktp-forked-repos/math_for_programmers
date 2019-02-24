import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


class Points():
    def __init__(self, vectors, colour='black'):
        self.vectors = list(vectors)
        self.colour = colour

    def draw(self):
        xs = [v[0] for v in self.vectors]
        ys = [v[1] for v in self.vectors]
        plt.scatter(xs, ys)
