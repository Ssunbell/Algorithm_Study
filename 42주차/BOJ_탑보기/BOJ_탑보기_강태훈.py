import sys
input = sys.stdin.readline

def check_viewable(n, building_len, answer):
    stack = []
    for idx, v in building_len:
        while len(stack)>0 and stack[-1][1] <= v:
            stack.pop()
        answer[idx][0] += len(stack)
        if len(stack) > 0 :
            diff = abs(stack[-1][0] - (idx))
            if diff < answer[idx][2]:
                answer[idx] = [answer[idx][0], stack[-1][0],diff]
            elif diff == answer[idx][2] and stack[-1][0] < answer[idx][1]:
                answer[idx][1] = stack[-1][0]
        stack.append([idx,v])
    return

def main():
    n = int(input())
    building_len = list(enumerate(map(int, input().split())))
    answer = [[0, float("inf"), float("inf")] for _ in range(n)]

    check_viewable(n, building_len, answer)
    check_viewable(n, building_len[::-1], answer)

    print(*["0" if answer[i][0]<=0 else f"{answer[i][0]} {answer[i][1]+1}" for i in range(n)], sep="\n")

if __name__ == "__main__":
    main()


"""
 *     *
 * *   *
 * * * *
 * * * *
** *** *
** *** *
********
"""