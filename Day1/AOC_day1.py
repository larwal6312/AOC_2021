import numpy as np

### Part 1 ###

increase = 0
count = 0

numbers = np.loadtxt('readings.list')
line_count = len(numbers) - 1

while count < line_count:
    if numbers[count + 1] > numbers[count]:
        increase += 1
    count += 1

print("Number of increases: {}".format(increase))

### Part 2 ###

increase = 0
count = 0
line_count = len(numbers) - 4
first3 = []
second3 = [0,0,0]

while count <= line_count:
    first3.append(numbers[count])
    first3.append(numbers[count + 1])
    first3.append(numbers[count + 2])
    second3.append(numbers[count + 1])
    second3.append(numbers[count + 2])
    second3.append(numbers[count + 3])
    if sum(second3) > sum(first3):
        increase += 1
    first3 = []
    second3 = []
    count += 1

print("Number of increases: {}".format(increase))
