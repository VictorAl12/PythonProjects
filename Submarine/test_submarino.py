import unittest
from Submarino import Submarino


class SubmarinoTestCase(unittest.TestCase):
    
    def test_sub_mov(self):
        sub = Submarino()
        result = sub.comandar('LMRDDMMUU')
        self.assertEqual(result, '-1 2 0 NORTE')

unittest.main()