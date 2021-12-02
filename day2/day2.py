#!/usr/bin/env python3

x = 0
y = 0

with open("data/input.txt") as in_handle:
    for move in in_handle:
        direction, steps = move.strip().split()
        steps = int(steps)
        if direction == "forward":
            x += steps
        elif direction == "up":
            y -= steps
        elif direction == "down":
            y += steps

print(x * y)

x = 0
y = 0
aim = 0
with open("data/input.txt") as in_handle:
    for move in in_handle:
        direction, steps = move.strip().split()
        steps = int(steps)
        if direction == "forward":
            x += steps
            y += steps * aim
        elif direction == "up":
            aim -= steps
        elif direction == "down":
            aim += steps

print(x * y)
