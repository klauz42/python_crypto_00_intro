#детектирование по одному символу

from task3 import delimiter, decode

path = "detectSingleCHXor_tasks\detectSingleXor01"
f = open(path, "r")


def sort_by_prob(inp):
     return min(inp)


def xored_str_detecting(file):
    lines = []
    indexes = []
    probs = []
    for line in f:
        lines.append(tuple(decode(line[:-3]))[0])
        #indexes.append(tuple(decode(line[:-3]))[1])
        probs.append(tuple(decode(line[:-3]))[2])
    print((lines[probs.index(min(probs))]))

if __name__ == "__main__":
    xored_str_detecting(f)
