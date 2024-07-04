#!/usr/bin/python3
<<<<<<< HEAD
"""Contain a single function"""


def add_attribute(self, attribute, value):
        """Add attribute if it's possible."""
            if hasattr(self, '__dict__'):
                        setattr(self, attribute, value)
                            else:
                                        raise TypeError("can't add new attribute")#!/usr/bin/python3
                                    """Contain a single function"""


                                    def add_attribute(self, attribute, value):
                                            """Add attribute if it's possible."""
                                                if hasattr(self, '__dict__'):
                                                            setattr(self, attribute, value)
                                                                else:
                                                                            raise TypeError("can't add new attribute")
=======
"""this module defines a function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
>>>>>>> 58f9a67cb1a269562fdc796162ac1a88f914f3e5
