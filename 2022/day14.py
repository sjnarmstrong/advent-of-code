#%%
import typing
from tqdm.auto import tqdm
from math import prod
#%%
with open("day14.txt") as fp:
    data = fp.read()
with open("day14_jurg.txt") as fp:
    data = fp.read()
test_data="""
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""
# %%
line_data = data.strip().split("\n")
test_line_data = test_data.strip().split("\n")
# %%
dta = line_data

# %%
dta = test_line_data

# %%
min_bounds, max_bounds = [float('inf'),float('inf')],[-float('inf'),-float('inf')]
points = []
for line in dta:
    line_pts = []
    for p in line.split(" -> "):
        x,y = p.split(",")
        x,y=int(x),int(y)
        min_bounds[1] = min(min_bounds[1],y)
        min_bounds[0] = min(min_bounds[0],x)
        max_bounds[1] = max(max_bounds[1],y)
        max_bounds[0] = max(max_bounds[0],x)
        line_pts.append((x,y))
    points.append(line_pts)

min_bounds[1] = min(min_bounds[1],0)
min_bounds[0] = min(min_bounds[0],500)
max_bounds[1] = max(max_bounds[1],0)
max_bounds[0] = max(max_bounds[0],500)
min_bounds[0] -= 1
min_bounds[1] -= 1
max_bounds[0] += 1
max_bounds[1] += 1

map_v = [["." for _ in range(min_bounds[0],max_bounds[0]+2)] for _ in range(min_bounds[1],max_bounds[1]+2)]

for line_pts in points:
    for prev_pt, pt in zip(line_pts, line_pts[1:]):
        for y in range(min(prev_pt[1], pt[1]), max(prev_pt[1], pt[1])+1):
            for x in range(min(prev_pt[0], pt[0]), max(prev_pt[0], pt[0])+1):
                xp,yp = x-min_bounds[0]+1,y-min_bounds[1]+1
                map_v[yp][xp] = "#"

# %%
def print_step(sand_pos=None):
    if sand_pos is not None:
        h=map_v[sand_pos[1]][sand_pos[0]]
        map_v[sand_pos[1]][sand_pos[0]] = "~"
    print('\n'.join([''.join(l) for l in map_v]))
    print()
    if sand_pos is not None:
        map_v[sand_pos[1]][sand_pos[0]] = h
# %%

def move_sand(sand_pos):
    xp,yp = sand_pos
    if map_v[yp+1][xp] == ".": return True, [xp,yp+1]
    if map_v[yp+1][xp-1] == ".": return True, [xp-1,yp+1]
    if map_v[yp+1][xp+1] == ".": return True, [xp+1,yp+1]
    return False, sand_pos


def move_sand_2(sand_pos):
    xp,yp = sand_pos
    if yp+1 >= len(map_v): return False, sand_pos
    if map_v[yp+1][xp] == ".": return True, [xp,yp+1]
    if map_v[yp+1][xp-1] == ".": return True, [xp-1,yp+1]
    if map_v[yp+1][xp+1] == ".": return True, [xp+1,yp+1]
    return False, sand_pos

def run():
    i=0
    while True:
        sand_moved, sand_pos = True, [500-min_bounds[0]+1,0-min_bounds[1]+1]


        while sand_moved:
            sand_moved, sand_pos = move_sand(sand_pos)
            if sand_pos[1] >= len(map_v)-1: 
                print_step(sand_pos)
                return i
            # sand_moved, sand_pos = move_sand_2(sand_pos)

        map_v[sand_pos[1]][sand_pos[0]] = 'o'
        if sand_pos[0] == 0:
            min_bounds[0] -=1
            for v in map_v:
                v.insert(0, '.')
        if sand_pos[0] == len(map_v[0])-1:
            max_bounds[0] += 1
            for v in map_v:
                v.append('.')
        print_step(sand_pos)
        i+=1
        if sand_pos[0] == 500-min_bounds[0]+1 and sand_pos[1] == 0-min_bounds[1]+1:
            return i
run()
# %%
