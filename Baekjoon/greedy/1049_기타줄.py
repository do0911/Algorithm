'''
끊어진 기타줄의 개수 N과 기타줄 브랜드 M개가 주어지고, 각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의 가격, 낱개로 살 때의 가격이 주어질 때, 적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. N은 100보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에는 각 브랜드의 패키지 가격과 낱개의 가격이 공백으로 구분하여 주어진다. 가격은 0보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫째 줄에 기타줄을 적어도 N개 사기 위해 필요한 돈의 최솟값을 출력한다.

예제 입력 1
4 2
12 3
15 4

예제 출력 1
12
'''
n, m = map(int, input().split(' '))
price = []
money=0
for i in range(m):
    a, b = map(int, input().split(' '))
    price.append([a, b])

price_1 = sorted(price, key=lambda x:x[1])
price_6 = sorted(price, key=lambda x:x[0])

if price_6[0][0]/6 <= price_1[0][1]:
    money = n//6 * price_6[0][0]
    remain = n % 6
    if remain * price_1[0][1] <= price_6[0][0]:
        money += remain * price_1[0][1]
    else:
        money += price_6[0][0]
else:
    money = price_1[0][1] * n

print(money)

'''
'''