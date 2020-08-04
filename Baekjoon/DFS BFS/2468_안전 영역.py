'''
이와 같이 장마철에 내리는 비의 양에 따라서 물에 잠기지 않는 안전한 영역의 개수는 다르게 된다. 위의 예와 같은 지역에서 내리는 비의 양에 따른 모든 경우를 다 조사해 보면 물에 잠기지 않는 안전한 영역의 개수 중에서 최대인 경우는 5임을 알 수 있다.

어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오.

입력
첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다. N은 2 이상 100 이하의 정수이다. 둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다. 각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다. 높이는 1이상 100 이하의 정수이다.

출력
첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.

예제 입력 1
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

예제 출력 1
5
'''
from _collections import deque

def bfs(j, k):
    q = deque()
    q.append([j, k])
    visit[j][k] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    q.append([nx, ny])

n = int(input())
a = []
answer = 0

for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(1, 101):
    visit = [[0] * n for i in range(n)]
    count = 0
    for j in range(n):
        for k in range(n):
            if a[j][k] < i:
                visit[j][k] = 1
    for j in range(n):
        for k in range(n):
            if visit[j][k] == 0:
                bfs(j,k)
                count += 1

    if count > answer:
        answer = count

print(answer)

'''
변수이름 기존 함수랑 겹치지 않기!!
'''
