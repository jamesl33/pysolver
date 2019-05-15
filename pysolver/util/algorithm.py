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


class Algorithm():
    """Algorithms which will be used on a Rubik's cube and are stored as
    a set of steps using the standard Rubik's cube notation which can be found
    here https://ruwix.com/the-rubiks-cube/notation/.

    Arguments:
        step (str): Space separated list of steps.
    """
    def __init__(self, steps):
        self._steps = steps.split()

    @property
    def steps(self):
        """Get the list of steps that make up the algorithm

        Returns:
            (list): A list Rubik's cube moves using the standard notation.
        """
        return self._steps

    def reverse(self):
        """Get a copy of the algorithm which has been reversed.

        Returns:
            (list): The reversed version of the algorithm.
        """
        return self._steps[::-1]

    def __iter__(self):
        """Allow iterating over the steps in the algorithm.

        Returns:
            (iter): The steps that make up the algorithm.
        """
        return iter(self._steps)

    def __str__(self):
        """Get a human readable version of the algorithm.

        Returns:
            (str): A space seperated list of Rubik's cube moves.
        """
        return ' '.join(self._steps)


SLEDGE = Algorithm("R U R' U'")
