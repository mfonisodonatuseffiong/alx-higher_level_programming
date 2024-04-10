Exploring More about Classes and Objects in Python

In this coding endeavor, I delved deeper into the realm of object-oriented programming (OOP) using Python. My learning trajectory encompassed delving into class methods, static methods, distinguishing between class and instance attributes, and mastering the utilization of the special str and repr methods.

Tasks Overview:

A Basic Blueprint for a Rectangle
I commenced by crafting a skeletal structure, an empty class Rectangle, which lays down the groundwork for defining rectangles without relying on any external module imports.

Defining the Essence of a Rectangle
Following the foundational phase, I proceeded to construct a more comprehensive representation of a rectangle encapsulated within a class Rectangle. This representation involves:

Establishing private instance attributes:
width: Featuring getter and setter methods (property def width(self): and property setter def width(self, value): respectively) to access and modify it.
When setting width, it validates whether the provided value is an integer; otherwise, it raises a TypeError with the informative message "width must be an integer."
Furthermore, if the assigned width is less than 0, it triggers a ValueError exception conveying the message "width must be >= 0."
height: Similar to width, it incorporates getter and setter methods to manage its accessibility and modification.
The setter ensures that the height value is an integer; otherwise, it raises a TypeError exception with the explanatory message "height must be an integer."
If the height value is less than 0, it raises a ValueError exception, signaling "height must be >= 0."
Instantiation with optional width and height:
The constructor __init__(self, width=0, height=0) facilitates the creation of instances with provision for specifying the width and height parameters, defaulting to 0 when not provided.
It's worth noting that throughout this endeavor, no external module imports were permitted, emphasizing a thorough understanding and implementation of the concepts within the Python ecosystem.




