

#%%
import typing
from tqdm.auto import tqdm
from math import prod, ceil
from functools import lru_cache
from dataclasses import dataclass
from collections import deque
import re
import bisect
#%%
with open("day22.txt") as fp:
    data = fp.read()
test_data="""
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""
# %%
line_data = data.strip('\n').split("\n\n")
test_line_data = test_data.strip('\n').split("\n\n")
# %%
map_dta, dta = line_data

# %%
map_dta, dta = test_line_data

# %%
l_map_dta = map_dta.split("\n")
map_bounds_x = [None]*len(l_map_dta)
map_bounds_y = [None]*max((len(l) for l in l_map_dta))
map_landmines_x = [set() for _ in map_bounds_x]
map_landmines_y = [set() for _ in map_bounds_y]
for i, ln in enumerate(l_map_dta):
    min_v = None
    max_v = None
    for j,c in enumerate(ln):
        if c=="#": 
            map_landmines_x[i].add(j)
            map_landmines_y[j].add(i)
        if c!=" ":
            if min_v is None:
                min_v = j
            max_v = j
            if map_bounds_y[j] is None:
                map_bounds_y[j] = [i,i]
            else:
                map_bounds_y[j][1] = i
    map_bounds_x[i] = [min_v, max_v]
map_landmines_x = [sorted(lm) for lm in map_landmines_x]
map_landmines_y = [sorted(lm) for lm in map_landmines_y]
# %%
patt = re.compile(r"(\d+)([RL]?)")
# %%
direction = (0,1)
pos = (0,map_bounds_x[0][0])
def make_turn(curr_dir, turn):
    if turn == "R":
        return (curr_dir[1], -curr_dir[0])
    if turn == "L":
        return (-curr_dir[1], curr_dir[0])
    return curr_dir

def landmine_check(prev_v, next_v, landmines, direction_ax):
    if len(landmines) <= 0: return next_v
    idx = bisect.bisect(landmines, prev_v)
    if direction_ax > 0:
        if idx < len(landmines):
            next_v = min(next_v, landmines[idx]-1)
    elif idx>0:
        next_v = max(next_v, landmines[idx-1]+1)
    return next_v

def do_moves(bounds, landmines, oth_coord, curr_dir, prev_v, mvnt):
    curr_landmines = landmines[oth_coord]
    curr_bounds = bounds[oth_coord]
    next_v = prev_v+curr_dir*mvnt
    next_v = landmine_check(prev_v, next_v, curr_landmines, curr_dir)
    while next_v > curr_bounds[1]:
        if curr_bounds[0] in curr_landmines:
            next_v = curr_bounds[1]
        else:
            next_v -= curr_bounds[1]-curr_bounds[0]+1
            next_v = landmine_check(curr_bounds[0], next_v, curr_landmines, curr_dir)
    while next_v < curr_bounds[0]:
        if curr_bounds[1] in curr_landmines:
            next_v = curr_bounds[0]
        else:
            next_v += curr_bounds[1]-curr_bounds[0]+1
            next_v = landmine_check(curr_bounds[1], next_v, curr_landmines, curr_dir)
    return next_v
facings = {
    (0,1): 0,
    (1,0): 1,
    (0,-1): 2,
    (-1,0): 3,
}
# %%
direction = (0,1)
pos = (0,map_bounds_x[0][0])
pos_history = [pos]
for step_idx, (mvnt, turn) in enumerate(patt.findall(dta), start=1):
    mvnt = int(mvnt)
    if direction[1] ==0:
        next_x = pos[1]
        next_y = do_moves(
            map_bounds_y, 
            map_landmines_y, 
            next_x, 
            direction[0], 
            pos[0], 
            mvnt
        )

    else:
        next_y = pos[0]
        next_x = do_moves(
            map_bounds_x, 
            map_landmines_x, 
            next_y, 
            direction[1], 
            pos[1], 
            mvnt
        )
    direction = make_turn(direction, turn)
    pos = (next_y,next_x)
    pos_history.append(pos)
    print(step_idx, mvnt, turn, pos, direction)
    # if step_idx>0 and (pos[0], pos[1], direction[0], direction[1]) != tuple(gt_data[step_idx-1]):
    #     print("Failed", gt_data[step_idx])

# %%
def print_map():
    lines = []
    for i,l in enumerate(map_dta.split("\n")):
        ln = []
        for j,c in enumerate(l):
            try:
                c=f"{pos_history.index((i,j))}"
            except ValueError:
                pass
            c=f"{c:^5}"
            ln.append(c)
        lines.append(''.join(ln))
    print('\n'.join(lines))
print_map()
# %%
1000 * (pos[0]+1) + 4 * (pos[1]+1) + facings[direction]
# %%
import json
with open('day22pt1_dt.json') as fp:
    gt_data = json.load(fp)
# %%
