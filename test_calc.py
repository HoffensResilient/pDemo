import unittest
import numpy as np
import pDemo as mod

class test_calc(unittest.TestCase):
    def test_mean(self):
        y = np.array([2,4,6,8])
        e=mod.mean(y)
        self.assertEqual(e,5)
        print(e)

