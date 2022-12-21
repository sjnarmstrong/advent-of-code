#%%
import typing
from tqdm.auto import tqdm
from math import prod
#%%
with open("day11.txt") as fp:
    data = fp.read()
test_data="""
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""
# %%
line_data = data.strip().split("\n")
test_line_data = test_data.strip().split("\n")
# %%
dta = line_data

# %%
dta = test_line_data
# %%
class Monkey():
    def __init__(self, starting_items, op, div_test, true_monkey, false_monkey, dev_amount=3) -> None:
        self.items=starting_items
        self.op=op
        self.div_test=div_test
        self.true_monkey:Monkey=true_monkey
        self.false_monkey:Monkey=false_monkey
        self.seen_items = 0
        self.dev_amount = dev_amount
    @staticmethod
    def get_monkey(lines:list) -> "Monkey":
        starting_items = [int(v) for v in lines[1].split(": ")[1].split(", ")]
        op = eval("lambda old: "+lines[2].split(": new = ")[1])
        div_test = int(lines[3].split("divisible by ")[1])
        true_monkey_idx = int(lines[4].split("throw to monkey ")[1])
        false_monkey_idx = int(lines[5].split("throw to monkey ")[1])
        return Monkey(starting_items, op, div_test, true_monkey_idx, false_monkey_idx)
    def inspect_items(self):
        while len(self.items):
            item = self.items.pop(0)
            self.seen_items += 1
            new_level = self.op(item)
            new_level = self.op(item)%self.dev_amount
            if new_level%self.div_test == 0:
                self.true_monkey.items.append(new_level)
            else:
                self.false_monkey.items.append(new_level)

monkeys: typing.List[Monkey] = []
for i,line in enumerate(dta):
    if line.startswith("Monkey"):
        monkeys.append(Monkey.get_monkey(dta[i:]))
total_sum = prod([m.div_test for m in monkeys])
for monkey in monkeys:
    monkey.true_monkey = monkeys[monkey.true_monkey]
    monkey.false_monkey = monkeys[monkey.false_monkey]
    monkey.dev_amount = total_sum
# %%
# for i in range(20):

for i in tqdm(range(10000)):
    for monkey in monkeys:
        monkey.inspect_items()
# %%
x1,x2 = sorted([m.seen_items for m in monkeys])[-2:]
x1*x2
# %%
