import random
import sys


def _random_permutation(iterable, r=None):
    r = len(iterable) if r is None else r
    return random.sample(iterable, r)


def random_connection_for(iterable: iter, i: int, r: int):
    result = None
    max_iterations = 100

    for _ in range(0, max_iterations):
        test = _random_permutation(iterable, r)
        if not i in test:
            return test

    raise Exception(f"Failed to find acyclic connection after {max_iterations} attempts")


def _to_idx(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out


def _get_connections(nodes, state):
    return iter(state[n] for n in nodes)


def transmute(P, network, state):
    def h(nodes, state):
        return _to_idx(_get_connections(nodes, state))

    return iter(P[h(network[i], state)] for i in range(len(state)))


class KN:
    def __init__(self, P, network, state, seed=None):
        self.seed = seed
        self.P = P
        self.network = network
        self.input = state
        self._state = state

    @staticmethod
    def create(N, K, seed=None):
        if seed:
            random.seed(seed)

        # Truth table
        P = [random.getrandbits(1) for x in range(2 ** K)]
        # Network map of connections between nodes
        network = [random_connection_for(range(N), i, K) for i in range(N)]
        # Starting state of network
        state = [random.getrandbits(1) for x in range(N)]

        return KN(P, network, state, seed)

    def __iter__(self):
        return self

    def __next__(self):
        state = self._state
        self._state = tuple(transmute(self.P, self.network, self._state))
        return state
