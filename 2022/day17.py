

#%%
import typing
from tqdm.auto import tqdm
from math import prod
from functools import lru_cache
#%%
with open("day17.txt") as fp:
    data = fp.read()
test_data="""
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
"""
# %%
line_data = data.strip()
test_line_data = test_data.strip()
# %%
dta = line_data

# %%
dta = test_line_data

# %%
blocks = [
    ((0,0),(0,3),(0,1),(0,2)),
    ((1,0),(1,2),(2,1),(1,1),(0,1)),
    ((0,0),(2,2),(0,1),(0,2),(1,2)),
    ((0, 0),(3, 0),(1, 0),(2, 0)),
    ((0, 0),(1,1),(1, 0),(0,1)),
]
block_max_rights = [max([b[1] for b in blk]) for blk in blocks]

tower = set()
skyline = [-1]*7


def try_move_lr(dir, block, st, bmr):
    if not ((d>0 and bmr<6) or (d<0 and st>0)):
        return block, st, bmr
    return [(x, y+dir) for x,y in block], st+dir, bmr+dir

def move(dir, block):
    return [(x+dir[0], y+dir[1]) for x,y in block]
def try_move(dir, block):
    new_block = move(dir, block)
    for b in new_block:
        if b[1] < 0: return False, block
        if b[1] >= 7: return False, block
        # if b[0] <= skyline[b[1]]: return False, block
        if b[0] < 0: return False, block
        if b in tower: return False, block
    return True, new_block

cache = {}

def print_tower(tower, block):
    print('\n'.join([''.join(['#' if (j,i) in tower else '@' if (j,i) in block else '.' for i in range(7)]) for j in reversed(range(max([b[0] for b in tower], default=0)+10))]))
    print()



directions = [-1 if c == "<" else 1 for c in dta]
max_height = max(skyline)
dir_i = 0
i = 0
END = 1000000000000
extra_height = 0
pbar = tqdm(total=END)
while i<END:
    pbar.update()
    block_idx = i%len(blocks)
    block = blocks[block_idx]
    bmr = 2+block_max_rights[block_idx]
    st = 2
    for _ in range(3):
        d = directions[dir_i]
        if (d>0 and bmr<6) or (d<0 and st>0):
            bmr += d
            st += d
        dir_i = (dir_i+1)%len(directions)

    block = move((max_height+1, st), block)
    can_go_down = True
    while can_go_down:
        _, block = try_move((0,directions[dir_i]), block)
        dir_i = (dir_i+1)%len(directions)
        can_go_down, block = try_move((-1,0), block)

    for b in block:
        skyline[b[1]] = max(skyline[b[1]],b[0])
    tower.update(block)
    i+=1

    max_height = max(skyline)
    m_skyline = min(skyline)
    profile = tuple(((b[0]-m_skyline, b[1]) for b in tower if b[0]>=m_skyline))
    # profile = tuple((max_height-s for s in skyline))
    cache_idx = (block_idx, dir_i, profile)
    if cache_idx in cache:
        print(cache_idx)
        last_i, last_height = cache[cache_idx]
        di = i-last_i
        dh = max_height-last_height
        times_applyable = (END-i)//di
        pbar.update(times_applyable)
        extra_height += times_applyable*dh
        i += di*times_applyable
        # print()
    cache[cache_idx] = i, max_height

    

    
max(skyline)+1+extra_height
# %%
