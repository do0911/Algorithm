'''
문제
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

예제 입력 1
110
예제 출력 1
99
예제 입력 2
1
예제 출력 2
1
예제 입력 3
210
예제 출력 3
105
'''
n = int(input())
count = 0

for i in range(1, n+1):
    if i <= 99:
        count += 1
    else:
        num = list(map(int, str(i)))
        if num[1] - num[0] == num[2] - num[1]:
            count += 1
print(count)

'''
1~99까지는 모두 등차수열이고 1000보다 작으므로 범위내의 등차수열인 세자리수를 더한다 
'''