"""Sierpinski tetrahedron

:Authors:
    - frootin
"""

from math import cos, sin
from itertools import combinations
from random import randint
from typing import Tuple, List
import numpy as np
import pygame as pg


SIDE = 800
SCALE = 250
ROTATE_SPEED = 0.02
MAX_ITERS = 4
MIN_ITERS = 0


class Tetrahedron():
    """Class for drawing Sierpinski tetrahedron located at the origin of the coordinate system"""
    projection_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]

    start_points = [[[-1], [0], [-2**(-0.5)]],
              [[1], [0], [-2**(-0.5)]],
              [[0], [-1], [2**(-0.5)]],
              [[0], [1], [2**(-0.5)]]]

    def __init__(self, window: pg.Surface, scale: int, colors: List[Tuple[int]]) -> None:
        self.window = window
        self.colors = colors
        self.scale = scale
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0
        self.rotation_x = [[]]
        self.rotation_y = [[]]
        self.rotation_z = [[]]

    def connect_points(self, i: int, j: int, points: List[Tuple[float]]):
        """Draw a line between two 3d points"""
        pg.draw.line(self.window, (255, 255, 255), (points[i][0], points[i][1]) , (points[j][0], points[j][1]))

    @staticmethod
    def matrices_to_coordinates(matrices: List[List[List[float]]]):
        """Convert column matrices to coordinates"""
        points = []
        for matrix in matrices:
            cord = [elem[0] for elem in matrix]
            points.append(cord)
        return points

    @staticmethod
    def coordinates_to_matrices(points: List[Tuple[float]]):
        """Convert coordinates to column matrices"""
        matrices = []
        for cords in points:
            tetra_point = [[cord] for cord in cords]
            matrices.append(tetra_point)
        return matrices

    def draw_tetra(self, tetra_points: List[Tuple[float]]):
        """Draw simple tetrahedron with list of points"""
        self.rotation_x = np.matrix([[1, 0, 0],
                    [0, cos(self.angle_x), -sin(self.angle_x)],
                    [0, sin(self.angle_x), cos(self.angle_x)]])

        self.rotation_y = np.matrix([[cos(self.angle_y), 0, sin(self.angle_y)],
                    [0, 1, 0],
                    [-sin(self.angle_y), 0, cos(self.angle_y)]])

        self.rotation_z = np.matrix([[cos(self.angle_z), -sin(self.angle_z), 0],
                    [sin(self.angle_z), cos(self.angle_z), 0],
                    [0, 0, 1]])

        points = []

        for point in tetra_points:
            rotate_x = np.matmul(self.rotation_x, point)
            rotate_y = np.matmul(self.rotation_y, rotate_x)
            rotate_z = np.matmul(self.rotation_z, rotate_y)
            point_2d = np.matmul(self.projection_matrix, rotate_z).tolist()

            window_size = self.window.get_size()
            x = (point_2d[0][0] * self.scale) + window_size[0] / 2
            y = (point_2d[1][0] * self.scale) + window_size[1] / 2

            points.append((x, y))
            pg.draw.circle(self.window, (255, 0, 0), (x, y), 0)

        triangles = combinations(points, 3)
        for triangle in triangles:
            pg.draw.polygon(self.window, self.colors[randint(0, len(self.colors) - 1)], (triangle[0], triangle[1], triangle[2]))

        lines = combinations([0, 1, 2, 3], 2)
        for line in lines:
            self.connect_points(*line, points)

    @staticmethod
    def find_medium(v1: Tuple[float], v2: Tuple[float]):
        """Find a middle point between two 3d points"""
        v12 = [0, 0, 0]
        v12[0], v12[1], v12[2] = (v1[0] + v2[0]) / 2, (v1[1] + v2[1]) / 2, (v1[2] + v2[2]) / 2
        return v12

    def divide_tetra(self, v1: Tuple[float], v2: Tuple[float], v3: Tuple[float], v4: Tuple[float], n: int):
        """Draw Sierpinski tetrahedron given start coordinates and number of iterations n"""
        if n > 0:
            v12 = self.find_medium(v1, v2)
            v13 = self.find_medium(v1, v3)
            v14 = self.find_medium(v1, v4)
            self.divide_tetra(v1, v12, v13, v14, n - 1)
            v23 = self.find_medium(v2, v3)
            v24 = self.find_medium(v2, v4)
            self.divide_tetra(v2, v12, v23, v24, n - 1)
            v34 = self.find_medium(v3, v4)
            self.divide_tetra(v3, v13, v23, v34, n - 1)
            self.divide_tetra(v4, v14, v24, v34, n - 1)
        else:
            points = self.coordinates_to_matrices((v1, v2, v3, v4))
            self.draw_tetra(points)

    def draw_Sierpinski(self, n: int):
        """Draw Sierpinski tetrahedron given number of iterations n (start points defined in the class)"""
        points = self.matrices_to_coordinates(self.start_points)
        self.divide_tetra(*points, n)


