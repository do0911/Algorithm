def dfs(v):
    print(v, end=' ')       #방문한 노드 출력
    visit[v] = 1            #방문한 노드 기록
    for i in range(1, n + 1):
        if visit[i] == 0 and s[v][i] == 1:  #방문한 노드의 행을 돌며 인접하고 방문한 적이 없는 점이 발견될 때 재귀호출
            dfs(i)

def bfs(v):
    queue = [v]   #큐에 현재 노드 삽입
    visit[v] = 1  #방문한 노드 기록
    while (queue): #큐를 돈다
        v = queue[0]  # 큐에서 첫번째 pop해서 출력
        print(v, end=' ') ##
        del queue[0]  ##
        for i in range(1, n + 1):  #pop한 노드의 인접값을 찾아서 큐에 삽입
            if visit[i] == 0 and s[v][i] == 1:
                queue.append(i)   ##
                visit[i] = 1      ## 삽입하고 방문표시

n, m, v = map(int, input().split())
s = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1

dfs(v)
visit = [0 for i in range(n + 1)]
print()
bfs(v)

"""



"""