from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for i in range(n)]
nums.sort()

class Statistics():
    def average(self):
        avg = round(sum(nums) / n)
        if -1 < avg < 0:
            avg = int(round(abs(avg)))
        print(avg)
        return

    def median(self):
        med = nums[n//2]
        print(med)
        return

    def mode(self):
        cnt = Counter(nums).most_common()
        mod = []
        for i in cnt:
            if i[1] == cnt[0][1]:
                mod.append(i[0])
            else:
                break
        if len(mod) == 1:
            print(mod[0])
        else:
            mod.sort()
            print(mod[1])
        return

    def range(self):
        r = max(nums) - min(nums)
        if len(nums) == 1:
            r = 0
        print(abs(r))
        return


stat = Statistics()
stat.average()
stat.median()
stat.mode()
stat.range()
