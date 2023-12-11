def read_file(file_name):
    input_array = []
    with open(file_name, "r") as file:
        for line in file:
            input_array.append(line.strip())
        return input_array


lines = read_file("input.txt")

times = list(map(int, lines[0].split(":")[1].split()))
distances = list(map(int, lines[1].split(":")[1].split()))
print(times, distances)

full_time = int("".join(list(map(str, times))))
full_dist = int("".join(list(map(str, distances))))
print(full_time, full_dist)


# speeds = [distances[i] / times[i] for i in range(len(times))]

def getWinnings(time, dist):
    wins = []
    for i in range(time):
        # 7 - 0 x 0
        trav = (time - i) * i
        if trav > dist:
            wins.append(i)
    return wins


def getWinsLen(time, dist):
    win = 0
    for i in range(time):
        # Calculation : 7 - 0 x 0
        trav = (time - i) * i
        if trav > dist:
            win = i
            break
    # total_wins = time - 2 * win - 1
    total_wins = time - 2 * win + 1
    print(total_wins)
    return total_wins


ans = 1
for i in range(len(times)):
    # print(getWinnings(times[i], distances[i]), len(getWinnings(times[i], distances[i])))
    # ans *= len(getWinnings(times[i], distances[i]))
    print(getWinsLen(times[i], distances[i]))
    ans *= getWinsLen(times[i], distances[i])

print(ans)
print(getWinsLen(full_time, full_dist))
# print(len(getWinnings(full_time, full_dist)))
