import unittest
from models import base
from models import rectangle
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle


class testRectangle_instantiation(unittest.TestCase):
    """
    Tests instantiation of the Rectanle
    """

    def test_module_docstring(self):
        self.assertIsNotNone(rectangle.__doc__)
        self.assertNotEqual(rectangle.__doc__.split(), 0)

    def test_class_docstring(self):
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertNotEqual(Rectangle.__doc__.split(), 0)

    def test_methods_docstring(self):
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIsNotNone(Rectangle.y.__doc__)

    def test_inheritance(self):
        r = Rectangle(2, 10)
        self.assertTrue(isinstance(r, base.Base))

    def test_default_intialization(self):
        r = Rectangle(2, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_initalization_with_values(self):
        r = Rectangle(2, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        r1 = Rectangle(1, 5, 7, 9)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 9)

    def test_ID_assignment(self):
        r = Rectangle(2, 10)
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10, id=12)
        r3 = Rectangle(1, 2, 3, 4, 37)
        self.assertEqual(r1.id - r.id, 1)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r3.id, 37)

    def test_accesing_private_class_attribute(self):
        with self.assertRaises(AttributeError):
            Rectangle(2, 10).__width
            Rectangle(2, 10).__height
            Rectangle(2, 10).__x
            Rectangle(2, 10).__y

    def test_getter_methods(self):
        r = Rectangle(1, 2, 3, 4, 49)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 49)

    def test_setter_methods(self):
        r = Rectangle(2, 3)
        r.width = 4
        r.height = 60
        r.x = 39
        r.y = 50
        r.id = 88
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 60)
        self.assertEqual(r.x, 39)
        self.assertEqual(r.y, 50)
        self.assertEqual(r.id, 88)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_excess_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 3, 4, 6, 78, 6, 5, 34, 56)


class testValidate_initialization(unittest.TestCase):
    """
    Tests validation of all setter methods and instantiation (id excluded)
    """

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 10)

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -5)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 10)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 5, -2)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 5, 2, -7)

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_None_heght(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, None)

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 7, None)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("hello", 2)

    def test_str_heght(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "hello")

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "hello")

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 7, "hello")

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 2)

    def test_float_heght(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 5.5)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, 5.5)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 7, 5.5)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_list_heght(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, [1, 2, 3])

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, [1, 2, 3])

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 7, [1, 2, 3])

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_tuple_heght(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (1, 2, 3))

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, (1, 2, 3))

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 7, (1, 2, 3))

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2, "c": 3}, 2)

    def test_dict_heght(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"a": 1, "b": 2, "c": 3})

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {"a": 1, "b": 2, "c": 3})

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 7, {"a": 1, "b": 2, "c": 3})


class testRectangle_area(unittest.TestCase):
    """
    Tests the area method
    """

    def test_docstring(self):
        self.assertIsNotNone(Rectangle.area.__doc__)

    def test_rectangle_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_square_area(self):
        r = Rectangle(2, 2)
        self.assertEqual(r.area(), 4)

    def test_large_area(self):
        r = Rectangle(999999999999999, 999999999999999999)
        self.assertEqual(r.area(), 999999999999998999000000000000001)

    def test_area_with_arg(self):
        with self.assertRaises(TypeError):
            r = Rectangle(2, 10)
            r.area("arg")

    def test_area_changed_values(self):
        r = Rectangle(2, 10)
        r.width = 5
        r.height = 7
        self.assertEqual(r.area(), 35)