def palette(colors: int):
    """Return one of palettes"""
    sunset = [(165, 0, 98), (255, 155, 85), (212, 97, 166), (214, 41, 0)]
    viburnum = [(0, 0, 0), (255, 0, 0)]
    mirrorball = [(0, 56, 168), (155, 79, 150), (214, 2, 112)]
    witch = [(0, 100, 0), (128, 0, 128), (0, 0, 0)]

    palettes = [sunset, mirrorball, witch, viburnum]

    return palettes[colors % len(palettes)]


def run_animation():
    """Init pygame and draw animated Sierpinski tetrahedron"""
    pg.init()
    running = True
    window = pg.display.set_mode((SIDE, SIDE))
    clock = pg.time.Clock()
    iters = 0
    colors = 0
    tetra = Tetrahedron(window, SCALE, palette(colors))
    while running:
        clock.tick(60)
        window.fill((0, 0, 0))
        tetra.draw_Sierpinski(iters)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.MOUSEBUTTONUP:
                #wheel down to increase number of iterations
                if event.button == 4:
                    iters += 1
                    if iters > MAX_ITERS:
                        iters = MIN_ITERS
                #wheel up to decrease number of iterations
                elif event.button == 5:
                    iters -= 1
                    if iters < MIN_ITERS:
                        iters = MAX_ITERS
                #change colors set
                elif event.button == 1:
                    colors += 1
                    tetra.colors = palette(colors)

            #rotate by mouse
            if event.type == pg.MOUSEMOTION:
                tetra.angle_x -= event.rel[0] * ROTATE_SPEED
                tetra.angle_y -= event.rel[1] * ROTATE_SPEED

            #rotate by keys
            keys = pg.key.get_pressed()
            if keys[pg.K_r]:
                tetra.angle_y = tetra.angle_x = tetra.angle_z = 0
            if keys[pg.K_a]:
                tetra.angle_y += ROTATE_SPEED
            if keys[pg.K_d]:
                tetra.angle_y -= ROTATE_SPEED
            if keys[pg.K_w]:
                tetra.angle_x += ROTATE_SPEED
            if keys[pg.K_s]:
                tetra.angle_x -= ROTATE_SPEED
            if keys[pg.K_q]:
                tetra.angle_z -= ROTATE_SPEED
            if keys[pg.K_e]:
                tetra.angle_z += ROTATE_SPEED

        pg.display.update()

    pg.quit()


def main():
    """Show instructions and ask for proceeding"""
    print("INSTRUCTION:\n")
    print("Left click to change colors;")
    print("Wheel to change number of iterations;")
    print("Move cursor to rotate OR try pressing one of the following: A, D, W, S, Q, E, R.\n")
    option = input("Want to proceed? Enter 'y', otherwise the program will exit: ")
    if option == "y":
        run_animation()
    print("Exit.")


if __name__ == "__main__":
    main()
