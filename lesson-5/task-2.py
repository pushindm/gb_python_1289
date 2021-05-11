# print simple statistics
with open(r"task-2\task-2.txt") as f:
    for idx, line in enumerate(f):
        print(f"The number of words in a current line: {len(line.split())}")
    print(f"Total number of lines: {idx + 1}")
