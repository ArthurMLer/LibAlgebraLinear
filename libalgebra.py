# "imports"
from __future__ import annotations
from math import sqrt


# "Class that determines the parameters x,y and z"
class Vector:
    # "Definition of the x,y,z parameters"
    def __init__(self: Vector, x: int | float, y: int | float, z: int | float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self: Vector) -> str:
        return f"[{self.x}, {self.y}, {self.z}]"

    def __str__(self: Vector) -> str:
        return self.__repr__()

    # "Adition operation"
    def __add__(self: Vector, other: Vector) -> Vector:
        """
        Puts in place an add method.

        Parameters
        ----------------------------
        Other:Vector
            Another vector

        Return
        ------
        New vector
            Result of the operation
        """
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    # "Subtraction operation"
    def __sub__(self: Vector, othersub: Vector) -> Vector:
        """
        Puts in place an subtraction method.

        Parameters
        ----------
        Other:Vector
            Another vector

        Return
        ------
        New vector
            Result of the operation
        """
        return Vector(self.x - othersub.x, self.y - othersub.y, self.z - othersub.z)

    # "Multiplication operation"
    def __rmul__(self: Vector, escalar: int | float) -> Vector:
        """
        Does the multiplication function.

        Parameters
        ----------
        Number
            Number that the vector is multiplied by

        Return
        ------
        A new vector
            The result of the operation
        """
        return Vector(self.x * escalar, self.y * escalar, self.z * escalar)

    def dotproduct(self: Vector, other: Vector) -> Vector:
        """
        Does the dot product of the vector.

        Parameters
        ----------
        other:vector
            Another vector

        Return
        ------
        A new vector
            Result of the operation
        """
        return float(self.x * other.x + self.y * other.y + self.z * other.z)

    # "Cross product by vectors operation"
    def crossproduct(self: Vector, other: Vector) -> Vector:
        """
        Does the cross-product of two vectors.

        Parameters
        ----------

        other: Vetor
            Another vector

        Return
        ------

        A new vector
            Result of the operation
        """

        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def length(self: Vector) -> int | float:
        """
        Lenght of modules

        Parameters
        ----------
        self: Vector
            Uses only one vector

        Return
        ------
            An scalar
                Returns the square root of the sum of the x, y, z parameters squared
        """
        return sqrt(self.x**2 + self.y**2 + self.z**2)
