#%%
with open("day6.txt") as fp:
    data = fp.read()

test_data = """
bvwbjplbgvbhsrlpgdmjqwftvncz
"""
# %%
line_data = data.strip()
test_line_data = test_data.strip()
# %%
dta = line_data
# %%
dta = test_line_data
# %%
s = set()
for i,c in enumerate(dta):
    print(s)
    s.add(c)
    if len(s) > 4:
        print(i)
        break

# %%
for i in range(len(dta)-14):
    if len(set(dta[i:i+14]))==14:break
print(i+14)
# %%
