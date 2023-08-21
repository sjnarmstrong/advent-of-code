#%%
import typing
from tqdm.auto import tqdm
from math import prod, ceil
from functools import lru_cache
from dataclasses import dataclass
import collections
import re
import bisect
#%%
with open("day22.txt") as fp:
    data = fp.read()
test_data="""
.....
..##.
..#..
.....
..##.
.....
"""
test_data="""
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
"""
test_data="""
..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............
"""
# %%
line_data = data.strip().split("\n")
test_line_data = test_data.strip().split("\n")
# %%
dta = line_data

# %%
dta = test_line_data
#%%
positions = set()
for j, ln in enumerate(dta):
    for i, c in enumerate(ln):
        if c == '#': positions.add((j,i))

directions = collections.deque([
    (((-1,-1),(-1,0),(-1,1)), ((-1,0))),
    (((1,-1),(1,0),(1,1)), ((1,0))),
    (((-1,-1),(0,-1),(1,-1)), ((0,-1))),
    (((-1,1),(0,1),(1,1)), ((0,1))),
])

def get_next_pos(pos):
    y,x=pos
    for direction_test, direction in directions:
        if positions.isdisjoint(((y+dti[0],x+dti[1]) for dti in direction_test)):
            return (y+direction[0],x+direction[1]), pos, True
    return pos, pos, False

def print_map():
    y_coords = [p[0] for p in positions]
    x_coords = [p[1] for p in positions]
    for j in range(min(y_coords), max(y_coords)+1):
        print(''.join(["#" if (j,i) in positions else '.' for i in range(min(x_coords), max(x_coords)+1)]))
    print()
print_map()
# %%

# while True:
print_map()
for _ in range(10):
    next_positions = [get_next_pos(pos) for pos in positions]
    next_positions_cnt = collections.Counter((p[0] for p in next_positions))
    positions = {p[0] if next_positions_cnt[p[0]] == 1 else p[1] for p in next_positions}
    # if all((p[2] for p in next_positions)) and len(next_positions_cnt) == len(next_positions): 
    #     print_map()
    #     break
    directions.rotate(-1)
    print_map()
# %%
