'''
문제
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

입력
첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

예제 입력 1
2 4
CAAB
ADCB

예제 출력 1
3

'''
def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])]) # 시작점 큐

    while q:
        x, y, ans = q.pop()

        for i in range(4):
            nx = x + dx[i]      # 상하좌우 갈 수 있는지
            ny = y + dy[i]

            # 영역벗어 나는지 알파벳 중복되는지
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny]))        #조건을 만족한다면 그 좌표, 알파벳 추가 (set은 중복 허용 안되기 때문에 겹치지않음)
                answer = max(answer, len(ans)+1)          #이전의 dist값과 현재 dist값 비교하여 높은값 등록

board = []
R, C = map(int, input().split(' '))

for i in range(R):
    b = list(input())
    board.append(b)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] # 상, 하, 좌, 우

answer = 1
BFS(0, 0)
print(answer)