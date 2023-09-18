import unittest
from models import base
from models.base import Base


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
        self.assertEqual(Base.to_json_string(input_list),result)

    def test_multiple_dictionaries(self):
        input_list = [{"a": 1, "b": 2, "c": 3},{"x": 1, "y": 2},
                      {"id": 35, "name": "value", "c": 3}]
        result = '[{"a": 1, "b": 2, "c": 3}, {"x": 1, "y": 2},'\
            ' {"id": 35, "name": "value", "c": 3}]'
        self.assertEqual(Base.to_json_string(input_list),result)

    def test_check_class(self):
        self.assertTrue(isinstance(Base.to_json_string([{"a": 1, "b": 2, "c": 3}]), str))

class testBase_JSON_string_to_file(unittest.TestCase):
    """
    Tests for the class method def save_to_file(cls, list_objs):
    that writes the JSON string representation of list_objs to a file
    """
    pass
