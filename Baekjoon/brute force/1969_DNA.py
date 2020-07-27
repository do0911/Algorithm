'''
����
DNA�� � ���������� �����ϴ� �����̴�. �� DNA�� ���� �ٸ� 4������ ��Ŭ����Ƽ��� �̷���� �ִ�(Adenine, Thymine, Guanine, Cytosine). �츮�� � DNA�� ������ ǥ���� ��, �� DNA�� �̷�� ��Ŭ����Ƽ���� ù���ڸ� ���� ǥ���Ѵ�. ���࿡ Thymine-Adenine-Adenine-Cytosine-Thymine-Guanine-Cytosine-Cytosine-Guanine-Adenine-Thymine�� �̷���� DNA�� �ִٰ� �ϸ�, ��TAACTGCCGAT���� ǥ���� �� �ִ�. �׸��� Hamming Distance�� ���̰� ���� �� DNA�� ���� ��, �� ��ġ�� ��Ŭ��Ƽ�� ���ڰ� �ٸ� ���� �����̴�. ���࿡ ��AGCAT"�� ��GGAAT"�� ù ��° ���ڿ� �� ��° ���ڰ� �ٸ��Ƿ� Hamming Distance�� 2�̴�.

�츮�� �� ���� ������ ����. n���� ���̰� ���� DNA�� �־��� ���� ��(�� DNA�� a1a2a3a4...�̶�� ����) Hamming Distance�� ���� ���� ���� DNA s�� ���ϴ� ���̴�. ��, s�� a1�� Hamming Distance + s�� a2�� Hamming Distance + s�� a3�� Hamming Distance ... �� ���� �ּҰ� �ȴٴ� �ǹ��̴�.

�Է�
ù �ٿ� DNA�� �� N�� ���ڿ��� ���� M�� �־�����. �׸��� ��° �ٺ��� N+1��° �ٱ��� N���� DNA�� �־�����. N�� 1,000���� �۰ų� ���� �ڿ����̰�, M�� 50���� �۰ų� ���� �ڿ����̴�.

���
ù° �ٿ� Hamming Distance�� ���� ���� ���� DNA �� ����ϰ�, ��° �ٿ��� �� Hamming Distance�� ���� ����Ͻÿ�. �׷��� DNA�� ���� �� ���� ������ ���������� ���� �ռ��� ���� ����Ѵ�.

���� �Է� 1 
5 8
TATGATAC
TAAGCTAC
AAAGATCC
TGAGATAC
TAAGATGT
���� ��� 1 
TAAGATAC
7

'''
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