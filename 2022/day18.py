

#%%
import typing
from tqdm.auto import tqdm
from math import prod
from functools import lru_cache
#%%
with open("day18.txt") as fp:
    data = fp.read()
test_data="""
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""
# %%
line_data = data.strip().split("\n")
test_line_data = test_data.strip().split("\n")
# %%
dta = line_data

# %%
dta = test_line_data

# %%
from collections import Counter
edges = Counter()
blocks = set()
for ln in dta:
    x,y,z = ln.split(",")
    x,y,z = int(x),int(y),int(z)

    edges.update([
        (x+0.5,y,z),
        (x-0.5,y,z),
        (x,y+0.5,z),
        (x,y-0.5,z),
        (x,y,z+0.5),
        (x,y,z-0.5)
    ])
    blocks.add((x,y,z))
sum((e for e in edges.values() if e == 1))
# %%
max_x = max([k[0] for k in edges.keys()])
max_y = max([k[1] for k in edges.keys()])
max_z = max([k[2] for k in edges.keys()])
min_x = min([k[0] for k in edges.keys()])
min_y = min([k[1] for k in edges.keys()])
min_z = min([k[2] for k in edges.keys()])

# %%
max_x = max([k[0] for k in blocks])
max_y = max([k[1] for k in blocks])
max_z = max([k[2] for k in blocks])
min_x = min([k[0] for k in blocks])
min_y = min([k[1] for k in blocks])
min_z = min([k[2] for k in blocks])

touched = set()
touched_edges = set()
to_explore = [
    (min_x -2 ,min_y -2 ,min_z -2 ,),
    (max_x +2 ,min_y -2 ,min_z -2 ,),
    (min_x -2 ,max_y+2 ,min_z -2 ,),
    (max_x +2 ,max_y+2 ,min_z -2 ,),
    (min_x -2 ,min_y -2 ,max_z+2,),
    (max_x +2 ,min_y -2 ,max_z+2 ,),
    (min_x -2 ,max_y+2 ,max_z+2,),
    (max_x +2 ,max_y+2 ,max_z+2 ,)
]
neighbours = [
    (+1,0,0),
    (-1,0,0),
    (0,+1,0),
    (0,-1,0),
    (0,0,+1),
    (0,0,-1),
]

pbar = tqdm()
while to_explore:
    pbar.update()
    water_pos = to_explore.pop()
    if water_pos in touched: continue
    touched.add(water_pos)
    if water_pos in blocks: continue
    x,y,z = water_pos
    touched_edges.update([
        (x+0.5,y,z),
        (x-0.5,y,z),
        (x,y+0.5,z),
        (x,y-0.5,z),
        (x,y,z+0.5),
        (x,y,z-0.5)
    ])
    for n in neighbours:
        n_pos = (water_pos[0]+n[0],water_pos[1]+n[1],water_pos[2]+n[2])
        if n_pos[0] < min_x-4 or n_pos[1] < min_y-4 or n_pos[2] < min_y-4: continue
        if n_pos[0] > max_x+4 or n_pos[1] > max_y+4 or n_pos[2] > max_y+4: continue
        to_explore.append(n_pos)
    # print(to_explore)


len(touched_edges.intersection(edges.keys()))

# %%


def is_exposed(edge):
    for x in range(edge[0]+1, max_x+1):
        if (x, edge[1], edge[2]) in edges:
            break
    else: return True
    for x in range(edge[0]-1, min_x-1, -1):
        if (x, edge[1], edge[2]) in edges:
            break
    else: return True
    for y in range(edge[1]+1, max_y+1):
        if (edge[0], y, edge[2]) in edges:
            break
    else: return True
    for y in range(edge[1]-1, min_y-1, -1):
        if (edge[0], y, edge[2]) in edges:
            break
    else: return True
    for z in range(edge[2]+1, max_z+1):
        if (edge[0], edge[1], z) in edges:
            break
    else: return True
    for z in range(edge[2]-1, min_z-1, -1):
        if (edge[0], edge[1], z) in edges:
            break
    else: return True
    return False

sum(is_exposed(f) for f,e in edges.items() if e == 1)

# %%

for f,e in edges.items():

