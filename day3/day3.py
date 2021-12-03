#!/usr/bin/env python3

with open("data/input.txt") as in_handle:
    tally = [int(x) if int(x) == 1 else -1 for x in in_handle.readline().strip()]
    for line in in_handle:
        for index, token in enumerate(line.strip()):
            token = int(token)
            if token == 1:
                tally[index] += 1
            elif token == 0:
                tally[index] -= 1
gamma = ["0" if x < 0 else "1" for x in tally]
epsilon = ["0" if x > 0 else "1" for x in tally]
gamma = int("".join(gamma), 2)
epsilon = int("".join(epsilon), 2)
print(gamma * epsilon)

with open("data/input.txt") as in_handle:
    readings = [x.strip() for x in in_handle.readlines()]
    ogr = set(readings)
    index = 0
    while len(ogr) > 1:
        new = set()
        mcv = sum([int(x[index]) for x in ogr])
        if (len(ogr) - mcv) > mcv:
            mcv = 0
        else:
            mcv = 1
        for reading in ogr:
            if int(reading[index]) == mcv:
                new.add(reading)
        ogr = new
        index += 1
ogr = int(list(ogr)[0], 2)
print(f"OGR: {ogr}")

with open("data/input.txt") as in_handle:
    readings = [x.strip() for x in in_handle.readlines()]
    csr = set(readings)
    index = 0
    while len(csr) > 1:
        new = set()
        mcv = sum([int(x[index]) for x in csr])
        if (len(csr) - mcv) > mcv:
            mcv = 1
        else:
            mcv = 0
        for reading in csr:
            if int(reading[index]) == mcv:
                new.add(reading)
        csr = new
        index += 1
csr = int(list(csr)[0], 2)
print(f"CSR: {csr}")

print(ogr * csr)
