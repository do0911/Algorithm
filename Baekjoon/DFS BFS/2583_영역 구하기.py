'''
눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.

M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다. 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다. 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다.

출력
첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.

예제 입력 1
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
예제 출력 1
3
1 7 13
'''
from collections import deque

m, n, k = map(int, input().split())
a = [[0] * n for i in range(m)]

dx = [-1, 1, 0, 0]  #상하좌우
dy = [0, 0, -1, 1]

l = []

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for j in range(x1, x2):
        for k in range(y1, y2):
            a[k][j] = 1

def bfs(s1, s2):
    de = deque()
    de.append([s1, s2])     #초기 좌표 큐에넣고 count 1
    a[s1][s2] = 1
    c = 1

    while de:
        x, y = de.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:  #맵 범위안이면
                if a[nx][ny] == 0:           #이미 방문한곳이 아니면
                    a[nx][ny] = 1
                    c += 1
                    de.append([nx, ny])
    l.append(c)


for i in range(m):            #맵을 돌며 0인부분찾으면 기점으로 bfs시작
    for j in range(n):
        if a[i][j] == 0:
            bfs(i, j)

print(len(l))
l.sort()
for i in l:
    print(i, end=' ')