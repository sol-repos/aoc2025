with open("test_input.txt") as file:
    txt = file.read()[:-1]
lines = txt.split("\n")
operations = [el for el in lines[-1].split(" ") if el != ""]
num_lines = [list(map(int, [el for el in line.split(" ") if el != ""])) for line in lines[:-1]]

def apply_operation(nums, operation):
    if operation == "+":
        return sum(nums)
    else :
        result = 1
        for n in nums:
            result *= n
        return result

total = 0
for i in range(len(operations)):
    numbers = [num_lines[j][i] for j in range(len(num_lines))]
    op = operations[i]
    result = apply_operation(numbers, op)
    total += result
print("Part 1:", total)