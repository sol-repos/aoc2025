with open("input.txt") as file:
    lines = file.readlines()

instructions = [line.replace("\n", "") for line in lines]

pos = 50
zero_count_1 = 0
zero_count_2 = 0
for instruction in instructions:
    isLeft = instruction[0] == "L"
    distance = int(instruction[1:])
    
    revs = distance // 100
    rest = distance % 100
    
    zero_count_2 += revs
    if (revs != 0):
        print(revs, "revs", instruction)
    
    if isLeft:
        if pos - rest < 0 and pos != 0:
            print(instruction, pos)
            zero_count_2 += 1
        pos = (pos - distance) % 100
    else:
        if pos + rest > 100:
            print(instruction, pos)
            zero_count_2 += 1
        pos = (pos + distance) % 100
    
    if pos == 0:
        print(instruction, pos)
        zero_count_1 += 1
        zero_count_2 += 1

print("Part 1:", zero_count_1)
print("Part 2:", zero_count_2)