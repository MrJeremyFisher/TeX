tau = {
    1: 6,
    2: 3,
    3: 7,
    4: 9,
    5: 1,
    6: 8,
    7: 2,
    8: 4,
    9: 5
}
iota = [1, 2, 3, 4, 5, 6, 7, 8, 9]

t = [6, 3, 7, 9, 1, 8, 2, 4, 5]

cnt = 1
while t != iota:
    cnt = cnt + 1
    for i in range(0, 9):
        t[i] = tau[t[i]]
    print(t)

print(f"Got iota on {cnt}")
