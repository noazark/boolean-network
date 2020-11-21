import argparse
import random
import sys
from PIL import Image
from boolean_network import BooleanNetwork


parser = argparse.ArgumentParser(description="Generate a random boolean network")
parser.add_argument("--nodes", metavar="N", type=int, default=256)
parser.add_argument("--connections", metavar="K", type=int, default=2)
parser.add_argument("--cycles", type=int, default=256)
parser.add_argument("--seed", type=int, default=random.randint(0, 999_999_999_999_999))
parser.add_argument("--outdir", type=str, default=".")


def to_ascii(bitmap):
    fmtc = lambda i: "█░" if i == 1 else "  "
    fmtl = lambda lst: "".join(fmtc(i) for i in lst) + "\n"

    sys.stdout.writelines(fmtl(c) for c in bitmap)


def to_img(bitmap, filename):
    # flattening the bitmap
    img_bitmap = tuple(node for net in bitmap for node in net)

    img = Image.new("1", (N, cycles))
    img.putdata(img_bitmap)
    img = img.rotate(90, expand=True)
    img.save(filename, "BMP")


if __name__ == "__main__":
    args = parser.parse_args()

    N = args.nodes
    K = args.connections
    seed = args.seed
    cycles = args.cycles
    outdir = args.outdir

    net = BooleanNetwork.random(N, K, seed)

    to_ascii(net.cycle(cycles))
    to_img(net.cycle(cycles), f"{outdir}/bn-{N}-{K}-{seed}a.bmp")
