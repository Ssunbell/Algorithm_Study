import sys
input = sys.stdin.readline

def solve(target_len, k, num, stack=[]):
    for i, val in enumerate(num):
        while k > 0 and stack and stack[-1] < num[i]:
            stack.pop()
            k -= 1
        stack.append(val)
    return ''.join(stack[:target_len])

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(solve(n-k, k, input(), []))
    # for n,k,num,answer in [
    #     [4,2,"1924",94],
    #     [7,3,"1231234",3234],
    #     [10,4,"4177252841",775841]
    # ]:
    #     print(solve(n, k, num, []), answer)

# 메모리 초과
# def solve(n, k, num, answer=[]):
#     if k==0:
#         return "".join(answer+num)
#     target = num[:k+1]
#     big = max(target)
#     idx = target.index(big)
#     answer.append(big)
#     return solve(n-idx, k-idx, num[idx+1:], answer=answer)