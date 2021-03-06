'''
문제
2~15개의 서로 다른 자연수로 이루어진 리스트가 있을 때, 이들 중 리스트 안에 자신의 정확히 2배인 수가 있는 수의 개수를 구하여라.

예를 들어, 리스트가 "1 4 3 2 9 7 18 22"라면 2가 1의 2배, 4가 2의 2배, 18이 9의 2배이므로 답은 3이다.

입력
입력은 여러 개의 테스트 케이스로 주어져 있으며, 입력의 끝에는 -1이 하나 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 2~15개의 서로 다른 자연수가 주어진다. 각 자연수는 100보다 작으며, 리스트의 끝은 0으로 판별한다(0은 리스트에 속하지 않는다).

출력
각 테스트 케이스마다 한 줄에 걸쳐 정답을 출력한다.

예제 입력 1
1 4 3 2 9 7 18 22 0
2 4 8 10 0
7 5 11 13 1 3 0
-1
예제 출력 1
3
2
0

'''
from itertools import product

while True:
    count = 0
    n = []

    n = list(map(int, input().split()))

    if n == [-1]:
        break

    del n[len(n)-1]

    n = list(product(n, repeat=2))

    for i in range(len(n)):
        if n[i][0] / n[i][1] == 2:
            count += 1

    print(count)

'''
product를 이용해 모든 케이스 비교
'''