#%%
import typing
from tqdm.auto import tqdm
from math import prod
from functools import lru_cache
#%%
with open("day16.txt") as fp:
    data = fp.read()
test_data="""
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
"""
# %%
line_data = data.strip().split("\n")
test_line_data = test_data.strip().split("\n")
# %%
dta = line_data

# %%
dta = test_line_data

# %%
valves = {}
for ln in dta:
    p1,p2 = ln.split(";")
    v,rt = p1.split(" has flow rate=")
    v = v.split("alve ")[1]
    p2 = " ".join(p2.split(" ")[5:])
    out_tunnels = p2.split(", ")
    valves[v] = (int(rt), out_tunnels)

# %%
shortest_paths = {k: {k:[]} for k in valves.keys()}
updated = True
while updated:
    updated = False
    for c in valves.keys():
        c_paths = shortest_paths[c]
        for n in valves[c][1]:
            n_paths = shortest_paths[n]
            for nn, n_path in n_paths.items():
                if nn not in c_paths or len(c_paths[nn])>len(n_path)+1:
                    c_paths[nn] = [n]+n_path
                    updated = True

# %%
def evaluate_value(path, depth=30):
    curr = 0
    on=0
    i=0
    open_v = set()
    for v in path:
        i+=1
        curr += on
        # print(f"{i}, {curr}, {on}, {v}, {open_v}")
        if v.startswith("o") and v not in open_v:
            on += valves[v[1:]][0]
            open_v.add(v)
        if i==depth: return curr
    # print(max((30-i),0), on)
    curr += on*max((depth-i),0)

    return curr

@lru_cache
def eval_open_order_old(v_to_o, pos='AA'):
    path = []
    for v in v_to_o:
        path.extend(shortest_paths[pos][v])
        path.append('o'+v)
        pos = v
    # print(path)
    return evaluate_value(path)

@lru_cache
def eval_open_order(v_to_o, pos='AA', end=None):
    on = 0
    ts = 0
    curr = 0
    for v in v_to_o:
        steps = len(shortest_paths[pos][v])+1
        ts += steps
        curr += steps*on
        on += valves[v][0]
        pos = v
    if end is not None:
        curr += on*max((end-ts),0)
    return curr
    


# %%
max_vals = {}
max_vals["AA"] = tuple()
paths_to_visit = ["AA"]
valves_to_open = set((k for k,v in valves.items() if v[0]>0))
while len(paths_to_visit)>0:
    cn = paths_to_visit.pop(0)
    # new_v = eval_open_order(new_path)
    for n in valves_to_open-set(max_vals[cn]):
        new_path = max_vals[cn] + (n,)
        new_path = max_vals[cn] + (n,)
        if n not in max_vals or eval_open_order(max_vals[n])<eval_open_order(new_path):
            max_vals[n] = new_path
            if n not in paths_to_visit:
                paths_to_visit.append(n)


# %%
def get_paths()

