def game(x, y):
    if x >= 100: return y%2==0
    if y == 0: return 0
    steps = [game(x+1,y-1), game(x+4,y-1), game(x*3,y-1)]
    return any(steps) if y%2!=0 else all(steps)

print("19:", [x for x in range(1,100) if game(x,2)])
print("20:", [x for x in range(1,100) if not game(x,1) and game(x,3)])
print("21:", [x for x in range(1,100) if not game(x,2) and game(x,4)]) 

# Written by Vsevolod Flovitskiy.