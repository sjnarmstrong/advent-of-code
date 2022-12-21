#%%
with open("day4.txt") as fp:
    data = fp.read()

test_data = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
# %%
line_data = data.strip().split('\n')
# line_data = line_data[:-1]
test_line_data = test_data.strip().split('\n')
# test_line_data = test_line_data[:-1]

# %%
line = test_line_data[0]
def get_line_score(line):
    pair1,pair2 = line.split(",")
    (st1,ed1),(st2 ,ed2)= pair1.split("-"),pair2.split("-")
    (st1,ed1),(st2 ,ed2)=(int(st1),int(ed1)),(int(st2) ,int(ed2))
    return (st1<=st2 and ed1>=ed2) or (st2<=st1 and ed2>=ed1)
def get_line_score_pt2(line):
    pair1,pair2 = line.split(",")
    (st1,ed1),(st2 ,ed2)= pair1.split("-"),pair2.split("-")
    (st1,ed1),(st2 ,ed2)=(int(st1),int(ed1)),(int(st2) ,int(ed2))
    return (st1<=ed2 and st2<=ed1)
# %%
sum([get_line_score(l) for l in test_line_data])
# %%

sum([get_line_score(l) for l in line_data])
# %%
sum([get_line_score_pt2(l) for l in test_line_data])

# %%
sum([get_line_score_pt2(l) for l in line_data])

# %%
