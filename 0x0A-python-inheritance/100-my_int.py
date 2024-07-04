#!/usr/bin/python3
<<<<<<< HEAD
"""Contains a class `MyInt` that inherits from `int`"""


class MyInt(int):
        """Inherits from int base class"""
            def __init__(self, value):
                        """Initialize value"""
                                self.value = value

                                    def __ne__(self, x):
                                                """not equal to comparison"""
                                                        if self.value is x:
                                                                        return True

                                                                        def __eq__(self, x):
                                                                                    """equal to comparison"""
                                                                                            return not self.__ne__(x)#!/usr/bin/python3
                                                                                        """Contains a class `MyInt` that inherits from `int`"""


                                                                                        class MyInt(int):
                                                                                                """Inherits from int base class"""
                                                                                                    def __init__(self, value):
                                                                                                                """Initialize value"""
                                                                                                                        self.value = value

                                                                                                                            def __ne__(self, x):
                                                                                                                                        """not equal to comparison"""
                                                                                                                                                if self.value is x:
                                                                                                                                                                return True

                                                                                                                                                                def __eq__(self, x):
                                                                                                                                                                            """equal to comparison"""
                                                                                                                                                                                    return not self.__ne__(x)
=======
"""this module defines a class MyInt that inherits from int"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """Override == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior"""
        return self.real == value
>>>>>>> 58f9a67cb1a269562fdc796162ac1a88f914f3e5
