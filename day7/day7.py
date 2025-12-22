with open("input.txt") as file:
    txt = file.read()[:-1]
rows = txt.split("\n")
lasers_x = set([rows[0].index("S")])
lasers_x_timelines = { x: 0 for x in range(len(rows[0])) }
lasers_x_timelines[rows[0].index("S")] = 1

print(rows[0])

def print_row(row, lasers_x):
    row_str = ""
    for x in range(len(row)):
        if x in lasers_x:
            row_str += str(lasers_x_timelines[x])
        else:
            row_str += row[x]
    print(row_str)

total_splits = 0
total_timelines = 1
for y in range(1, len(rows)):
    row = rows[y]
    new_lasers_x = set()
    new_lasers_x_timelines = { x: 0 for x in range(len(rows[0]))}
    for x in lasers_x:
        if row[x] == ".":
            new_lasers_x.add(x)
            new_lasers_x_timelines[x] += lasers_x_timelines[x]
        elif row[x] == "^":
            new_lasers_x.add(x - 1)
            new_lasers_x.add(x + 1)
            new_lasers_x_timelines[x - 1] += lasers_x_timelines[x]
            new_lasers_x_timelines[x + 1] += lasers_x_timelines[x]
            total_timelines += lasers_x_timelines[x]
            total_splits += 1
    lasers_x = new_lasers_x
    lasers_x_timelines = new_lasers_x_timelines
    print_row(row, lasers_x)

print("Part 1:", total_splits)
print("Part 2:", total_timelines)