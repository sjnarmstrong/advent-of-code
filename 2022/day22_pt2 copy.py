

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
total_h = len(l_map_dta)
total_w = max((len(l) for l in l_map_dta))
map_cntr = collections.Counter(map_dta)
total_blocks = map_cntr["."]+map_cntr["#"]
block_size = int((total_blocks/6)**0.5)
mesh = [[None]*int(total_w/block_size) for _ in range(int(total_h/block_size))]
mesh_landmines = {}
for i, mesh_row in enumerate(mesh):
    for j, mesh_el in enumerate(mesh_row):
        start_y = i*block_size
        start_x = j*block_size
        if start_x >= len(l_map_dta[start_y]) or l_map_dta[start_y][start_x] == " ": continue
        mesh_idx = len(mesh_landmines)
        mesh[i][j] = mesh_idx
        mesh_face_landmines = set()
        for y,ln in enumerate(l_map_dta[start_y:start_y+block_size]):
            for x,c in enumerate(ln[start_x:start_x+block_size]):
                if c=="#": mesh_face_landmines.add((y,x))
        mesh_landmines[mesh_idx] = mesh_face_landmines
mesh
# %%
@lru_cache()
def get_mesh_face_idx(face):
    for i, mesh_row in enumerate(mesh):
        try:
            return i, mesh_row.index(face)
        except ValueError:
            pass
def rotation_mod(*args):
    return tuple(((x+1)%4-1 for x in args))

@lru_cache
def get_sin_cos_angle(angle):
    if angle ==0: # 0 deg
        cos_a = 1
        sin_a = 0
    elif angle ==1: # 90 deg
        cos_a = 0
        sin_a = 1
    elif angle ==2: # 180 deg
        cos_a = -1
        sin_a = 0
    elif angle ==2: # -90 deg
        cos_a = 0
        sin_a = -1
    return cos_a, sin_a

def rx(angle, vector):
    ca, sa = get_sin_cos_angle(angle)
    x,y,z = vector
    return (
        ca*x-sa*y,
        sa*x+ca*y,
        z,
    )

def ry(angle, vector):
    ca, sa = get_sin_cos_angle(angle)
    x,y,z = vector
    return (
        ca*x+sa*z,
        y,
        -sa*x+ca*z,
    )

def rz(angle, vector):
    ca, sa = get_sin_cos_angle(angle)
    x,y,z = vector
    return (
        x,
        ca*y-sa*z,
        sa*y+ca*z,
    )
def apply_rolls(rolls, vector):
    return rz(rolls[2],ry(rolls[1],rx(rolls[0], vector)))

def tuple_sum(v1,v2):
    return tuple((i1+i2 for i1,i2 in zip(v1,v2)))

rolls = [None]*6
rolls[0] = (0,0,0)
to_explore = [0]
while to_explore:
    j = to_explore.pop(0)
    pos_j = get_mesh_face_idx(j)
    for i in range(6):
        if i==j: continue
        if rolls[i] is not None: continue
        pos_i = get_mesh_face_idx(i)
        diff = (pos_i[1]-pos_j[1], pos_i[0]-pos_j[0], 0)
        if abs(diff[0])+abs(diff[1]) != 1: continue
        rolls[i] = rotation_mod(*tuple_sum(rolls[j],apply_rolls(rolls[j], diff)))
        to_explore.append(i)




# @lru_cache()
# def get_rotations(face_i, face_j):
#     pos_i = get_mesh_face_idx(face_i)
#     pos_j = get_mesh_face_idx(face_j)
#     return (rotation_mod(pos_j[0]-pos_i[0]), rotation_mod(pos_j[1]- pos_i[1]))

# class Connection:
#     def __init__(self, block_size, connecting_axis=0, invert=False, swap_axis=False):
#         self.invert = invert
#         self.connecting_axis = connecting_axis
#         self.swap_axis = swap_axis
#         self.block_size = block_size
#     def wrap(self,v):
#         # TODO maybe there is a case for -v
#         if self.invert:
#             return self.block_size-v
#         return v-block_size
#     def __call__(self, pos):
#         pos = list(pos)
#         pos[self.connecting_axis] = self.wrap(pos[self.connecting_axis])
#         if self.swap_axis:
#             pos = reversed(pos)
#         return tuple(pos)
#     def __repr__(self) -> str:
#         params = [f"ax: {self.connecting_axis}"]
#         if self.swap_axis:
#             params.append("swap")
#         if self.invert:
#             params.append("invert")
#         return f"Connection({', '.join(params)})"
        

# def get_connection_fn(face_i, face_j):
#     r_y, r_x = get_rotations(face_i, face_j)
#     if abs(r_x)!=1 and abs(r_y)!=1: return None
#     if abs(r_y)==1:
#         conn_ax = 0
#         inv = r_y<0
# %%
