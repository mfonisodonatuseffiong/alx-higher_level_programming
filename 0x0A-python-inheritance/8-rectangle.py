<<<<<<< HEAD

#!/usr/bin/python3
"""Contains a class that inherits from `BaseGeometry"""

=======
#!/usr/bin/python3
"""Inheris from baseGeometry"""
>>>>>>> 58f9a67cb1a269562fdc796162ac1a88f914f3e5
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
<<<<<<< HEAD
        """Inherits from `BaseGeometry `"""

            def __init__(self, width, height):
                        """Initialize rectangle value"""
                                self.integer_validator("width", width)
                                        self.__width = width
                                                self.integer_validator("height", height)
                                                        self.__height = height

                                                        #!/usr/bin/python3
                                                        """Contains a class that inherits from `BaseGeometry"""

                                                        BaseGeometry = __import__('7-base_geometry').BaseGeometry


                                                        class Rectangle(BaseGeometry):
                                                                """Inherits from `BaseGeometry `"""

                                                                    def __init__(self, width, height):
                                                                                """Initialize rectangle value"""
                                                                                        self.integer_validator("width", width)
                                                                                                self.__width = width
                                                                                                        self.integer_validator("height", height)
                                                                                                                self.__height = height

=======
    """a class to define rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
>>>>>>> 58f9a67cb1a269562fdc796162ac1a88f914f3e5
