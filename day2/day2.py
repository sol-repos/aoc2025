import math

with open("test_input.txt") as file:
    lines = file.read()

input_line = lines.replace("\n", "")
ranges = input_line.split(",")
ranges = [el.split("-") for el in ranges]

# part 1
total = 0
for r in ranges:
    start = r[0]
    end = r[1]

    start_half = (len(start))//2
    if start_half < 1:
        start_half = 1
    start_scnd_half = len(start) - start_half
    start_leading = start[:start_half]

    end_half = (len(end))//2
    if end_half < 1:
        end_half = 1
    end_scnd_half = len(end) - end_half
    end_leading = end[:end_half]
    max_end = end_leading + "9" * end_scnd_half

    test_leading = start_leading
    while int(test_leading * 2) <= int(end_leading + "9" * end_scnd_half):
        test_num = test_leading + test_leading
        if int(test_num) >= int(start) and int(test_num) <= int(end):
            print("Found:", test_num)
            total += int(test_num)
        test_leading = str(int(test_leading) + 1)

print("Part 1:", total)

# part 2 (unfinished)
total = 0
for r in ranges:
    start = r[0]
    end = r[1]

    max_pattern_len = len(end)//2
    if max_pattern_len < 1:
        max_pattern_len = 1
    found_nums = set()
    for pattern_len in range(1, max_pattern_len + 1):
        for pattern_num in range(int(start[:pattern_len]), int("9" * pattern_len) + 1):
            pattern = str(pattern_num)
            min_repeat = math.ceil(len(start) / pattern_len)
            if min_repeat < 2:
                min_repeat = 2
            max_repeat = len(end) // pattern_len
            if pattern 
            for repeat_count in range(min_repeat, max_repeat + 1):
                test_num = pattern * repeat_count
                print('test_num:', test_num, "range:", start, "-", end)
                if int(test_num) >= int(start) and int(test_num) <= int(end) and test_num not in found_nums:
                    print("Found:", test_num)
                    total += int(test_num)
                    found_nums.add(test_num)
                
print("Part 2:", total)