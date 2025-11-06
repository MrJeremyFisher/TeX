class Permutation:
    def __init__(self, map: dict, name: str):
        self.map = map
        self.name = name

    def __mul__(self, other):
        result = [1, 2, 3, 4]
        for i in range(len(self.map)):
            result[i] = self.map[other.map[i + 1]]
        return result

    def inverse(self):
        inv = {v: k for k, v in self.map.items()}
        return list(dict(sorted(inv.items())).values())


sig_1 = Permutation({
    1: 3,
    2: 4,
    3: 2,
    4: 1,
}, "sig_1")

sig_2 = Permutation({
    1: 4,
    2: 3,
    3: 1,
    4: 2,
}, "sig_2")

sig_3 = Permutation({
    1: 3,
    2: 4,
    3: 1,
    4: 2,
}, "sig_3")

sig_4 = Permutation({
    1: 4,
    2: 3,
    3: 2,
    4: 1,
}, "sig_4")

sig_5 = Permutation({
    1: 2,
    2: 1,
    3: 4,
    4: 3,
}, "sig_5")

sig_6 = Permutation({
    1: 1,
    2: 2,
    3: 4,
    4: 3,
}, "sig_6")

sig_7 = Permutation({
    1: 2,
    2: 1,
    3: 3,
    4: 4,
}, "sig_7")

vals = [sig_1, sig_2, sig_3, sig_4, sig_5, sig_6, sig_7]

for v in vals:
    for v1 in vals:
        prod = v * v1
        print(
            f"{v.name}*{v1.name}={[x.name for x in vals if list(x.map.values()) == prod]}")
