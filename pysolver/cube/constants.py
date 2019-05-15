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

import numpy as np


# axis vectors
X_AXIS = np.array([1, 0, 0])
Y_AXIS = np.array([0, 1, 0])
Z_AXIS = np.array([0, 0, 1])

# cube face vectors
UP = np.array([0, 1, 0])
DOWN = np.array([0, -1, 0])
RIGHT = np.array([1, 0, 0])
LEFT = np.array([-1, 0, 0])
FRONT = np.array([0, 0, 1])
BACK = np.array([0, 0, -1])

# piece types
FACE = 0
EDGE = 1
CORNER = 2

# rotation matrices
ROT_YZ = np.array([
    [1, 0, 0],
    [0, 0, 1],
    [0, -1, 0]
])

ROT_YZ_PRIME = np.array([
    [1, 0, 0],
    [0, 0, -1],
    [0, 1, 0]
])

ROT_XZ = np.array([
    [0, 0, -1],
    [0, 1, 0],
    [1, 0, 0]
])

ROT_XZ_PRIME = np.array([
    [0, 0, 1],
    [0, 1, 0],
    [-1, 0, 0]
])

ROT_XY = np.array([
    [0, 1, 0],
    [-1, 0, 0],
    [0, 0, 1]
])

ROT_XY_PRIME = np.array([
    [0, -1, 0],
    [1, 0, 0],
    [0, 0, 1]
])
