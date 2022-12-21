#%%
with open("day2.txt") as fp:
    data = fp.read()
# %%
games = data.split("\n")
# %%
def score_win_loose(a,b):
    diff = b-a
    if diff==0: return 3
    if diff==1 or diff==-2 : return 6
    return 0


def decode(game):
    a,b = game.split(' ')
    return ord(a)-ord('A'), ord(b)-ord('X')
# %%
def game_score(game):
    a,b=decode(game)
    b=get_hand(a,b)
    return score_win_loose(a,b)+b+1
# %%
sum((game_score(g) for g in games if len(g)>0))
# %%
def get_hand(a,b):
    if b == 0:
        r = a-1
        if r < 0: return 2
        return r
    if b ==1:
        return a
    r = a+1
    if r > 2: return 0
    return r

# %%
