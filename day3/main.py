def ans1():
    count = 0
    r = 0
    c = 0
    while r+1 < len(G):
        r += 1
        c += 3
        if G[r][c%len(G[r])] == '#':
            count += 1
    return count
    

def ans2():
    count = 0
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    ans = 1
    for (dc, dr) in slopes:
        c = 0
        r = 0
        count = 0
        while r < len(G):
            c += dc
            r += dr
            if r < len(G) and G[r][c%len(G[r])] == '#':
                count += 1
        ans *= count
    return ans
        

G = []
with open('input') as f:
    for line in f:
        G.append(list(line.strip()))


print(ans1())
print(ans2())
