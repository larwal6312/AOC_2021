### Part 1 ###

x = 0
y = 0

with open('position.txt', 'r') as f:
    for line in f:
        line_split = line.split()
        direction = line_split[0]
        amount = int(line_split[1])
        if direction == "forward":
            x += amount
        elif direction == "down":
            y += amount
        elif direction == "up":
            y -= amount

print(x * y)

### Part 2 ###
