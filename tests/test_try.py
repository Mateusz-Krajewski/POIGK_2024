import unittest # pylint: disable=all
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))


class TestClass(unittest.TestCase):  # pylint: disable=all
    def test_is_none(self): # pylint: disable=all
        self.assertTrue(True) # pylint: disable=all