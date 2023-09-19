import unittest
import os
from models import base
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    Tests for 'base' class which will be the “base” of all other classes.
    """

    def test_module_docstring(self):
        self.assertIsNotNone(base.__doc__)
        self.assertNotEqual(len(base.__doc__.split()), 0)

    def test_class_docstring(self):
        self.assertIsNotNone(base.Base.__doc__)
        self.assertNotEqual(len(base.Base.__doc__.split()), 0)

    def test_init_method_docstring(self):
        self.assertIsNotNone(base.Base.__init__.__doc__)
        self.assertNotEqual(len(base.Base.__init__.__doc__.split()), 0)

    def test_default_initialization(self):
        a = base.Base()
        b = base.Base()
        self.assertEqual(b.id - a.id, 1)

    def test_None_id(self):
        a = base.Base(None)
        b = base.Base(None)
        self.assertEqual(b.id - a.id, 1)

    def test_initialization_with_custom_ID(self):
        b = base.Base(12)
        self.assertEqual(b.id, 12)

    def test_multiple_objects_with_custom_IDs(self):
        a = base.Base(12)
        b = base.Base(5)
        c = base.Base(7)
        self.assertEqual(a.id, 12)
        self.assertEqual(b.id, 5)
        self.assertEqual(c.id, 7)

    def test_incrementing_ID(self):
        a = base.Base()
        b = base.Base()
        c = base.Base()
        d = base.Base()
        self.assertEqual(b.id - a.id, 1)
        self.assertEqual(c.id - b.id, 1)
        self.assertEqual(d.id - c.id, 1)

    def test_setting_ID_after_object_creation(self):
        a = base.Base()
        a.id = 8
        self.assertEqual(a.id, 8)

    def test_accesing_private_class_attribute(self):
        with self.assertRaises(AttributeError):
            base.Base().__nb_objects

    def test_str_ID(self):
        b = base.Base("string")
        self.assertEqual(b.id, "string")

    def test_float_ID(self):
        b = base.Base(7.5)
        self.assertEqual(b.id, 7.5)

    def test_list_ID(self):
        b = base.Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def test_dict_ID(self):
        b = base.Base({"a": 1, "b": 2, "c": 3})
        self.assertEqual(b.id, {"a": 1, "b": 2, "c": 3})

    def test_tuple_ID(self):
        b = base.Base((1, 2, 3))
        self.assertEqual(b.id, (1, 2, 3))


class testBase_to_JSON_string(unittest.TestCase):
    """
    Tests for the static method def to_json_string(list_dictionaries):
    that returns the JSON string representation of list_dictionaries
    """

    def test_to_JSON_string_docstring(self):
        self.assertIsNotNone(Base.to_json_string.__doc__)

    def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_None_list(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_single_dictionary(self):
        input_list = [{"a": 1, "b": 2, "c": 3}]
        result = '[{"a": 1, "b": 2, "c": 3}]'
        self.assertEqual(Base.to_json_string(input_list), result)

    def test_multiple_dictionaries(self):
        input_list = [{"a": 1, "b": 2, "c": 3}, {"x": 1, "y": 2},
                      {"id": 35, "name": "value", "c": 3}]
        result = '[{"a": 1, "b": 2, "c": 3}, {"x": 1, "y": 2},'\
            ' {"id": 35, "name": "value", "c": 3}]'
        self.assertEqual(Base.to_json_string(input_list), result)

    def test_check_class(self):
        self.assertTrue(isinstance(
            Base.to_json_string([{"a": 1, "b": 2, "c": 3}]), str))


class testBase_save_to_file(unittest.TestCase):
    """
    Tests for the class method def save_to_file(cls, list_objs):
    that writes the JSON string representation of list_objs to a file
    """
    def test_save_to_file_docstring(self):
        self.assertIsNotNone(Base.save_to_file.__doc__)

    def test_save_to_file_Empty(self):
        instances = []
        Base.save_to_file(instances)
        self.assertTrue(os.path.exists("Base.json"))

    def test_save_to_file_None(self):
        Base.save_to_file(None)
        self.assertTrue(os.path.exists("Base.json"))

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_rectangle(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_square(self):
        s = Square(10)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists("Square.json"))

    def test_save_to_file_None_Square(self):
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))

    def test_save_to_file_empty_Square(self):
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))

    def test_save_to_file_None_Rectangle(self):
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_empty_Rectangle(self):
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def tearDown(self):
        # Clean up created files after each test
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")


class testBase_from_json_string(unittest.TestCase):
    """
    Tests for static method def from_json_string(json_string):
    that returns the list of the JSON string representation json_string
    """

    def test_from_json_string_docstring(self):
        self.assertIsNotNone(Base.from_json_string.__doc__)

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], "hello")

    def test_from_json_string_valid(self):
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        result = Base.from_json_string(json_string)
        self.assertIsInstance(result, list)
        expected = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
        self.assertEqual(result, expected)

    def test_from_json_string_None(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])


class testBase_create(unittest.TestCase):
    """
    Tests for static method def from_json_string(json_string):
    that returns the list of the JSON string representation json_string
    """

    def test_create_square_original(self):
        s = Square(3, 5, 1, 35)
        s_dictionary = s.to_dictionary()
        s1 = Square.create(**s_dictionary)
        self.assertEqual("[Square] (35) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        s = Square(3, id=3)
        s_dictionary = s.to_dictionary()
        s1 = Square.create(**s_dictionary)
        self.assertEqual("[Square] (3) 0/0 - 3", str(s1))

    def test_create_square_is(self):
        s = Square(2)
        s_dictionary = s.to_dictionary()
        s1 = Square.create(**s_dictionary)
        self.assertIsNot(s, s1)

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_square_equals(self):
        s = Square(10)
        s_dictionary = s.to_dictionary()
        s1 = Square.create(**s_dictionary)
        self.assertNotEqual(s, s1)


class testBase_load_from_file(unittest.TestCase):
    """
    Tests for class method def load_from_file(cls):
    that returns a list of instances:
    """
    def tearDown(self):
        # Clean up created files after each test
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_load_from_file_docstring(self):
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

    def test_load_from_file_rectangle(self):
        r = Rectangle(1, 2)
        r = Rectangle(2, 4)
        Rectangle.save_to_file([r, r])
        list_output = Rectangle.load_from_file()
        self.assertEqual(str(r), str(list_output[0]))

    def test_load_from_file_square(self):
        s = Square(5)
        s1 = Square(9)
        Square.save_to_file([s, s1])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s), str(list_squares_output[0]))

    def test_load_from_file_rectangle_types(self):
        r = Rectangle(1, 2)
        r1 = Rectangle(2, 4)
        Rectangle.save_to_file([r, r1])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_square_types(self):
        s = Square(10)
        s1 = Square(9)
        Square.save_to_file([s, s1])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)


if __name__ == "__main__":
    unittest.main()
