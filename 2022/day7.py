#%%
with open("day7.txt") as fp:
    data = fp.read()

test_data = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
# %%
line_data = data.strip().split("\n")
test_line_data = test_data.strip().split("\n")
# %%
dta = line_data

# %%
dta = test_line_data
# %%
def try_get_size(l):
    try:
        return int(l.split(" ")[0])
    except ValueError: return None

import re
import os
current_directory = ""
directory_sizes = {}
ds = 0
for l in dta:
    sz = try_get_size(l)
    if sz is not None and current_directory not in directory_sizes:
        ds += sz
        # directory_sizes[current_directory] = directory_sizes.get(current_directory,0)+sz
    elif l.startswith("$ cd "):
        if current_directory not in directory_sizes:
            directory_sizes[current_directory] = ds
        current_directory =os.path.abspath(os.path.join(current_directory,l.split("$ cd ")[1]))
        ds = 0

directory_sizes[current_directory] = ds
used_space = sum(directory_sizes.values())
directory_sizes
# %%
for key,v in directory_sizes.items():
    parts = key.split("/")
    for i in range(len(parts)):
        directory_sizes["/".join(parts[:i])]+=v

# %%
directory_sizes.pop("")
directory_sizes.pop("/")
# %%
unused_space = 70000000-used_space
needed_space = 30000000-unused_space
min([v for v in directory_sizes.values() if v >= needed_space])
# %%


# min([v for v in directory_sizes.values() if v >= (70000000-directory_sizes["/"])])
# %%
