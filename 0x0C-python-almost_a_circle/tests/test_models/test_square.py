import unittest
from models import square
from io import StringIO
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle


class testSquare_instantiation(unittest.TestCase):
    """
    Tests instantiation of the Rectanle
    """

    def test_module_docstring(self):
        self.assertIsNotNone(square.__doc__)
        self.assertNotEqual(square.__doc__.split(), 0)

    def test_class_docstring(self):
        self.assertIsNotNone(Square.__doc__)
        self.assertNotEqual(Square.__doc__.split(), 0)

    def test_methods_docstring(self):
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertIsNotNone(Square.width.__doc__)
        self.assertIsNotNone(Square.height.__doc__)
        self.assertIsNotNone(Square.x.__doc__)
        self.assertIsNotNone(Square.y.__doc__)

    def test_inheritance(self):
        s = Square(2)
        self.assertTrue(isinstance(s, Rectangle))

    def test_default_intialization(self):
        s = Square(2)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_initalization_with_values(self):
        s = Square(2)
        self.assertEqual(s.width, 2)
        self.assertEqual(s.height, 2)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

        r1 = Square(5, 7, 9)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 9)

    def test_ID_assignment(self):
        s = Square(2)
        r1 = Square(10)
        r2 = Square(2, id=12)
        r3 = Square(2, 3, 4, 37)
        self.assertEqual(r1.id - s.id, 1)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r3.id, 37)

    def test_accesing_private_class_attribute(self):
        with self.assertRaises(AttributeError):
            Square(2).__width
            Square(2).__height
            Square(2).__x
            Square(2).__y

    def test_getter_methods(self):
        s = Square(2, 3, 4, 49)
        self.assertEqual(s.width, 2)
        self.assertEqual(s.height, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        self.assertEqual(s.id, 49)

    def test_setter_methods(self):
        s = Square(2, 4, 7)
        s.size = 60
        s.x = 39
        s.y = 50
        s.id = 88
        self.assertEqual(s.size, 60)
        self.assertEqual(s.height, 60)
        self.assertEqual(s.x, 39)
        self.assertEqual(s.y, 50)
        self.assertEqual(s.id, 88)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            s = Square()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            s = Square()

    def test_excess_args(self):
        with self.assertRaises(TypeError):
            s = Square(1, 3, 4, 6, 78, 6, 5, 34, 56)


class testValidate_initialization(unittest.TestCase):
    """
    Tests validation of all settes methods and instantiation (id excluded)
    """

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -2)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 5, -7)

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, None)

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, None)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("hello")

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "hello")

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, "hello")

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, 5.5)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, 5.5)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, [1, 2, 3])

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, [1, 2, 3])

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3))

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, (1, 2, 3))

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, (1, 2, 3))

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2, "c": 3})

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, {"a": 1, "b": 2, "c": 3})

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, {"a": 1, "b": 2, "c": 3})


class testSquare_area(unittest.TestCase):
    """
    Tests the area method
    """

    def test_docstring(self):
        self.assertIsNotNone(Square.area.__doc__)

    def test_square_area(self):
        s = Square(2)
        self.assertEqual(s.area(), 4)

    def test_large_area(self):
        s = Square(99999)
        self.assertEqual(s.area(), 9999800001)

    def test_area_with_arg(self):
        with self.assertRaises(TypeError):
            s = Square(2)
            s.area("arg")

    def test_area_changed_values(self):
        s = Square(10)
        s.size = 5
        self.assertEqual(s.area(), 25)


class testSquare_Display(unittest.TestCase):
    """
    Tests fos display method that prints in stdout the
    Square instance with the charactes #
    """

    def test_docstring(self):
        self.assertIsNotNone(Square.display.__doc__)

    def test_display_square(self):
        s = Square(2)
        expected = "##\n##\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display_large(self):
        s = Square(5)
        expected = "#####\n#####\n#####\n#####\n#####\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display_changed_values(self):
        s = Square(5)
        s.size = 2
        expected = "##\n##\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display_arg_exception(self):
        with self.assertRaises(TypeError):
            s = Square(2)
            s.display("arg")

    def test_display_with_coordinates(self):
        s = Square(2, 2, 3)
        expected = "\n\n\n  ##\n  ##\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display_x_zero(self):
        s = Square(4, 0, 4, 3)
        expected = "\n\n\n\n####\n####\n####\n####\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display_y_zero(self):
        s = Square(2, 2, 0)
        expected = "  ##\n  ##\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display_x_y_large(self):
        s = Square(2, 4, 7)
        expected = "\n\n\n\n\n\n\n    ##\n    ##\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display_same_xy(self):
        s = Square(2, 3, 3)
        expected = "\n\n\n   ##\n   ##\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue(), expected)


