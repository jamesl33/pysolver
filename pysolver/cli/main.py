#!/usr/bin/env python3
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

import argparse

from ..cube.cube import Cube, InvalidCubeString


def run_pysolver():
    """Run the command line interface for pysolver."""
    parser = argparse.ArgumentParser(
        description="Python Rubik's cube solver which makes use of the CFOP \
            solving strategy.",
        prog='pysolver'
    )

    parser.add_argument(
        'cube_string',
        action='store',
        help="string representation of the Rubik's cubes current state",
        type=str
    )

    arguments = parser.parse_args()

    try:
        cube = Cube(arguments.cube_string)
    except InvalidCubeString:
        print('Error: Input cube is not valid')
