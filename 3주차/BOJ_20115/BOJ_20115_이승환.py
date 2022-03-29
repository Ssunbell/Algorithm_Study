N = int(input())

energy_drink = list(map(int,input().split()))

# 가장 많은 양의 에너지드링크와 가장 적은 양의 에너지 드링크를 선택
# 가장 적은 양의 에너지 드링크의 절반을 가장 많은 양의 에너지드링크에 더함
# 이 과정을 반복
# 결과적으로 가장 많은 양의 에너지 드링크는 그대로
# 나머지 에너지 드링크는 절반의 양이 합쳐짐

max_ed = max(energy_drink)
energy_drink.remove(max_ed)

print(sum(energy_drink)/2 + max_ed)