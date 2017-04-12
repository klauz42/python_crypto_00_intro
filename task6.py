#взлом xor с повторяющимся ключом

from lab0 import delimiter, b64tohex as base64_to_hex_str
from task3 import decode_by_single
from math import ceil, floor
from time import clock

def task():
    path = "breakRepeatedKeyXor.txt"
    f = open(path, "r")
    b64 = f.read().replace("\n", '')
    hex_str = base64_to_hex_str(b64)
    hex_list = delimiter(hex_str, 2)
    text_len = len(hex_list)
    str_array = []
    dec_str_arr = []
    decoded_strings = []
    start = 25
    finish = 40

    t1 = clock()
    for k in range(start, finish):
        str_array.clear()
        for i in range(k):
            str_array.append("")
            for n in range(text_len):
                if (n % k) == i:
                    str_array[i] += hex_list[n]
            str_array[i] = decode_by_single(str_array[i])
        decoded_strings.append("")
        iters = ceil(text_len/k)
        print(iters)
        #max_len_of_str = len(str_array[0])
        for j in range(iters):
            for s in str_array:
                if len(s) > j:
                    decoded_strings[k - start] += s[j]
                else:
                    break
        print("Ключ длины {0}: \n".format(k))
        print(decoded_strings[k-start])
    t2 = clock()
    print(t2 - t1)

if __name__ == "__main__":
    task()

'''
for k in range(start, finish):
    str_array.clear()
    for i in range(k):
        str_array.append("")
        for n in range(text_len):
            if (n % k) == i:
                str_array[i] += hex_list[n]
        str_array[i] = decode_by_single(str_array[i])
    decoded_strings.append("")
    iters = ceil(text_len/k)
    print(iters)
    #max_len_of_str = len(str_array[0])
    for j in range(iters):
        for s in str_array:
            if len(s) > j:
                decoded_strings[k - start] += s[j]
            else:
                break
    print("Ключ длины {0}: \n".format(k))
    print(decoded_strings[k-start])
'''