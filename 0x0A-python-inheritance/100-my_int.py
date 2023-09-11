#!/usr/bin/python3
"""defines a class MyInt that inherits from int"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """ == opeartor inverts to != """
        return self.real != value

    def __ne__(self, value):
        """ != operator inverts to == """
        return self.real == value
