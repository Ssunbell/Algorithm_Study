import sys

input_s = lambda : sys.stdin.readline().strip()

rmax, n = map(int, input_s().split())

commands = []
for i in range(n):
    commands.append(input_s())

# direction = ["E","S","W","N"]
curr_d = 0
curr = [0, 0]
result = 0
for comm in commands:
    com, num = comm.split()
    num = int(num)
    if com == "MOVE":
        if curr_d == 0:
            curr[0] += num
        elif curr_d == 1:
            curr[1] -= num
        elif curr_d == 2:
            curr[0] -= num
        elif curr_d == 3:
            curr[1] += num
    elif com == "TURN":
        if num == 0:
            curr_d -= 1
            curr_d = curr_d % 4
        elif num == 1:
            curr_d += 1
            curr_d = curr_d % 4
    if curr[0] < 0 or curr[0] > rmax or curr[1] < 0 or curr[1] > rmax:
        result = -1
        break

if result != -1:
    result = f"{curr[0]} {curr[1]}"

print(result)
