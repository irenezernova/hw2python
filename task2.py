S = int(input('sum: '))
P = int(input('mult: '))
flag = False
for X in range(1, 1001):
    for Y in range(1, 1001):
        if X * Y == P and X + Y == S:
            flag = True
            print(X, Y)
if not flag:
    print('такого не бывает')
