

#%%
import typing
from tqdm.auto import tqdm
from math import prod, ceil
from functools import lru_cache
from dataclasses import dataclass
import re
#%%
with open("day19.txt") as fp:
    data = fp.read()
test_data="""
Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian.
"""
# %%
line_data = data.strip().split("\nBlueprint ")
test_line_data = test_data.strip().split("\nBlueprint ")
# %%
dta = line_data

# %%
dta = test_line_data

# %%
@dataclass
class Blueprint:
    ore_robot: tuple
    clay_robot: tuple
    obs_robot: tuple
    geode_robot: tuple
    ore_cost: tuple = None
    clay_cost: tuple = None
    obs_cost: tuple = None
    g_cost: tuple = None

    def __post_init__(self):
        self.ore_cost = (self.ore_robot[0],0,0,0)
        self.clay_cost = (self.clay_robot[0],0,0,0)
        self.obs_cost = (self.obs_robot[0]+self.clay_cost[0]*self.obs_robot[1],self.obs_robot[1],0,0)
        self.g_cost = (
            self.geode_robot[0]+self.obs_cost[0]*self.geode_robot[2],
            self.obs_cost[1]*self.geode_robot[2],
            self.geode_robot[2],
            1
        )

    @classmethod
    def from_text(cls, lines):
        _, lines = lines.split(":")
        ore_text, clay_text, obs_text, geode_text, _ = lines.split(".")
        number_patt = re.compile("\d+")
        ore_cost = (int(number_patt.findall(ore_text)[0]),0,0)
        clay_cost = (int(number_patt.findall(clay_text)[0]),0,0)
        obs_cost = [int(n) for n in number_patt.findall(obs_text)]
        obs_cost = (obs_cost[0],obs_cost[1],0)
        geode_cost = [int(n) for n in number_patt.findall(geode_text)]
        geode_cost = (geode_cost[0],0,geode_cost[1])
        return Blueprint(ore_robot = ore_cost, clay_robot=clay_cost, obs_robot=obs_cost, geode_robot=geode_cost)

    def __getitem__(self, index):
        if index==0: return self.ore_robot
        if index==1: return self.clay_robot
        if index==2: return self.obs_robot
        if index==3: return self.geode_robot
        raise IndexError("Index out of bounds")

blueprints = [Blueprint.from_text(bp_text) for bp_text in dta]
blueprint = blueprints[0]
blueprint

# %%
def calc_time_needed(build_cost,production_rate):
    time_needed_to_build = max(((bc/(pr+1e-15)) for bc,pr in zip(build_cost,production_rate)))
    return round(time_needed_to_build)+1

PROD_INCREASES = (
    (1,0,0,0),
    (0,1,0,0),
    (0,0,1,0),
    (0,0,0,1),
)
@lru_cache(maxsize=None)
def calc_max_stocks_added(time_remaining, production_rate, current_stocks, costs, max_spend):
    if time_remaining<=0:
        # return (current_stocks[-1], [(production_rate, current_stocks, time_remaining)])
        return current_stocks[-1]
    # max_score = (current_stocks[-1]+time_remaining*production_rate[-1], [(production_rate, current_stocks, time_remaining)])
    max_score = current_stocks[-1]+time_remaining*production_rate[-1]
    if time_remaining>20:
        print(time_remaining)
    for i,build_cost in enumerate(costs):
        if production_rate[i] >= max_spend[i]: continue 

        time_needed_to_build = max((((bc-cs)/(pr+1e-15)) for bc,pr,cs in zip(build_cost,production_rate,current_stocks)))
        time_needed_to_build = max(time_needed_to_build,0)
        time_needed_to_build = ceil(time_needed_to_build)+1
        if time_needed_to_build >= time_remaining: continue

        new_prod_rate = (
            production_rate[0]+PROD_INCREASES[i][0],
            production_rate[1]+PROD_INCREASES[i][1],
            production_rate[2]+PROD_INCREASES[i][2],
            production_rate[3]+PROD_INCREASES[i][3]
        )
        new_time_remaining = time_remaining -time_needed_to_build
        new_stocks = (
            min(current_stocks[0]+time_needed_to_build*production_rate[0]-build_cost[0], max_spend[0]+(max_spend[0]-production_rate[0])*new_time_remaining),
            min(current_stocks[1]+time_needed_to_build*production_rate[1]-build_cost[1], max_spend[1]+(max_spend[1]-production_rate[1])*new_time_remaining),
            min(current_stocks[2]+time_needed_to_build*production_rate[2]-build_cost[2], max_spend[2]+(max_spend[2]-production_rate[2])*new_time_remaining),
            current_stocks[3]+time_needed_to_build*production_rate[3],
        )
        # score, history = calc_max_stocks_added(time_remaining-time_needed_to_build, new_prod_rate, new_stocks, costs, max_spend)
        score = calc_max_stocks_added(time_remaining-time_needed_to_build, new_prod_rate, new_stocks, costs, max_spend)
        # new_history = [(production_rate, current_stocks, time_remaining)]+history
        max_score = max(max_score, score)
    return max_score