class tesSquare__str__(unittest.TestCase):
    """
    Test fos the __str__ method so that
    Returns Square representation
        [Square] (<id>) <x>/<y> - <size>
    """

    def test_docstring(self):
        self.assertIsNotNone(Square.__str__.__doc__)

    def test_str_square(self):
        s = Square(2)
        self.assertEqual(str(s), f'[Square] ({s.id}) 0/0 - 2')

    def test_with_coordinates(self):
        s = Square(2, 9, 1, 7)
        self.assertEqual(str(s), f'[Square] (7) 9/1 - 2')

    def test_multiple_instances(self):
        s = Square(6, 2, 1, 12)
        self.assertEqual(str(s), f'[Square] (12) 2/1 - 6')
        s = Square(7, 2, 5, 35)
        self.assertEqual(str(s), f'[Square] (35) 2/5 - 7')
        s = Square(20, 6, 3, 49)
        self.assertEqual(str(s), f'[Square] (49) 6/3 - 20')


class testSquare_update(unittest.TestCase):
    """
    Tests fos the the public method def update(self, *args):
    that assigns an argument to each attribute
    """
    def test_update_docstring(self):
        self.assertIsNotNone(Square.update.__doc__)

    def test_no_args(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual(s.id, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 10)

    def test_update_id(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_width(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(s.size, 2)

    def test_update_height(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual(s.x, 3)

    def test_update_x(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual(s.y, 4)

    def test_update_all(self):
        s = Square(2)
        s.update(4, 7, 2, 9)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 9)

    def test_update_kwargs(self):
        s = Square(2)
        s.update(id=35, width=4, height=7, x=2, y=9)
        self.assertEqual(s.id, 35)
        self.assertEqual(s.width, 4)
        self.assertEqual(s.height, 7)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 9)

    def test_update_args_kwargs(self):
        s = Square(2)
        s.update(3, 7, 10, 2, id=35, x=2, y=9)
        self.assertEqual(s.id, 3)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 2)

    def test_kwags_negative_value(self):
        with self.assertRaises(ValueError):
            s = Square(1, 2)
            s.update(size=-5)

    def test_kwags_zero_value(self):
        with self.assertRaises(ValueError):
            s = Square(2)
            s.update(size=0)

    def test_kwags_negative_x(self):
        with self.assertRaises(ValueError):
            s = Square(2)
            s.update(x=-7)

    def test_kwags_invalid_value(self):
        with self.assertRaises(TypeError):
            s = Square(2)
            s.update(height="hello")


class testSquare_dictionary(unittest.TestCase):
    """
    Test fos public method def to_dictionary(self):
    that returns the dictionary representation of a Square
    """

    def test_dict_docstring(self):
        self.assertIsNotNone(Square.to_dictionary.__doc__)

    def test_dict_default(self):
        s = Square(2)
        expected = {'id': s.id, 'x': 0, 'y': 0, 'size': 2}
        self.assertEqual(s.to_dictionary(), expected)

    def test_dict_instance(self):
        s = Square(5)
        self.assertTrue(isinstance(s.to_dictionary(), dict))

    def test_dict_xy(self):
        s = Square(2, 7, 10, 12)
        expected = {'id': 12, 'x': 7, 'y': 10, 'size': 2}
        self.assertEqual(s.to_dictionary(), expected)

    def test_dict_arg(self):
        with self.assertRaises(TypeError):
            s = Square(1, 2)
            s.to_dictionary("hello")


if __name__ == "__main__":
    unittest.main()
