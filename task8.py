#детектирование ECB
from lab0 import delimiter

path = "detectEcb.txt"
f = open(path, "r")
text = f.read()
string_list = text.split("\n")[:-3]
i = 0
for string in string_list:
    divided = delimiter(string, 32)
    uniq = set(divided)
    for e in uniq:
        if divided.count(e) > 1:
            print("Строка: {0}\nБлок: {1}".format(i, e))
    i += 1