#%%
with open("day8.txt") as fp:
    data = fp.read()

test_data = """
30373
25512
65332
33549
35390
"""
# %%
line_data = data.strip().split("\n")
test_line_data = test_data.strip().split("\n")
# %%
dta = line_data

# %%
dta = test_line_data
# %%
visable = set()
for i,row in enumerate(dta):
    row_highest = -1
    for j,c in enumerate(row):
        c= int(c)
        if c > row_highest:
            row_highest = c
            visable.add((i,j))
for i,row in enumerate(dta):
    row_highest = -1
    for j,c in reversed(list(enumerate(row))):
        c= int(c)
        if c > row_highest:
            row_highest = c
            visable.add((i,j))

for j in range(len(dta[0])):
    row_highest = -1
    for i in range(len(dta)):
        c= int(dta[i][j])
        if c > row_highest:
            row_highest = c
            visable.add((i,j))

for j in range(len(dta[0])):
    row_highest = -1
    for i in reversed(range(len(dta))):
        c= int(dta[i][j])
        if c > row_highest:
            row_highest = c
            visable.add((i,j))
len(visable)
# %%
def scenic_score(u,v):
    c1= int(dta[u][v])
    y1=0
    for i in range(1,len(dta[0])-v):
        y1 +=1
        if int(dta[u][v+i]) >= c1: 
            break
    y2=0
    for i in range(1,v+1):
        # print(u,v+y1, dta[u][v+y1])
        y2 +=1
        if int(dta[u][v-i]) >= c1: 
            break
    x1=0
    for i in range(1,len(dta)-u):
        # print(u,v+y1, dta[u][v+y1])
        x1 +=1
        if int(dta[u+i][v]) >= c1: 
            break
    x2=0
    for i in range(1,u+1):
        x2 +=1
        if int(dta[u-i][v]) >= c1: 
            break
    return y1*y2*x1*x2
# scenic_score(i,j)
max([scenic_score(i,j) for i in range(1,len(dta)-1) for j in range(1,len(dta[0])-1)])



# %%
