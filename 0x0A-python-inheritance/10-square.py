<<<<<<< HEAD

#!/usr/bin/python3
"""Module contains implementation of `Square` class"""
=======
#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
>>>>>>> 58f9a67cb1a269562fdc796162ac1a88f914f3e5
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
<<<<<<< HEAD
        """Inherits from class `Rectangle`"""
            def __init__(self, size):
                        """Initializes the values"""
                                self.integer_validator("size", size)
                                        self.__size = size
                                                super().__init__(self.__size, self.__size)

                                                #!/usr/bin/python3
                                                """Module contains implementation of `Square` class"""
                                                Rectangle = __import__('9-rectangle').Rectangle


                                                class Square(Rectangle):
                                                        """Inherits from class `Rectangle`"""
                                                            def __init__(self, size):
                                                                        """Initializes the values"""
                                                                                self.integer_validator("size", size)
                                                                                        self.__size = size
                                                                                                super().__init__(self.__size, self.__size)

=======
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size 
>>>>>>> 58f9a67cb1a269562fdc796162ac1a88f914f3e5
