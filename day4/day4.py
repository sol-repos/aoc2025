with open("./input.txt") as f:
    lines = f.read().splitlines()
cards = [[[int(num.strip()) for num in side.split(" ") if num.strip() != ""] for side in line.split(": ")[1].split(" | ")] for line in lines]

total = 0
winningCounts = [0 for card in cards]
for c in range(len(cards)):
    card = cards[c]
    winningNumbers = card[0]
    myNumbers = card[1]
    winningCount = 0
    score = 0
    for num in myNumbers:
        if num in winningNumbers:
            winningCount += 1
            winningCounts[c] += 1
    if(winningCount >= 1):
        score = 2**(winningCount-1)
    total += score

print(total)

copies = [1 for card in cards]
for c in range(len(cards)):
    card = cards[c]
    winningCount = winningCounts[c]
    for i in range(1, winningCount+1):
        if(c+i < len(cards)):
            copies[c+i] += copies[c]
        
print(sum(copies))