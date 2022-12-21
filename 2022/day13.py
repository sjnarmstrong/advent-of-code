#%%
import typing
from tqdm.auto import tqdm
from math import prod
#%%
with open("day13.txt") as fp:
    data = fp.read()
test_data="""
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]

"""
# %%
line_data = data.strip().split("\n")
test_line_data = test_data.strip().split("\n")
# %%
dta = line_data

# %%
dta = test_line_data

# # %%
# prev_gt_tuple = tuple.__gt__
# prev_gt_int = int.__gt__

# %%
# def override_gt_tuple(self, other):
#     if isinstance(other, int):
#         return prev_gt_tuple((other,))
#     return prev_gt_tuple((other,))
# def override_gt_int(self, other):
#     return prev_gt_tuple((self,))
# tuple.__gt__ = override_gt_tuple
# int.__gt__ = override_gt_int
# class CustTuple():
#     def __init__(self, *args):
#         self.args = args
#         if len(args)==1: return
#         new_args = []
#         for item in args:
#             if isinstance(item, int):
#                 item = CustTuple(item)
#             new_args.append(item)
#         self.args = tuple(new_args)
#     def __gt__(self, other):
#         if isinstance(other, int):
#             return self.args > CustTuple(*other.args,)
#         if isinstance(other.args, int):
#             return self.args > CustTuple(*other.args,)
#         if isinstance(self.args, int):
#             return CustTuple(*self.args,) > self.args
#         return self.args > other.args

# %%
def list_cmp(l1:list,l2:list):
    for v1,v2 in zip(l1,l2):
        if isinstance(v1, list) or isinstance(v2, list):
            if not isinstance(v2, list):
                v2=[v2]
            if not isinstance(v1, list):
                v1=[v1]
            r = list_cmp(v1,v2)
        else: 
            r = v1<v2 if v1!=v2 else None
            # print(v1,v2,r)
        if r is not None: return r
    return len(l1) <= len(l2)

correct_pairs = []
for i, (p1, p2) in enumerate(zip(dta[::3],dta[1::3]), start=1):
    # p1 = p1.replace("[","CustTuple(")
    # p1 = p1.replace("]",")")
    # p2 = p2.replace("[","CustTuple(")
    # p2 = p2.replace("]",")")
    p1 = eval(p1)
    p2 = eval(p2)
    
    if list_cmp(p1,p2):
        correct_pairs.append(i)
sum(correct_pairs)
# %%

import functools

def list_cmp2(l1:list,l2:list):
    if list_cmp(l1,l2): return -1
    return 1

all_pairs = [eval(p) for p in dta[::3]]+[eval(p) for p in dta[1::3]]+[[[2]], [[6]]]
all_pairs.sort(key=functools.cmp_to_key(list_cmp2))
(all_pairs.index([[2]])+1)*(all_pairs.index([[6]])+1)

# %%
