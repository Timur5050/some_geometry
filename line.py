# line.py
# -*- coding: windows-1251 -*-

import matplotlib.pyplot as plt
from point import Point


class Line:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.ind = 0
        if self.B.x - self.A.x != 0:
            self.slope = (self.B.y - self.A.y) / (self.B.x - self.A.x)
            self.intercept = self.A.y - self.slope * self.A.x
        else:
            self.ind = 1
            self.slope = float('inf')
            self.intercept = None

    def distance(self):
        return round(float(((self.A.x - self.B.x) ** 2 + (self.A.y - self.B.y) ** 2) ** 0.5), 3)

    def position(self, C):
        if self.ind == 1:
            return "Точка праворуч" if self.A.x < C.x else "Точка ліворуч"
        elif self.slope == 0:
            return "Точка вище" if self.A.y < C.y else "Точка нижче"
        else:
            if self.slope > 0:
                return "Точка вище" if C.y > self.slope * C.x + self.intercept else "Точка нижче"
            else:
                return "Точка вище" if C.y > self.slope * C.x + self.intercept else "Точка нижче"

    def solve(self, C):
        self.build_graphic(Line(C, C))
        PC = self.crossing(C)
        normal_line = Line(C, PC)
        dist = normal_line.distance()
        self.build_graphic(normal_line)
        return dist

    def crossing(self, C):
        if self.ind == 1:
            return Point(self.A.x, C.y)
        elif self.slope == 0:
            return Point(C.x, self.intercept)
        else:
            normal_slope = -1 / self.slope
            normal_intercept = C.y - normal_slope * C.x
            x_cross = (normal_intercept - self.intercept) / (self.slope - normal_slope)
            y_cross = self.slope * x_cross + self.intercept
            return Point(x_cross, y_cross)

    def build_graphic(self, line, save_path=None):
        plt.subplots_adjust(0.08, 0.05, 0.76, 0.95)
        points = [self.A.x, self.B.x, self.A.y, self.B.y, line.A.x, line.B.x, line.A.y, line.B.y]
        size = max(abs(min(points)), abs(max(points))) + 1
        plt.xlim(-size, size)
        plt.ylim(-size, size)
        plt.grid()
        plt.axhline()
        plt.axvline()

        lx = []
        ly = []
        i = -size

        if self.ind != 1:
            while i <= size:
                y_val = self.slope * i + self.intercept
                if -size < y_val < size:
                    lx.append(i)
                    ly.append(y_val)
                i += 1
        else:
            lx = [self.A.x, self.B.x]
            ly = [-size, size]

        nx = [line.A.x, line.B.x]
        ny = [line.A.y, line.B.y]

        plt.plot(lx, ly, color='green')
        plt.plot(nx, ny, color='red')
        plt.scatter([self.A.x, self.B.x, line.A.x, line.B.x],
                    [self.A.y, self.B.y, line.A.y, line.B.y],
                    color=['green', 'green', 'red', 'red'])

        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()
