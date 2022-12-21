#%%
with open("day1.txt") as fp:
    data = fp.read()
# %%
elves = data.split("\n\n")
def get_elve_total(elve):
    return sum((int(e) for e in elve.split("\n") if len(e)>0))
max((get_elve_total(e) for e in elves))
# %%
sum(sorted((get_elve_total(e) for e in elves))[-3:])
# %%
