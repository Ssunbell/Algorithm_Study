cases = int(input())


for i in range(cases):
    n, *scores = map(int, input().split())
    average = sum(scores) / n
    results = int()
    for score in scores:
        if average < score:
            results += 1
    truth = (results / n) * 100
    print(f'{truth:.3f}%')
