<<<<<<< HEAD

#!/usr/bin/python3
"""Contains a `BaseGeometry` class"""


class BaseGeometry():
        """An empty BaseGeometry class"""

            def area(self):
                        """Calculates the area of the geometry"""
                                raise Exception('area() is not implemented')

                                def integer_validator(self, name, value):
                                            """Validates the `value`"""
                                                    if type(value) != int:
                                                                    raise TypeError("{} must be an integer".format(name))
                                                                        if value <= 0:
                                                                                        raise ValueError("{} must be greater than 0".format(name))

                                                                                    #!/usr/bin/python3
                                                                                    """Contains a `BaseGeometry` class"""


                                                                                    class BaseGeometry():
                                                                                            """An empty BaseGeometry class"""

                                                                                                def area(self):
                                                                                                            """Calculates the area of the geometry"""
                                                                                                                    raise Exception('area() is not implemented')

                                                                                                                    def integer_validator(self, name, value):
                                                                                                                                """Validates the `value`"""
                                                                                                                                        if type(value) != int:
                                                                                                                                                        raise TypeError("{} must be an integer".format(name))
                                                                                                                                                            if value <= 0:
                                                                                                                                                                            raise ValueError("{} must be greater than 0".format(name))

=======
#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """this class represents a base geometry"""

    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
>>>>>>> 58f9a67cb1a269562fdc796162ac1a88f914f3e5
