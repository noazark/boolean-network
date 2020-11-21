import random
from PIL import Image
from bn import KN


def to_print(bitmap):
    fmt = lambda i: " " if i == 1 else i
    fmtl = lambda lst: (fmt(i) for i in lst)

    for c in bitmap:
        print(*fmtl(c))


if __name__ == "__main__":
    # number of nodes in the graph
    N = 2 ** 8
    # number of connections between each node
    K = 3
    # number of iterations to perform on the
    cycles = 1024

    seed = random.randint(0, 999_999_999_999)
    print(f"seed: {seed}")
    net = KN.create(N, K, seed)

    # iterate over each node in every step in the cycle
    bitmap = [node for idx, net in zip(range(cycles), net) for node in net]

    img = Image.new("1", (N, cycles))
    img.putdata(bitmap)
    img = img.rotate(90, expand=True)
    img.save("examples/foo.bmp", "BMP")
