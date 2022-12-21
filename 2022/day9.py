#%%
with open("day9.txt") as fp:
    data = fp.read()
test_data="""
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
test_data = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""
# %%
line_data = data.strip().split("\n")
test_line_data = test_data.strip().split("\n")
# %%
dta = line_data

# %%
dta = test_line_data
# %%
dir_map = {
    "R": (0,1),
    "L": (0,-1),
    "U": (1,0),
    "D": (-1,0),
}
H = (0,0)
tails = [(0,0) for i in range(9)]
T_Places = {(0,0)}

def move_tail(H,T):
    if (T[0]-H[0])**2+(T[1]-H[1])**2 < 4: return False, T
    diff_0 = (H[0]-T[0])/abs(H[0]-T[0]) if H[0]!=T[0] else 0
    diff_1 = (H[1]-T[1])/abs(H[1]-T[1]) if H[1]!=T[1] else 0
    T = (int(T[0]+diff_0), int(T[1]+diff_1))
    return True, T

def get_text_results():
    nodes = [(0,0), H]+tails
    nodes_and_markers = [(0,0), H]+tails+list(T_Places)
    max_x = max([t[0] for t in nodes_and_markers])
    min_x = min([t[0] for t in nodes_and_markers])
    max_y = max([t[1] for t in nodes_and_markers])
    min_y = min([t[1] for t in nodes_and_markers])

    spots = [["." for _ in range(min_x,max_x+1)] for _ in range(min_y,max_y+1)]

    for n in T_Places:
        spots[n[1]-min_y][n[0]-min_x] = '#'

    for i,n in enumerate(nodes):
        marker = 's' if i ==0 else 'm' if i==1 else str(i-1)
        spots[n[1]-min_y][n[0]-min_x] = marker

    return '\n'.join([''.join(r) for r in spots])

stage_results = []
for move in dta:
    direction, count = move.split(" ")
    direction = dir_map[direction]
    count = int(count)
    # stage_results.append(get_text_results())
    for i in range(count):
        H = (H[0]+direction[0], H[1]+direction[1])
        for i in range(len(tails)):
            should_move, T = move_tail(H if i==0 else tails[i-1],tails[i])
            tails[i] = T
            if not should_move: break
        else:
            T_Places.add(tails[-1])
        # stage_results.append(get_text_results())





# %%
