#!/usr/bin/python3
"""square module for geometry lover"""


class Square():

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            if self.width != self.height:
                return None

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        return self.width * 4

    def __str__(self):
        return "{}/{}".format(self.width, self.height)
