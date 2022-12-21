#%%
with open("day5.txt") as fp:
    data = fp.read()

test_data = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
# %%
header, line_data = data.split('\n\n')
line_data = line_data.strip().split("\n")
header = header.split("\n")[:-1]
# line_data = line_data[:-1]
test_header, test_line_data = test_data.split('\n\n')
test_line_data = test_line_data.strip().split("\n")
test_header, test_last_line = test_header.split("\n")[:-1], test_header.split("\n")[-1]
# test_line_data = test_line_data[:-1]

# %%
hdr = header
moves = line_data
patt = [[] for i in range((len(hdr[-1])+1)//4)]
for line in hdr:
    for i in range(0, len(line), 4):
        if line[i+1] != " ":
            patt[i//4].insert(0,line[i+1])

# %%

def move(patt, from_v, to_v):
    patt[to_v].append(patt[from_v].pop())
# %%
print(patt)
for mv in moves:
    _, count, _, from_v, _, to_v = mv.split(" ")
    count = int(count) 
    from_v = int(from_v) -1
    to_v = int(to_v) -1
    for i in range(count):
        move(patt, from_v, to_v)
        print(from_v, to_v)
        print(patt)
# %%
''.join([p[-1] for p in patt])
# %%


def move2(patt, from_v, to_v,n):
    patt[to_v].extend(reversed([patt[from_v].pop() for _ in range(n)]))

for mv in moves:
    _, count, _, from_v, _, to_v = mv.split(" ")
    count = int(count) 
    from_v = int(from_v) -1
    to_v = int(to_v) -1
    move2(patt, from_v, to_v, count)
# %%
