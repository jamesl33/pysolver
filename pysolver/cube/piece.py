#!/usr/bin/python3
"""
This file is part of pysolver.

Copyright (C) 2018, James Lee <jamesl33info@gmail.com>.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

import numpy as np


class Piece():
    """A single piece from a Rubik's cube which can be rotated just
    like a piece on a normal Rubik's cube.

    Arguments:
        position (np.array): x, y, z position of the piece.
        colors (np.array): x, y, z sticker colors.

    Attributes:
        _position (np.array): x, y, z position of the cube piece where 0, 0, 0
            is the centre of the cube.
        _colors (np.array): x, y, z sticker colors where x: left < 0 > right,
            y: down < 0 > up, z: back < 0 > front.
        _type (int): Which type of piece is being represented. This value
            directly corresponds to the constant values for FACE, EGDE and
            CORNER.
    """
    def __init__(self, position, colors):
        self._position = position
        self._colors = colors
        self._type = np.count_nonzero(colors) - 1

    @property
    def x(self):  # pylint: disable-msg=C0103
        """Get the x coordinate for the cube piece.

        Returns:
            (int): The pieces current x coordinate.
        """
        return self._position[0]

    @property
    def y(self):  # pylint: disable-msg=C0103
        """Get the y coordinate for the cube piece.

        Returns:
            (int): The pieces current y coordinate.
        """
        return self._position[1]

    @property
    def z(self):  # pylint: disable-msg=C0103
        """Get the z coordinate for the cube piece.

        Returns:
            (int): The pieces current z coordinate.
        """
        return self._position[2]

    @property
    def position(self):
        """Get the pieces current position; useful when searching for a piece
        on the cube.

        Returns:
            (tuple {int}): The current position of the piece.
        """
        return tuple(self._position)

    @property
    def colors(self):
        """Get the pieces current colors as a tuple.

        Returns:
            (tuple {int}): The current colors for the piece.
        """
        return tuple(self._colors)

    def rotate(self, rotation_matrix):
        """Rotate the cube piece using a valid rotation matrix.

        Arguments:
            rotation_matrix (np.ndarray): A valid rotation matrix.
        """
        new_pos = np.matmul(rotation_matrix, self._position)
        rotated = new_pos - self._position

        # update the colors to match the rotation where
        # the two non zero values should be swapped
        if np.count_nonzero(rotated):
            if np.count_nonzero(rotated) == 1:
                rotated += np.matmul(rotation_matrix, rotated)

            # get the indices of the colors that need swapping
            index_a, index_b = [i for i, v in enumerate(rotated) if v != 0]

            self._colors[index_a], self._colors[index_b] = \
                self._colors[index_b], self._colors[index_a]

        self._position = new_pos

    def __repr__(self):
        """Get a detailed representation of the cube piece.

        Returns:
            (str): The type of piece followed by its position and colors.
        """
        return 'Type: {0}, {1}, {2}'.format(self._type, self._position,
                                            self._colors)
