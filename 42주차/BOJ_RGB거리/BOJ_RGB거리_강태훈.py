import sys
input = sys.stdin.readline

def main(nums):
    for i in range(1, len(nums)):
        for j in range(3):
            nums[i][j] += min(nums[i-1][(j+1)%3], nums[i-1][(j-1)%3])
    print(min(nums[-1]))

if __name__ == "__main__":
    nums = [list(map(int, input().split())) for _ in range(int(input()))]
    main(nums)