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

import toolz as tz

increased = 0
with open("data/input.txt") as in_handle:
    measurements = [int(x.strip()) for x in in_handle.readlines()]

prev = math.inf
for window in tz.sliding_window(3, measurements):
    current = sum(window)
    if current > prev:
        increased += 1
    prev = current
print(increased)
