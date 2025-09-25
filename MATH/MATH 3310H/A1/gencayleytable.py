import numpy as np
from abc import abstractmethod


class operator:
    @abstractmethod
    def do_op(a, b):
        return

    @abstractmethod
    def getstr(lat):
        return


class plus(operator):
    def do_op(a, b):
        return a + b

    def getstr(lat):
        return "+"


class mul(operator):
    def do_op(a, b):
        return a * b

    def getstr(lat):
        if lat:
            return "\cdot"
        else:
            return "*"


def printcayley(op: operator):
    closed = True
    badval = []
    if latex:
        v = str(np.full_like(S, "c", dtype=object)).strip("[]").replace("'c'", "c")
        print(v)
        print("\\setlength\\extrarowheight{3pt}")
        print(f"\\noindent\\begin{{tabular}}{{c | {v}}}")
        print(f"${op.getstr(latex)}_{{{mod}}}$ &", end=" ")
    else:
        print(f"{op.getstr(latex)}_{mod}", end=" ")
    for i in S:
        if i != S[-1]:
            if latex:
                print(i, end=" & ")
            else:
                print(i, end=" ")
        else:
            print(f"{i}", end=" ")
    if latex:
        print("\\\\")
    else:
        print("")
    if latex:
        print(f"\cline{{1-{len(S)+1}}}")

    for i in S:
        if latex:
            print(i, end=" & ")
        else:
            print(i, end=" ")
        for j in S:
            val = (op.do_op(i, j)) % mod
            if val not in S:
                if val not in badval:
                    badval.append(val)
                closed = False
            print(f"{val} ", end="")
            if j != S[-1] and latex:
                print("& ", end="")
        if latex:
            print("\\\\")
        else:
            print("")
    print("\\end{tabular}")
    if closed:
        print("closed!")
    else:
        print("not closed,", badval)


S = [1,5,7,11]
mod = 12
latex = True

printcayley(plus)
print("")
printcayley(mul)
