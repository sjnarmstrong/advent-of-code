#%%
import typing
from tqdm.auto import tqdm
from math import prod
#%%
with open("day12.txt") as fp:
    data = fp.read()
test_data="""
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
# %%
line_data = data.strip().split("\n")
test_line_data = test_data.strip().split("\n")
# %%
dta = line_data

# %%
dta = test_line_data
#%%
def cap_ord(v:str):
    if v == 'S': 
        v = 'a'
    if v == 'E': 
        v = 'z'
    # if v.isupper():
    #     return ord(v)-ord('A')+26
    return ord(v)-ord('a')
def get_positions(pos):
    x,y = pos
    res = []
    current = cap_ord(dta[y][x])
    for i in range(-1,2):
        
        if x+i<0 or x+i>=len(dta[0]): continue
        for j in range(-1,2):

            if i==0 and j ==0: continue
            if y+j<0 or y+j>=len(dta): continue
            if abs(i)==1 and abs(j)==1: continue
            if cap_ord(dta[y+j][x+i]) - current > 1: continue
            res.append((x+i,y+j))
    return res

def get_start():
    for y,l in enumerate(dta):
        for x,c in enumerate(l):
            if c=='S': return (x,y)
start = get_start()
seen_nodes = [[None]*len(dta[0]) for i in range(len(dta))]
seen_nodes[start[1]][start[0]]=[]
nodes_to_visit = [start]
e_pos = None
while len(nodes_to_visit):
    pos = nodes_to_visit.pop(0)
    x,y = pos
    for n in get_positions(pos):
        if seen_nodes[n[1]][n[0]] is None or len(seen_nodes[n[1]][n[0]])>len(seen_nodes[y][x])+1:
            seen_nodes[n[1]][n[0]] = list(seen_nodes[y][x])+[pos]
            nodes_to_visit.append(n)
            if dta[n[1]][n[0]] != 'E':
                nodes_to_visit.append(n)
            else:
                e_pos = n

lens = [[len(s) if s is not None else 'na' for s in snr] for snr in seen_nodes]
lens[e_pos[1]][e_pos[0]]
# [(sn,dta[sn[1]][sn[0]]) for sn in seen_nodes[e_pos[1]][e_pos[0]]]
# def dfs(pos, seen):
#     x,y = pos
#     # print(pos, seen)
#     if dta[y][x] == 'E':
#         return [pos]
#     for p in get_positions(pos):
#         seen_nodes[p[1]][p[0]]
#         res = dfs(p, set([pos]).union(seen))
#         if res is not None:
#             return [pos]+res
#     return None
# dfs((0,0),[])
# %%
# %%
def get_start():
    res = []
    for y,l in enumerate(dta):
        for x,c in enumerate(l):
            if c=='S' or c=='a': res.append((x,y))
    return res
starts = get_start()
seen_nodes = [[None]*len(dta[0]) for i in range(len(dta))]
for start in starts:
    seen_nodes[start[1]][start[0]]=[]
nodes_to_visit = starts
e_pos = None
while len(nodes_to_visit):
    pos = nodes_to_visit.pop(0)
    x,y = pos
    for n in get_positions(pos):
        if seen_nodes[n[1]][n[0]] is None or len(seen_nodes[n[1]][n[0]])>len(seen_nodes[y][x])+1:
            seen_nodes[n[1]][n[0]] = list(seen_nodes[y][x])+[pos]
            nodes_to_visit.append(n)
            if dta[n[1]][n[0]] != 'E':
                nodes_to_visit.append(n)
            else:
                e_pos = n

lens = [[len(s) if s is not None else 'na' for s in snr] for snr in seen_nodes]
lens[e_pos[1]][e_pos[0]]
# %%
