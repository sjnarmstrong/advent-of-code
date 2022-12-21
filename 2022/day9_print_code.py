def get_text_results():
    nodes = [(0,0), H]+tails
    nodes_and_markers = [(0,0), H]+tails+list(T_Places)
    max_x = max([t[0] for t in nodes_and_markers])
    min_x = min([t[0] for t in nodes_and_markers])
    max_y = max([t[1] for t in nodes_and_markers])
    min_y = min([t[1] for t in nodes_and_markers])

    spots = [["." for _ in range(min_x,max_x+1)] for _ in range(min_y,max_y+1)]

    for n in T_Places:
        spots[n[1]][n[0]] = '#'

    for i,n in enumerate(nodes):
        marker = 's' if i ==0 else 'm' if i==1 else str(i-1)
        spots[n[1]][n[0]] = marker

    return '\n'.join([''.join(r) for r in spots])