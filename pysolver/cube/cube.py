#!/usr/bin/env python3
"""
This file is part of pysolver.

Copyright (C) 2019, James Lee <jamesl33info@gmail.com>.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import string

from .constants import (X_AXIS, Y_AXIS, Z_AXIS, UP, DOWN, RIGHT, LEFT, FRONT,
                        BACK, ROT_YZ, ROT_YZ_PRIME, ROT_XZ, ROT_XZ_PRIME,
                        ROT_XY, ROT_XY_PRIME)
from .piece import Piece
from ..util.algorithm import Algorithm


class InvalidCubeString(Exception):
    """This exception is raised when the given cube string does not
    represent a valid Rubik's cube.
    """
    pass

class Cube():
    """Rubik's cube object accurately represents the Rubik's cube. All of the
    rotation functions follow the Rubik's cube stadard notation which can be
    found here https://ruwix.com/the-rubiks-cube/notation/.

    Arguments:
        cs (str): String representation of the Rubik's cube as seen below.

        BBB                         0,  1,  2,
        BBB                         3,  4,  5,
        BBB                         6,  7,  8,

    LLL UUU RRR DDD     9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    LLL UUU RRR DDD     21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
    LLL UUU RRR DDD     33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,

        FFF                         45, 46, 47,
        FFF                         48, 49, 50,
        FFF                         51, 52, 53

    Examples of correct unsolved cube strings.

       'RWR
        GOR
        RWO

    BRB WBB YWW GGY
    YBO WYG YGR YWO
    YGB WBG ORG YOR

        OYW
        ORB
        GBO'

    'RWRGORRWOBRBWBBYWWGGYYBOWYGYGRYWOYGBWBGORGYOROYWORBGBO'
    """
    def __init__(self, cs):
        # remove any whitespace from the cube string.
        cs = [char for char in cs if char not in string.whitespace]

        # check too see if we can make a cube from the given cube string.
        if not self.valid_cube_string(cs):
            raise InvalidCubeString

        self._faces = set()
        self._edges = set()
        self._corners = set()

        # create the face pieces from colors in the cube string.
        self._faces.add(Piece(BACK, [None, None, cs[4]]))
        self._faces.add(Piece(LEFT, [cs[22], None, None]))
        self._faces.add(Piece(UP, [None, cs[25], None]))
        self._faces.add(Piece(RIGHT, [cs[28], None, None]))
        self._faces.add(Piece(DOWN, [None, cs[31], None]))
        self._faces.add(Piece(FRONT, [None, None, cs[49]]))

        # create the edge pieces from colors in the cube string.
        self._edges.add(Piece(FRONT + UP, [None, cs[37], cs[46]]))
        self._edges.add(Piece(BACK + UP, [None, cs[13], cs[7]]))
        self._edges.add(Piece(LEFT + UP, [cs[23], cs[24], None]))
        self._edges.add(Piece(RIGHT + UP, [cs[27], cs[26], None]))
        self._edges.add(Piece(BACK + LEFT, [cs[10], None, cs[3]]))
        self._edges.add(Piece(BACK + RIGHT, [cs[16], None, cs[5]]))
        self._edges.add(Piece(LEFT + FRONT, [cs[34], None, cs[48]]))
        self._edges.add(Piece(RIGHT + FRONT, [cs[40], None, cs[50]]))
        self._edges.add(Piece(FRONT + DOWN, [None, cs[43], cs[52]]))
        self._edges.add(Piece(BACK + DOWN, [None, cs[19], cs[1]]))
        self._edges.add(Piece(LEFT + DOWN, [cs[21], cs[32], None]))
        self._edges.add(Piece(RIGHT + DOWN, [cs[29], cs[30], None]))

        # create the corner pieces from colors in the cube string.
        self._corners.add(Piece(UP + LEFT + FRONT, [cs[35], cs[36], cs[45]]))
        self._corners.add(Piece(UP + RIGHT + FRONT, [cs[39], cs[38], cs[47]]))
        self._corners.add(Piece(UP + LEFT + BACK, [cs[11], cs[12], cs[6]]))
        self._corners.add(Piece(UP + RIGHT + BACK, [cs[15], cs[14], cs[8]]))
        self._corners.add(Piece(DOWN + LEFT + FRONT, [cs[33], cs[44], cs[51]]))
        self._corners.add(
            Piece(DOWN + RIGHT + FRONT, [cs[41], cs[42], cs[53]]))
        self._corners.add(Piece(DOWN + LEFT + BACK, [cs[9], cs[20], cs[0]]))
        self._corners.add(Piece(DOWN + RIGHT + BACK, [cs[17], cs[18], cs[2]]))

        self._pieces = self._faces | self._edges | self._corners

        # check too see if the cube string produced an accurate Rubik's cube.
        if not self._valid_cube():
            raise InvalidCubeString

    def do_algorithm(self, algorithm):
        """Perform all of the steps of an algorithm.

        Arguments:
            algorithm (Algorithm): The algorithm to perform.
        """
        assert isinstance(algorithm, Algorithm)

    def rotate_l(self, prime=False):
        """Rotate the left face of the cube 90 degrees.

        Arguments:
            prime (bool): True if rotating the opposite way. e.g. l'
        """
        if prime:
            self._rotate_face(LEFT, ROT_YZ_PRIME)
        else:
            self._rotate_face(LEFT, ROT_YZ)

    def rotate_r(self, prime=False):
        """Rotate the right face of the cube 90 degrees.

        Arguments:
            prime (bool): True if rotating the opposite way. e.g. r'
        """
        if prime:
            self._rotate_face(RIGHT, ROT_YZ_PRIME)
        else:
            self._rotate_face(RIGHT, ROT_YZ)

    def rotate_u(self, prime=False):
        """Rotate the upper face of the cube 90 degrees.

        Arguments:
            prime (bool): True if rotating the opposite way. e.g. u'
        """
        if prime:
            self._rotate_face(UP, ROT_XZ_PRIME)
        else:
            self._rotate_face(UP, ROT_XZ)

    def rotate_d(self, prime=False):
        """Rotate the bottom/down face of the cube 90 degrees.

        Arguments:
            prime (bool): True if rotating the opposite way. e.g. d'
        """
        if prime:
            self._rotate_face(DOWN, ROT_XZ_PRIME)
        else:
            self._rotate_face(DOWN, ROT_XZ)

    def rotate_f(self, prime=False):
        """Rotate the front face of the cube 90 degrees.

        Arguments:
            prime (bool): True if rotating the opposite way. e.g. f'
        """
        if prime:
            self._rotate_face(FRONT, ROT_XY_PRIME)
        else:
            self._rotate_face(FRONT, ROT_XY)

    def rotate_b(self, prime=False):
        """Rotate the back face of the cube 90 degrees.

        Arguments:
            prime (bool): True if rotating the opposite way. e.g. b'
        """
        if prime:
            self._rotate_face(BACK, ROT_XY_PRIME)
        else:
            self._rotate_face(BACK, ROT_XY)

    def rotate_m(self, prime=False):
        """Rotate the m slice 90 degrees.

        Arguments:
            prime (bool): True if rotating the opposite way. e.g. m'
        """
        if prime:
            self._rotate_slice(Y_AXIS + Z_AXIS, ROT_YZ_PRIME)
        else:
            self._rotate_slice(Y_AXIS + Z_AXIS, ROT_YZ)

    def rotate_e(self, prime=False):
        """Rotate the e slice 90 degrees.

        Arguments:
            prime (bool): True if rotating the opposite way. e.g. e'
        """
        if prime:
            self._rotate_slice(X_AXIS + Z_AXIS, ROT_XZ_PRIME)
        else:
            self._rotate_slice(X_AXIS + Z_AXIS, ROT_XZ)

    def rotate_s(self, prime=False):
        """Rotate the s slice 90 degrees.

        Arguments:
            prime (bool): True if rotating the opposite way. e.g. s'
        """
        if prime:
            self._rotate_slice(X_AXIS + Y_AXIS, ROT_XY_PRIME)
        else:
            self._rotate_slice(X_AXIS + Y_AXIS, ROT_XY)

    def rotate_x(self, prime=False):
        """Rotate the whole cube on the x axis.

        Arguments:
            prime (bool): True if rotating the opposite way. e.g. x'
        """
        if prime:
            self._rotate_cube(ROT_YZ_PRIME)
        else:
            self._rotate_cube(ROT_YZ)

    def rotate_y(self, prime=False):
        """Rotate the whole cube on the y axis.

        Arguments:
            prime (bool): True if rotating the opposite way. e.g. y'
        """
        if prime:
            self._rotate_cube(ROT_XZ_PRIME)
        else:
            self._rotate_cube(ROT_XZ)

    def rotate_z(self, prime=False):
        """Rotate the whole cube on the z axis.

        Arguments:
            prime (bool): True if rotating the opposite way. e.g. z'
        """
        if prime:
            self._rotate_cube(ROT_XY_PRIME)
        else:
            self._rotate_cube(ROT_XY)

    def _rotate_face(self, face, matrix):
        """Rotate a specific face using a rotation matrix.

        Arguments:
            face (np.array): One of the constants FRONT, BACK, LEFT, RIGHT,
                UP, DOWN.
            matrix (np.ndarray): The rotation which will be applied to each
                piece.
        """
        for piece in self._face(face):
            piece.rotate(matrix)

    def _rotate_slice(self, plane, matrix):
        """Rotate a specific slice using a rotation matrix.

        Arguments:
            plane (np.array): The plane of rotation. Will be a comination of
                two constants. e.g. X_AXIS + Y_AXIS
            matrix (np.ndarray): The rotation which will be applied to each
                piece.
        """
        for piece in self._slice(plane):
            piece.rotate(matrix)

    def _rotate_cube(self, matrix):
        """Rotate the whole cube using a rotation matrix.

        Arguments:
            matrix (np.ndarray): The rotation which will be applied to each
                piece.
        """
        for piece in self._pieces:
            piece.rotate(matrix)

    def _face(self, face):
        """Get all the pieces on one face of the cube.

        Arguments:
            face (np.array): One of the constants FRONT, BACK, LEFT, RIGHT,
                UP, DOWN.
        """
        face_pieces = set()

        for piece in self._pieces:
            if list(abs(piece.position + face)).count(2) == 1:
                face_pieces.add(piece)

        return face_pieces

    def _slice(self, plane):
        """Get all the pieces in a slice on the cube e.g the 'm' slice.

        Arguments:
            plane (np.array): The plane of rotation. Will be a comination of
                two constants. e.g. X_AXIS + Y_AXIS
        """
        slice_pieces = set()

        for index, value in enumerate(plane):
            if value == 0:
                for piece in self._pieces:
                    if piece.position[index] == 0:
                        slice_pieces.add(piece)

        return slice_pieces

    def _valid_cube(self):
        """Advanced verification to make sure that the current cube object is
        in fact a valid Rubik's cube.

        Returns:
            (bool): True if the cube is valid.
        """
        return True

    def __iter__(self):
        """Iterate over the pieces of the cube when iterating over the cube
        object.

        Returns:
            (iter): All the cubes pieces.
        """
        return iter(self._pieces)

    def __str__(self):
        """Get a string representation of the Rubik's cube. This will be in
        the same format as when the cube was input into the program.

        Returns:
            (str): A cube string representing the current state of the cube.
        """
        color_list = []
        face_colors = {'back': [], 'up': [], 'left': [], 'right': [],
                       'down': [], 'front': []}

        for piece in sorted(self._face(BACK), key=lambda p: (p.y, p.x)):
            face_colors['back'].append(piece.colors[2])

        for piece in sorted(self._face(UP), key=lambda p: (p.z, p.x)):
            face_colors['up'].append(piece.colors[1])

        for piece in sorted(self._face(LEFT), key=lambda p: (p.z, p.y)):
            face_colors['left'].append(piece.colors[0])

        for piece in sorted(self._face(RIGHT), key=lambda p: (p.z, -p.y)):
            face_colors['right'].append(piece.colors[0])

        for piece in sorted(self._face(DOWN), key=lambda p: (p.z, -p.x)):
            face_colors['down'].append(piece.colors[1])

        for piece in sorted(self._face(FRONT), key=lambda p: (-p.y, p.x)):
            face_colors['front'].append(piece.colors[2])

        color_list += face_colors['back']

        for index in range(0, 9, 3):
            for face in ['left', 'up', 'right', 'down']:
                color_list += face_colors[face][index:index + 3]

        color_list += face_colors['front']

        return ''.join(color_list)

    @classmethod
    def valid_cube_string(cls, cube_string):
        """Naive verification to see if the cube string can produce a Cube
        object.

        Arguments:
            cube_string (str): The string representation of the cubes colors.

        Returns:
            (bool): True if the cube string is valid.
        """
        valid = True

        # verify we have enough sticker colors.
        if len(cube_string) != 54:
            valid = False

        # verify we have 9 of each color.
        colors = {'R': 0, 'G': 0, 'B': 0, 'O': 0, 'W': 0, 'Y': 0}

        for element in cube_string:
            colors[element] += 1

        for _, count in colors.items():
            if count != 9:
                valid = False

        return valid
