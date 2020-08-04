'''
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.
'''
def dfs(x):
    li.remove(x)
    for i in range(1, n+1):
        if i in li and a[x][i] == 1:
            dfs(i)

n,m = map(int, input().split(' '))
a = [[0] * (n+1) for i in range(n+1)]
li = [i for i in range(1, n+1)]
count = 0

for i in range(m):
    x, y = map(int, input().split())
    a[x][y] = 1
    a[y][x] = 1

for i in range(1, n+1):
    if i in li:
        dfs(i)
        count += 1

print(count)

'''
리스트에 정점목록을 넣어두고 끊기면 다음 정점부터 시작하도록 설계
'''