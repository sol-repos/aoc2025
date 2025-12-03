with open("input.txt") as file:
    txt = file.read()[:-1]

banks = txt.split('\n')
banks = [list(map(int, line)) for line in banks]

# part 1
total = 0
for bank in banks:
    highest_first = max(bank[:-1])
    first_index = bank.index(highest_first)
    highest_second = max(bank[first_index+1:])
    max_jolt = int(str(highest_first) + str(highest_second))
    total += int(str(highest_first) + str(highest_second))
print("Part 1:", total)

# part 2
MAX_BATTERIES = 12
total = 0
for bank in banks:
    highest_strings = []
    prev_index = -1
    start_offset = 0
    for battery_index in range(MAX_BATTERIES):
        max_found = -1
        max_index = -1
        available_batteries = bank[prev_index+1:len(bank)-MAX_BATTERIES+battery_index+1]
        for i in range(len(available_batteries)):
            if available_batteries[i] > max_found:
                max_found = available_batteries[i]
                max_index = i
        highest_strings.append(str(max_found))
        prev_index = max_index + start_offset
        start_offset = prev_index + 1
    
    max_jolt = int("".join(highest_strings))
    total += max_jolt
print("Part 2:", total)