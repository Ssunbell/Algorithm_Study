import sys

input_s = lambda : sys.stdin.readline().strip()

n = int(input_s())
ori_seq = list(map(int,input_s().split()))
num_seq = int(input_s())
seqs = [list(map(int,input_s().split())) for _ in range(num_seq)]
revers_seq = []
for s in ori_seq:
    if s == 1:
        revers_seq.append(3)
    elif s == 2:
        revers_seq.append(4)
    elif s == 3:
        revers_seq.append(1)
    else:
        revers_seq.append(2)
revers_seq = revers_seq[::-1]
result = []
for seq in seqs:
    for i in range(n):
        if seq[i:] + seq[:i] == ori_seq or seq[i:]+seq[:i] == revers_seq:
            result.append(seq)
            break

print(len(result))
for seq in result:
    print(*seq)

