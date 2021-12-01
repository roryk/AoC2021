#!/usr/bin/env python3

import math

increased = 0
prev = math.inf
with open("data/input.txt") as in_handle:
    for measurement in in_handle:
        current = int(measurement.strip())
        if current > prev:
            increased += 1
        prev = current
print(increased)
