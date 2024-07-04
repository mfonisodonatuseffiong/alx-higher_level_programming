<<<<<<< HEAD

#!/usr/bin/python3
"""Contains a single function"""


def inherits_from(obj, a_class):
        """
                Check if the object is instance of a class inherited
                        from directly or indirectly
                            """
                                return ((issubclass(type(obj), a_class)) and type(obj) != a_class)

                            #!/usr/bin/python3
                            """Contains a single function"""


                            def inherits_from(obj, a_class):
                                    """
                                            Check if the object is instance of a class inherited
                                                    from directly or indirectly
                                                        """
                                                            return ((issubclass(type(obj), a_class)) and type(obj) != a_class)

=======
#!/usr/bin/python3
"""checks if object is an instance of a class that
inherited from the specified class or not
"""


def inherits_from(obj, a_class):
    """Returns true if object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
>>>>>>> 58f9a67cb1a269562fdc796162ac1a88f914f3e5
