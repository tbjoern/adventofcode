output = 0

with open("input.txt", "r") as f:
    for line in f:
    	numbers = line.split()
    	numbers = map(lambda x: (int(x)), numbers)

    	if numbers[0] + numbers[1] > numbers[2] and numbers[0] + numbers[2] > numbers[1] and numbers[2] + numbers[1] > numbers[0]:
    		output += 1

print output