import random
import sys
from copy import copy


def random_connection_for(iterable: iter, i: int, r: int):
    result = None
    max_iterations = 100

    for _ in range(max_iterations):
        test = random.sample(iterable, r)
        if not i in test:
            return test

    raise Exception(
        f"Failed to find acyclic connection after {max_iterations} attempts"
    )


def bits_to_int(bitlist):
    '''
    Converts a list of bits into an integer
    '''
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out


def transmute_node(P, network, state, i):
    """
    For a given index, i, return the next state of the node at that position.

    Parameters:
    P (int[][]): the truth table defining state transitions
    network: map of connections between nodes in the state graph
    state: current state of the network
    i (int): index of node to transmute
    """

    connections = iter(state[n] for n in network[i])
    return P[bits_to_int(connections)]


def transmute(P, network, state):
    return iter(transmute_node(P, network, state, i) for i in range(len(state)))


class BooleanNetwork:
    def __init__(self, P, network, state, seed=None):
        self.seed = seed
        self.P = P
        self.network = network
        self.input = state
        self._state = state

    @staticmethod
    def random(N, K, seed=None):
        if seed:
            random.seed(seed)

        # Truth table
        P = tuple(random.getrandbits(1) for x in range(2 ** K))
        # Network map of connections between nodes
        network = tuple(random_connection_for(range(N), i, K) for i in range(N))
        # Starting state of network
        state = tuple(random.getrandbits(1) for x in range(N))

        return BooleanNetwork(P, network, state, seed)

    def __iter__(self):
        return copy(self)

    def __next__(self):
        state = self._state
        self._state = tuple(transmute(self.P, self.network, self._state))
        return state

    def cycle(self, n):
        return [net for idx, net in zip(range(n), self)]