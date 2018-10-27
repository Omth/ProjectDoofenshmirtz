test = int(input())
for i in range(test):
    input()
    input()
    g = max(map(int,input().split(' ')))
    mg = max(map(int,input().split(' ')))
    if (g>mg or g==mg):
        print ('Godzilla')
    else:
        print ('MechaGodzilla')
