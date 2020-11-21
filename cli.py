import argparse
import random
from PIL import Image
from bn import KN


# cli.py --nodes=256 --connections=3 --cycles=1024 --seed

parser = argparse.ArgumentParser(description="Generate a random boolean network")
parser.add_argument("--nodes", metavar="N", type=int, default=256)
parser.add_argument("--connections", metavar="K", type=int, default=2)
parser.add_argument("--cycles", type=int, default=256)
parser.add_argument("--seed", type=int, default=random.randint(0, 999_999_999_999))


def to_print(bitmap):
    fmt = lambda i: " " if i == 1 else i
    fmtl = lambda lst: (fmt(i) for i in lst)

    for c in bitmap:
        print(*fmtl(c))


if __name__ == "__main__":
    args = parser.parse_args()

    N = args.nodes
    K = args.connections
    seed = args.seed
    cycles = args.cycles

    print(f"seed: {seed}")
    net = KN.create(N, K, seed)

    # iterate over each node in every step in the cycle
    bitmap = [node for idx, net in zip(range(cycles), net) for node in net]

    img = Image.new("1", (N, cycles))
    img.putdata(bitmap)
    img = img.rotate(90, expand=True)
    img.save("examples/foo.bmp", "BMP")
