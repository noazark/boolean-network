from unittest import TestCase

from boolean_network import transmute, bits_to_int

class Run(TestCase):

    def test_transmute(self):
        P = (1, 0, 1, 1, 0, 0, 0)
        input = (0, 1, 0, 1)
        network = (
            (1, 2, 3), # 1 0 1 -> 5 -> 0
            (0, 2, 3), # 0 0 1 -> 1 -> 0
            (0, 1, 3), # 0 1 1 -> 3 -> 1
            (0, 1, 2), # 0 1 0 -> 2 -> 1
        )

        self.assertEqual(tuple(transmute(P, network, input)), (0, 0, 1, 1))

    def test_bits_to_int(self):
        self.assertEqual(bits_to_int((0, 0, 0)), 0)
        self.assertEqual(bits_to_int((0, 0, 1)), 1)
        self.assertEqual(bits_to_int((0, 1, 0)), 2)
        self.assertEqual(bits_to_int((0, 1, 1)), 3)
        self.assertEqual(bits_to_int((1, 0, 0)), 4)
        self.assertEqual(bits_to_int((1, 0, 1)), 5)
        self.assertEqual(bits_to_int((1, 1, 0)), 6)
        self.assertEqual(bits_to_int((1, 1, 1)), 7)