# %%  
score = 0
for pbid, blueprint in enumerate(blueprints, start=1):
    blueprint_costs = tuple([blueprint[i] for i in range(4)])
    max_spend = tuple([max([blueprint[j][i] for j in range(4)]) for i in range(3)]+[float('inf')])
    geode = calc_max_stocks_added(24, (1,0,0,0), (0,0,0,0), blueprint_costs, max_spend)
    calc_max_stocks_added.cache_clear()
    print(geode[0], pbid)
    score += geode[0]*pbid
score
# %%  
geodes = []
for pbid, blueprint in enumerate(blueprints[:3], start=1):
    blueprint_costs = tuple([blueprint[i] for i in range(4)])
    max_spend = tuple([max([blueprint[j][i] for j in range(4)]) for i in range(3)]+[float('inf')])
    geode = calc_max_stocks_added(32, (1,0,0,0), (0,0,0,0), blueprint_costs, max_spend)
    calc_max_stocks_added.cache_clear()
    print(geode, pbid)
    geodes.append(geode)
prod(geodes)
# %%  
# %%  
# %%  
# %%  
# %%  
# %%  
# %%  
# %%  
# # %%
# def calc_score_for_nothing(time_remaining, production_rate, current_stocks, g_cost):
#     return sum([(pr*time_remaining+c)/nc for pr,c,nc in zip(production_rate, current_stocks, g_cost)])

# def calc_score_build(time_remaining, production_rate, current_stocks, g_cost, build_cost, prod_increase):
#     time_needed_to_build = max(((bc/(pr+1e-15)) for bc,pr in zip(build_cost,production_rate)))
#     time_needed_to_build = round(time_needed_to_build)+1
#     if time_needed_to_build>time_remaining: 
#         new_stocks = (
#             current_stocks[0]+time_remaining*production_rate[0],
#             current_stocks[1]+time_remaining*production_rate[1],
#             current_stocks[2]+time_remaining*production_rate[2],
#             current_stocks[3]+time_remaining*production_rate[3],
#         )
#         return calc_score_for_nothing(time_remaining, production_rate, current_stocks, g_cost), production_rate, 0, new_stocks
#     do_nothing = calc_score_for_nothing(time_needed_to_build-1, production_rate, current_stocks, g_cost)
#     new_prod_rate = (
#         production_rate[0]+prod_increase[0],
#         production_rate[1]+prod_increase[1],
#         production_rate[2]+prod_increase[2],
#         production_rate[3]+prod_increase[3]
#     )
#     new_stocks = (
#         current_stocks[0]+time_needed_to_build*production_rate[0]-build_cost[0],#couldnt collect ore for one round
#         current_stocks[1]+time_needed_to_build*production_rate[1]-build_cost[1],
#         current_stocks[2]+time_needed_to_build*production_rate[2]-build_cost[2],
#         current_stocks[3]+time_needed_to_build*production_rate[3],
#     )
#     score_after_build = calc_score_for_nothing(time_remaining-time_needed_to_build, new_prod_rate, current_stocks, g_cost)
#     return do_nothing+score_after_build, new_prod_rate, time_remaining-time_needed_to_build, new_stocks


# def calc_action_score(production_rate, current_stocks, time_remaining, blueprint:Blueprint):
#     # sum_nc = sum(blueprint.g_cost)
#     build_ore_robot = calc_score_build(
#         time_remaining, 
#         production_rate, 
#         current_stocks, 
#         blueprint.g_cost, 
#         blueprint.ore_robot, 
#         (1,0,0,0)
#     )
#     build_clay_robot = calc_score_build(
#         time_remaining, 
#         production_rate, 
#         current_stocks, 
#         blueprint.g_cost, 
#         blueprint.clay_robot, 
#         (0,1,0,0)
#     )
#     build_obs_robot = calc_score_build(
#         time_remaining, 
#         production_rate, 
#         current_stocks, 
#         blueprint.g_cost, 
#         blueprint.obs_robot, 
#         (0,0,1,0)
#     )
#     build_g_robot = calc_score_build(
#         time_remaining, 
#         production_rate, 
#         current_stocks, 
#         blueprint.g_cost, 
#         blueprint.geode_robot, 
#         (0,0,0,1)
#     )
#     return max((build_ore_robot, build_clay_robot, build_obs_robot, build_g_robot))
# #%%
# calc_action_score((1, 10, 0, 0), (10, 135, 0, 0), 30, blueprint)
# # %%
# remaining_time = 30
# prod_rate = (1,0,0,0)
# current_stocks = (0,0,0,0)
# while remaining_time>0:
#     _, prod_rate, remaining_time, current_stocks = calc_action_score(prod_rate, current_stocks, remaining_time, blueprint)
#     print(prod_rate, remaining_time, current_stocks)
# %%
