import unittest
from Submarine import Submarine


class SubmarineTestCase(unittest.TestCase):
    
    def test_sub_mov(self):
        sub = Submarine()
        result = sub.command('LMRDDMMUU')
        self.assertEqual(result, '-1 2 0 NORTH')

unittest.main()