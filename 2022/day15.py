#%%
import typing
from tqdm.auto import tqdm
from math import prod
#%%
with open("day15.txt") as fp:
    data = fp.read()
test_data="""
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""
# %%
line_data = data.strip().split("\n")
test_line_data = test_data.strip().split("\n")
# %%
dta = line_data

# %%
dta = test_line_data

# %%
sensor_beacons = []
for l in dta:
    _,sx,bx = l.split("x=")
    _,sy,by = l.split("y=")
    sx = int(sx.split(",")[0])
    bx = int(bx.split(",")[0])
    sy = int(sy.split(":")[0])
    by = int(by)
    sensor_beacons.append(((sx,sy),(bx,by)))

# %%
all_sensors = set(d[0] for d in sensor_beacons)
all_beacons = set(d[1] for d in sensor_beacons)
def print_map(sensors=None,beacons=None):
    min_x = 0
    max_x = 0
    for s in top_map.values():
        min_x = min(min_x,s.min())
        max_x = max(max_x,s.max())
    def get_badge(x,y):
        if (x,y) in all_sensors: return 'S'
        if (x,y) in all_beacons: return 'B'
        if sensors is not None and sensors[0]==x and sensors[1]==y:
            return 's'
        if beacons is not None and beacons[0]==x and beacons[1]==y:
            return 'b'
        return '.' if x not in top_map.get(y,{}) else '#' 
    dta = [[get_badge(x,y) for x in range(min_x,max_x+1)] for y in range(min(top_map.keys()),max(top_map.keys())+1)]
    print('\n'.join([''.join(r) for r in dta]))

# %%
import bisect
class IntervalSet():
    def __init__(self) -> None:
        self.interval_starts=[]
        self.interval_ends=[]
    def add(self,start, end):
        # self.interval_starts[idx] <= start
        # end >= start
        # self.interval_ends[idx] >= self.interval_starts[idx]
        ost,oed = start,end
        if end <=start: 
            # print(start,end,"\n----", "skipped", "\n----")
            return
        idx = bisect.bisect(self.interval_starts, start)
        self.interval_starts.insert(idx, start)
        self.interval_ends.insert(idx, end)
        while idx < len(self.interval_ends)-1 and self.interval_starts[idx+1]<=end:
            start = min(start, self.interval_starts.pop(idx+1))
            end = max(end, self.interval_ends.pop(idx+1))
        while idx > 0 and start<=self.interval_ends[idx-1]:
            start = min(start, self.interval_starts.pop(idx-1))
            end = max(end, self.interval_ends.pop(idx-1))
            idx -= 1
        self.interval_starts[idx]=start
        self.interval_ends[idx]=end
        # print(ost,oed,"\n----\n", self, "\n----")
    def __contains__(self, o):
        idx = bisect.bisect(self.interval_starts, o)
        if idx < len(self.interval_starts) and self.interval_starts[idx]<=o and self.interval_ends[idx]>o:
            return True
        if idx > 0 and self.interval_starts[idx-1]<=o and self.interval_ends[idx-1]>o:
            return True
        return False
    def __len__(self):
        return sum((e-s for e,s in zip(self.interval_ends, self.interval_starts)))
    def min(self):
        return self.interval_starts[0]
    def max(self):
        return self.interval_ends[-1]-1
    def __repr__(self) -> str:
        if len(self.interval_starts) == 0: return "{}"
        return '\n'.join([f'{s} -> {e}' for s,e in zip(self.interval_starts, self.interval_ends)])

# %%
top_map = {}
top_map_s = {}
top_map_b = {}
# y_s_to_check = [2000000]
for sensors,beacons in sensor_beacons:
    dist = abs(sensors[0]-beacons[0])+abs(sensors[1]-beacons[1])
    y_top_map_s = top_map_s.setdefault(sensors[1], set())
    y_top_map_b = top_map_b.setdefault(beacons[1], set())
    y_top_map_s.add(sensors[0])
    y_top_map_b.add(beacons[0])

    for y in range(sensors[1]-dist,sensors[1]+dist+1):
        y_set = top_map.setdefault(y, IntervalSet())
        y_len = abs(sensors[1]-y)
        y_set.add(
            sensors[0]-dist+y_len,sensors[0]+dist+1-y_len
        )
    # for y in y_s_to_check:
    #     if y<sensors[1]-dist or y > sensors[1]+dist: continue
    #     y_set = top_map.setdefault(y, IntervalSet())
    #     y_len = abs(sensors[1]-y)
    #     y_set.add(
    #         sensors[0]-dist+y_len,sensors[0]+dist+1-y_len
    #     )
    print_map(sensors,beacons )
    # print()

len(top_map[2000000])-len(top_map_b[2000000])
# len(top_map[2000000])-len(top_map_b[2000000])

# %% PT 2
top_map = {}
top_map_s = {}
top_map_b = {}
y_s_to_check = range(4000000)
for sensors,beacons in tqdm(sensor_beacons):
    dist = abs(sensors[0]-beacons[0])+abs(sensors[1]-beacons[1])
    y_top_map_s = top_map_s.setdefault(sensors[1], set())
    y_top_map_b = top_map_b.setdefault(beacons[1], set())
    y_top_map_s.add(sensors[0])
    y_top_map_b.add(beacons[0])

    # for y in range(sensors[1]-dist,sensors[1]+dist+1):
    #     y_set = top_map.setdefault(y, IntervalSet())
    #     y_len = abs(sensors[1]-y)
    #     y_set.add(
    #         sensors[0]-dist+y_len,sensors[0]+dist+1-y_len
    #     )
    for y in y_s_to_check:
        if y<sensors[1]-dist or y > sensors[1]+dist: continue
        y_set = top_map.setdefault(y, IntervalSet())
        y_len = abs(sensors[1]-y)
        y_set.add(
            sensors[0]-dist+y_len,sensors[0]+dist+1-y_len
        )
    # print_map(sensors,beacons )
    # print()
def get_value():
    for y in tqdm(range(4000000)):
        if top_map[y].interval_starts[0] > 0 or top_map[y].interval_ends[0] < 4000000:
            for x in tqdm(range(4000000)):
                if x not in top_map[y]:
                    return x,y
    
resx,res_y = get_value()
4000000*resx+res_y
# %%
yval = 3249288
def get_xval():
    for x in tqdm(range(4000000)):
        if x not in top_map[yval]:
            return x
xval = get_xval()
# %%
import portion
top_map = {}
top_map_s = {}
top_map_b = {}
y_s_to_check = [2000000]
for sensors,beacons in sensor_beacons:
    dist = abs(sensors[0]-beacons[0])+abs(sensors[1]-beacons[1])
    y_top_map_s = top_map_s.setdefault(sensors[1], set())
    y_top_map_b = top_map_b.setdefault(beacons[1], set())
    y_top_map_s.add(sensors[0])
    y_top_map_b.add(beacons[0])

    # for y in range(sensors[1]-dist,sensors[1]+dist+1):
    for y in y_s_to_check:
        if y<sensors[1]-dist or y > sensors[1]+dist: continue
        y_set = top_map.setdefault(y, portion.empty())
        y_len = abs(sensors[1]-y)
        top_map[y] = y_set | portion.closedopen(sensors[0]-dist+y_len,sensors[0]+dist+1-y_len)
        print(top_map[y])
    # print_map(sensors,beacons )
    # for y in y_s_to_check:
    #     if y<sensors[1]-dist or y > sensors[1]+dist: continue
    #     y_set = top_map.setdefault(y, IntervalSet())
    #     y_len = abs(sensors[1]-y)
    #     y_set.add(
    #         se
sum([v._intervals[0].upper - v._intervals[0].lower for v in top_map[2000000]])
# %%
