# https://adventofcode.com/2022/day/7#part1
from collections import defaultdict

# read the file containing the input and store its contents
with open("input.txt", "rt") as f:
    str_input = f.read()

# split the input at line end
list_input = str_input.splitlines()

# keeps track of the current -file- path (where are we at the moment)
current_path = []

# will store the various paths with value as the path's/directory's total size
d = defaultdict(int)

# split each item of list_input at the spaces and iterate through them: ["$", "cd", ".."]
for i in [x.split(" ") for x in list_input]:
    # check if cd command
    if i[1] == "cd":
        # check if '..' present then move out of the current directory
        if i[2] == '..':
            current_path.pop()
        else:
            # if we have cd but no dots then the third value (i[2]) is a directory we need to move in to
            current_path.append(i[2])
    # if 'ls', then continue (stops the current iteration at this point, and goes to next iteration)
    elif i[1] == "ls":
        continue
    # if no command(cd, ls) was found, then look for digits (file size)
    elif i[0].isdigit():
        # convert the value to integer
        file_size = int(i[0])
        # we add the above file_size to the current directory and all directories above it
        for idx in range(len(current_path)):  # dir-example: / , a, e
            d['/'.join(current_path[:idx + 1])] += file_size

total = 0

# iterate over all our directories looking only for those with total sizes less than or equal to 100000
for a in d:
    if d[a] <= 100_000:
        total += d[a]

# print out the total/ANSWER to the question
print("ANSWER=", total)

