#!/usr/bin/python3
<<<<<<< HEAD
"""Contains a class that inherits from `BaseGeometry"""

=======
"""Defines a class Rectangle that inherits from BaseGeometry."""
>>>>>>> 58f9a67cb1a269562fdc796162ac1a88f914f3e5
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
<<<<<<< HEAD
        """Inherits from `BaseGeometry`"""

            def __init__(self, width, height):
                        """Initialize rectangle values"""
                                self.integer_validator("width", width)
                                        self.__width = width
                                                self.integer_validator("height", height)
                                                        self.__height = height

                                                            def area(self):
                                                                        """Calculates the area of the geometry"""
                                                                                return (self.__width * self.__height)

                                                                                def __str__(self):
                                                                                            """Prints the description of the `Rectangle`"""
                                                                                                    string = "[Rectangle] {}/{}".format(self.__width, self.__height)
                                                                                                            return string#!/usr/bin/python3
                                                                                                        """Contains a class that inherits from `BaseGeometry"""

                                                                                                        BaseGeometry = __import__('7-base_geometry').BaseGeometry


                                                                                                        class Rectangle(BaseGeometry):
                                                                                                                """Inherits from `BaseGeometry`"""

                                                                                                                    def __init__(self, width, height):
                                                                                                                                """Initialize rectangle values"""
                                                                                                                                        self.integer_validator("width", width)
                                                                                                                                                self.__width = width
                                                                                                                                                        self.integer_validator("height", height)
                                                                                                                                                                self.__height = height

                                                                                                                                                                    def area(self):
                                                                                                                                                                                """Calculates the area of the geometry"""
                                                                                                                                                                                        return (self.__width * self.__height)

                                                                                                                                                                                        def __str__(self):
                                                                                                                                                                                                    """Prints the description of the `Rectangle`"""
                                                                                                                                                                                                            string = "[Rectangle] {}/{}".format(self.__width, self.__height)
                                                                                                                                                                                                                    return string
=======
    """this class represents a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new rectangle"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the print() and str() representation of a Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
>>>>>>> 58f9a67cb1a269562fdc796162ac1a88f914f3e5
