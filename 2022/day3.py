#%%
with open("day3.txt") as fp:
    data = fp.read()
# %%
sacks = data.split('\n')
# %%
sacks = sacks[:-1]
# %%
def get_sack_priority(sack):
    in_both = set(sack[:len(sack)//2]).intersection(sack[len(sack)//2:])
    assert len(in_both) == 1
    in_both = list(in_both)
    value = ord(in_both[0])-ord('a')+1
    if value < 0:
        value = ord(in_both[0])-ord('A')+27
    return value
# %%
sack_p = [get_sack_priority(s) for s in sacks]
sum(sack_p)
# %%
sacks_test = [
"vJrwpWtwJgWrhcsFMMfFFhFp",
"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
"PmmdzqPrVvPwwTWBwg",
"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
"ttgJtRGJQctTZtZT",
"CrZsJsPPZsGzwwsLwLmpwMDw"]
sum([get_sack_priority(s) for s in sacks_test])
# %%

def sack_badge(s1,s2,s3):
    in_both = set(s1).intersection(s2).intersection(s3)
    assert len(in_both) == 1
    in_both = list(in_both)
    value = ord(in_both[0])-ord('a')+1
    if value < 0:
        value = ord(in_both[0])-ord('A')+27
    return value
sack_b = [sack_badge(*s) for s in zip(sacks_test[0::3],sacks_test[1::3],sacks_test[2::3])]
sack_b
# %%


sack_b = [sack_badge(*s) for s in zip(sacks[0::3],sacks[1::3],sacks[2::3])]
sum(sack_b)
# %%
