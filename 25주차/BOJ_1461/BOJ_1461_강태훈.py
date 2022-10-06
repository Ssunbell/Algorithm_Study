# 백준 도서관_ Greedy
import sys
input = sys.stdin.readline


def split_arr_mlen(arr, m):
    return [arr[i:i+m] for i in range(0, len(arr), m)]


n, m = map(int, input().split())
book_location = sorted(map(int, input().split()))
pos_val = []
neg_val = []
answer, longest_path = 0, -1
for n in book_location:
    if n >= 0:
        pos_val.append(n)
    else:
        neg_val.append(n)
    longest_path = max(longest_path, abs(n))
pos_val.reverse()
for i in split_arr_mlen(neg_val, m):
    answer += abs(min(i)) * 2
for i in split_arr_mlen(pos_val, m):
    answer += max(i) * 2
answer -= longest_path
print(answer)
