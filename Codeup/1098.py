'''
첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
두 번째 줄에 놓을 수 있는 막대의 개수(n)
세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.

입력값의 정의역은 다음과 같다.

1 <= w, h <= 100
1 <= n <= 10
d = 0 or 1
1 <= x <= 100-h
1 <= y <= 100-w


출력
모든 막대를 놓은 격자판의 상태를 출력한다.
막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.
단, 각 숫자는 공백으로 구분하여 출력한다.


입력 예시   
5 5
3
2 0 1 1
3 1 2 3
4 1 2 5

출력 예시
1 1 0 0 0
0 0 1 0 1
0 0 1 0 1
0 0 1 0 1
0 0 0 0 1
'''
h, w = map(int, input().split(' '))

a = [[0 for _ in range(w)] for _ in range(h)]


num = int(input())

for i in range(num):
    stick = [int(x) for x in input().split(' ')]
    a[stick[2]-1][stick[3]-1] = 1

    if stick[1] == 0:
        for j in range(stick[0]):
            a[stick[2]-1][stick[3]-1+j] = 1

    else:
        for j in range(stick[0]):
            a[stick[2]-1+j][stick[3]-1] = 1

for i in range(h):
    for j in range(w):
        print(a[i][j], end=' ')
    print()
