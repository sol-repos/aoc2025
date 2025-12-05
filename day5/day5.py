with open("input.txt") as file:
    txt = file.read()[:-1]
parts = txt.split("\n\n")

ranges = [list(map(int, line.split("-"))) for line in parts[0].split("\n")]
ids = [int(line) for line in parts[1].split("\n")]

class MultiRange:
    def __init__(self):
        self.ranges = []

    def merge_ranges(self, merge_start, start, end):
        redundant_indices = []
        new_start = min(start, self.ranges[merge_start][0])
        new_end = max(end, self.ranges[merge_start][1])
        for i in range(merge_start, len(self.ranges)):
            s, e = self.ranges[i]
            if s <= new_end + 1:
                new_end = max(new_end, e)
                redundant_indices.append(i)
            else:
                break
        for i in reversed(redundant_indices):
            self.ranges.pop(i)
        self.ranges.insert(merge_start, (new_start, new_end))

    def add_range(self, start, end):
        for i in range(len(self.ranges)):
            s, e = self.ranges[i]
            if end < s - 1:
                self.ranges.insert(i, (start, end))
                return
            elif start <= e + 1:
                self.merge_ranges(i, start, end)
                return
        self.ranges.append((start, end))
    
    def contains(self, value):
        for s, e in self.ranges:
            if s <= value <= e:
                return True
        return False

mr = MultiRange()
for r in ranges:
    start, end = r
    mr.add_range(start, end)

# Part 1
fresh_count = 0
for food_id in ids:
    if mr.contains(food_id):
        fresh_count += 1
print("Part 1:",fresh_count)

# Part 2
total_fresh = 0
for s, e in mr.ranges:
    total_fresh += (e - s + 1)
print("Part 2:", total_fresh)