

#%%
import typing
from tqdm.auto import tqdm
from math import prod, ceil
from functools import lru_cache
from dataclasses import dataclass
from collections import deque
import re
#%%
with open("day21.txt") as fp:
    data = fp.read()
test_data="""
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
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
class ReverseOperator:
    def __init__(self):
        self.operator_list = []
        self.prev = None
    def __truediv__(self, other):
        # return self.x / other
        self.operator_list.append(f"prev_val * {other}")
        return self

    def __rtruediv__(self, other):
        # return other / self.x
        self.operator_list.append(f"{other} / prev_val")
        return self

    def __eq__(self, other):
        self.prev = other
        return True

    def __add__(self, other):
        self.operator_list.append(f"prev_val - {other}")
        return self
    def __radd__(self, other):
        self.operator_list.append(f"prev_val - {other}")
        return self

    def __mul__(self, other):
        self.operator_list.append(f"prev_val / {other}")
        return self
    def __rmul__(self, other):
        self.operator_list.append(f"prev_val / {other}")
        return self

    def __sub__(self, other):
        # x-other
        self.operator_list.append(f"prev_val + {other}")
        return self
    def __rsub__(self, other):
        # other - x
        self.operator_list.append(f"{other} - prev_val")
        return self
    def eval(self):
        prev_val = self.prev
        for op in reversed(self.operator_list):
            prev_val = eval(op, {"prev_val":prev_val})
        return prev_val

class Operator:
    def __init__(self, value=None, expression=None, deps=None):
        self.value = value
        self.expr_fn = expression
        self.deps = deps
    @staticmethod
    def from_line(ln):
        key, expr = ln.split(": ")
        deps = None
        try:
            value = int(expr)
        except ValueError as e:
            value = None
            deps = expr.split(" ")[::2]
        return key, Operator(value, expr, deps)
    def eval(self, others):
        if self.value is None:
            glbs = {k: others[k].eval(others) for k in self.deps}
            self.value = eval(self.expr_fn, glbs)
        return self.value

# %%
monkeys = dict((Operator.from_line(l) for l in dta))
# %% PT 1
monkeys["root"].eval(monkeys)
# %% PT2
# Apply monkey patch
monkeys["root"].expr_fn = " == ".join(monkeys["root"].deps)
monkeys["humn"].value = ReverseOperator()
monkeys["root"].eval(monkeys)
monkeys["humn"].value.eval()
