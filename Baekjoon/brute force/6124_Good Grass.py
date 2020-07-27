'''
00 01 02
10 11 12
20 21 22

01 02 03
11 12 13
21 22 23

02 03 04
12 13 14
22 23 24

10 11 12
20 21 22
30 31 32
'''

r, c = map(int, input().split(' '))
map_ = []
max = 0
max_map = []
count = 0
for i in range(r):
    a = list(map(int, input().split()))
    map_.append(a)

for i in range(r-2):
    for j in range(c-2):
        count = map_[i][j] + map_[i][j+1] + map_[i][j+2] + map_[i+1][j] + map_[i+1][j+1] + map_[i+1][j+2] + map_[i+2][j] + map_[i+2][j+1] + map_[i+2][j+2]
        if max < count:
            max =  count
            max_map.append([i+1,j+1])
        count = 0

a = max_map.pop()

print(max)
for i in a:
    print(i, end=' ')