"Tests for my custom meta class"
import unittest

from custom_meta import CustomMeta


class CustomMetaTest(unittest.TestCase):

    "Test case for CustomMeta."

    class CustomClass(metaclass=CustomMeta):

        "Class with CustomMeta as metaclass."

        x = 50

        def __init__(self, val=99):
            self.val = val

        def line(self) -> int:
            "Some method."
            return 100

    def setUp(self):
        self.inst = CustomMetaTest.CustomClass()

    def test_new_attr_names(self):
        "Test attributes names (with custom_)."
        self.assertEqual(self.inst.custom_x, 50)
        self.assertEqual(self.inst.custom_val, 99)
        self.assertEqual(self.inst.custom_line(), 100)

    def test_old_attr_names(self):
        "Test attributes names (without custom_)."
        self.assertFalse(hasattr(self.inst, 'x'))
        self.assertFalse(hasattr(self.inst, 'val'))
        self.assertFalse(hasattr(self.inst, 'line'))
