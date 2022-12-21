#%%
with open("day10.txt") as fp:
    data = fp.read()
test_data="""
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""
# %%
line_data = data.strip().split("\n")
test_line_data = test_data.strip().split("\n")
# %%
dta = line_data

# %%
dta = test_line_data
# %%
cycles = 0
sum_v = 1
collect = {20,60,100,140,180,220}
vals = []
for line in dta:
    if line.startswith("noop"):
        cycles+=1
        if cycles in collect:
            vals.append((cycles*sum_v))
    if line.startswith("addx"):
        if cycles +1 in collect:
            vals.append(((cycles+1)*sum_v))

        cycles+=2
        if cycles in collect:
            vals.append(((cycles)*sum_v))
        sum_v += int(line.split(" ")[1])
    # vals.append((cycles,sum_v))
sum(vals)
# %%
screen = [['.' for i in range(40)] for j in range(8)]
cycles = 0
sum_v = 1
for line in dta:
    if line.startswith("noop"):
        cycles+=1
    if line.startswith("addx"):
        cycles+=1
        screen[cycles//40][cycles%40] = "#" if sum_v-1 <= cycles%40 <= sum_v+1 else '.'
        cycles+=1
        sum_v += int(line.split(" ")[1])
    screen[cycles//40][cycles%40] = "#" if sum_v-1 <= cycles%40 <= sum_v+1 else '.'
print('\n'.join([''.join(r) for r in screen]))
# %%
