n, m = map(int, input().split(' '))
dna = []
output= ''
h = 0
for i in range(n):
    dna.append(input())

for i in range(m):
    count = [0, 0, 0, 0]
    for j in range(n):
        if dna[j][i] == 'A':
            count[0] += 1
        elif dna[j][i] == 'C':
            count[1] += 1
        elif dna[j][i] == 'G':
            count[2] += 1
        elif dna[j][i] == 'T':
            count[3] += 1

    if count.index(max(count)) == 0:
        output += 'A'
        h += n - count[0]
    elif count.index(max(count)) == 1:
        output += 'C'
        h += n - count[1]
    elif count.index(max(count)) == 2:
        output += 'G'
        h += n - count[2]
    elif count.index(max(count)) == 3:
        output += 'T'
        h += n - count[3]
print(output)
print(h)