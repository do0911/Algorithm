'''
자연수가 주어졌을 때, 그 정수가 정확히 3개의 삼각수의 합으로 표현될 수 있는지 없는지를 판단해주는 프로그램을 만들어라. 단, 3개의 삼각수가 모두 달라야 할 필요는 없다.

입력
프로그램은 표준입력을 사용한다. 테스트케이스의 개수는 입력의 첫 번째 줄에 주어진다. 각 테스트케이스는 한 줄에 자연수 K (3 ≤ K ≤ 1,000)가 하나씩 포함되어있는 T개의 라인으로 구성되어있다.

출력
프로그램은 표준출력을 사용한다. 각 테스트케이스에대해 정확히 한 라인을 출력한다. 만약 K가 정확히 3개의 삼각수의 합으로 표현될수 있다면 1을, 그렇지 않다면 0을 출력한다.

예제 입력 1
3
10
20
1000
예제 출력 1
1
0
1
'''
from itertools import product
triple_arr = []
count = 0
def triple(n):
    return int(n * ( n + 1 ) / 2)

for i in range(1, 50):
    triple_arr.append(triple(i))

p = list(product(triple_arr, repeat=3))

t = int(input())

for i in range(t):
    k = int(input())
    for j in range(len(p)):
        if k == sum(p[j]):
            count = 1
            break
    print(count)
    count = 0

'''
itertools.product 를 사용해 데카르트곱을 활용
'''