class testRectangle_Display(unittest.TestCase):
    """
    Tests for display method that prints in stdout the
    Rectangle instance with the character #
    """

    def test_docstring(self):
        self.assertIsNotNone(Rectangle.display.__doc__)

    def test_display_rectangle(self):
        r = Rectangle(2, 4)
        expected = "##\n##\n##\n##\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display_square(self):
        r = Rectangle(2, 2)
        expected = "##\n##\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display_large(self):
        r = Rectangle(5, 8)
        expected = "#####\n#####\n#####\n#####\n#####\n#####\n#####\n#####\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display_changed_values(self):
        r = Rectangle(5, 8)
        r.width = 1
        r.height = 2
        expected = "#\n#\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display_arg_exception(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2)
            r.display("arg")

    def test_display_with_coordinates(self):
        r = Rectangle(2, 4, 2, 3)
        expected = "\n\n\n  ##\n  ##\n  ##\n  ##\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display_x_zero(self):
        r = Rectangle(2, 4, 0, 3)
        expected = "\n\n\n##\n##\n##\n##\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display_y_zero(self):
        r = Rectangle(2, 4, 2, 0)
        expected = "  ##\n  ##\n  ##\n  ##\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display_x_y_large(self):
        r = Rectangle(2, 4, 4, 7)
        expected = "\n\n\n\n\n\n\n    ##\n    ##\n    ##\n    ##\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display_same_xy(self):
        r = Rectangle(2, 2, 3, 3)
        expected = "\n\n\n   ##\n   ##\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected)


class tesRectangle__str__(unittest.TestCase):
    """
    Test for the __str__ method so that
    returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
    """

    def test_docstring(self):
        self.assertIsNotNone(Rectangle.__str__.__doc__)

    def test_str_rectangle(self):
        r = Rectangle(2, 10)
        self.assertEqual(str(r), f'[Rectangle] ({r.id}) 0/0 - 2/10')

    def test_str_square(self):
        r = Rectangle(2, 2)
        self.assertEqual(str(r), f'[Rectangle] ({r.id}) 0/0 - 2/2')

    def test_with_coordinates(self):
        r = Rectangle(2, 9, 1, 7)
        self.assertEqual(str(r), f'[Rectangle] ({r.id}) 1/7 - 2/9')

    def test_multiple_instances(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), f'[Rectangle] (12) 2/1 - 4/6')
        r = Rectangle(3, 7, 2, 5, 35)
        self.assertEqual(str(r), f'[Rectangle] (35) 2/5 - 3/7')
        r = Rectangle(9, 20, 6, 3, 49)
        self.assertEqual(str(r), f'[Rectangle] (49) 6/3 - 9/20')


class testRectangle_update(unittest.TestCase):
    """
    Tests for the the public method def update(self, *args):
    that assigns an argument to each attribute
    """
    def test_update_docstring(self):
        self.assertIsNotNone(Rectangle.update.__doc__)

    def test_no_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_update_id(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_width(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual(r.width, 2)

    def test_update_height(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)

    def test_update_x(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)

    def test_update_y(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)

    def test_update_all(self):
        r = Rectangle(1, 2)
        r.update(35, 4, 7, 2, 9)
        self.assertEqual(r.id, 35)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 9)

    def test_update_kwargs(self):
        r = Rectangle(1, 2)
        r.update(id=35, width=4, height=7, x=2, y=9)
        self.assertEqual(r.id, 35)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 9)

    def test_update_args_kwargs(self):
        r = Rectangle(1, 2)
        r.update(1, 3, 7, 10, 2, id=35, x=2, y=9)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 2)

    def test_kwags_negative_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2)
            r.update(width=-5)

    def test_kwags_zero_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2)
            r.update(height=0)

    def test_kwags_negative_x(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2)
            r.update(x=-7)

    def test_kwags_invalid_value(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2)
            r.update(height="hello")


class testRectangle_dictionary(unittest.TestCase):
    """
    Test for public method def to_dictionary(self):
    that returns the dictionary representation of a Rectangle
    """

    def test_dict_docstring(self):
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)

    def test_dict_default(self):
        r = Rectangle(1, 2)
        expected = {'id': r.id, 'x': 0, 'y': 0, 'width': 1, 'height': 2}
        self.assertEqual(r.to_dictionary(), expected)

    def test_dict_instance(self):
        r = Rectangle(1, 2)
        self.assertTrue(isinstance(r.to_dictionary(), dict))

    def test_dict_xy(self):
        r = Rectangle(1, 2, 7, 10, 12)
        expected = {'id': 12, 'x': 7, 'y': 10, 'width': 1, 'height': 2}
        self.assertEqual(r.to_dictionary(), expected)

    def test_dict_arg(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2)
            r.to_dictionary("hello")


if __name__ == "__main__":
    unittest.main()
