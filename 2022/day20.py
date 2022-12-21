

#%%
import typing
from tqdm.auto import tqdm
from math import prod, ceil
from functools import lru_cache
from dataclasses import dataclass
from collections import deque
import re
#%%
with open("day20.txt") as fp:
    data = fp.read()
test_data="""
1
2
-3
3
-2
0
4
"""
# %%
line_data = data.strip().split("\n")
test_line_data = test_data.strip().split("\n")
# %%
dta = line_data

# %%
dta = test_line_data

# %%
# %%
@lru_cache
def circular_move(value, nums:tuple, mv):
    idx = nums.index(value)
    new_pos = idx+mv
    if idx+mv <= 0:
        new_pos = idx+mv+len(nums)-1
    if idx+mv >= len(nums):
        new_pos = idx+mv-len(nums)+1
    # if new_pos<idx:
    #     new_pos += 1
    # print('v', value, "np", new_pos, "idx", idx, "mv", mv, idx+mv)
    nums = list(nums)
    num = nums.pop(idx)
    nums.insert(new_pos, num)
    return tuple(nums)

mvs = []
for ln in dta:
    mvs.append(int(ln))
nums = mvs
order = mvs

for i in range(len(mvs)):
    n = order[i%len(order)]
    mv = mvs[i%len(mvs)]
    nums = circular_move(n, tuple(nums), mv)
    print(nums)
    # if i<5:
    #     print(nums)
    # elif i%1000 == 0:
    #     print("mo",nums)
# %%
for i,x in enumerate(nums):
    if x == 0:
        r = 0
        y = i
        for _ in range(3):
            for _ in range(1000):
                i+=1
                if i >= len(nums):
                    i = 0
            print(nums[i])
            r += nums[i]
# %%
