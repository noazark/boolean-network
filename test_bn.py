from unittest import TestCase

from bn import transmute, _to_idx, _get_connections

class Run(TestCase):

    def test_get_connections(self):
        input = (0, 1, 0, 1)

        self.assertEqual(tuple(_get_connections((1, 2, 3), input)), (1, 0, 1))
        self.assertEqual(tuple(_get_connections((0, 2, 3), input)), (0, 0, 1))
        self.assertEqual(tuple(_get_connections((0, 1, 3), input)), (0, 1, 1))
        self.assertEqual(tuple(_get_connections((0, 1, 2), input)), (0, 1, 0))

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

    def test_to_idx(self):
        self.assertEqual(_to_idx((0, 0, 0)), 0)
        self.assertEqual(_to_idx((0, 0, 1)), 1)
        self.assertEqual(_to_idx((0, 1, 0)), 2)
        self.assertEqual(_to_idx((0, 1, 1)), 3)
        self.assertEqual(_to_idx((1, 0, 0)), 4)
        self.assertEqual(_to_idx((1, 0, 1)), 5)
        self.assertEqual(_to_idx((1, 1, 0)), 6)
        self.assertEqual(_to_idx((1, 1, 1)), 7)