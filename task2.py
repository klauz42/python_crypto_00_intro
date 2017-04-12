#xor двух буферов

from lab0 import delimiter
from lab0 import WrongFormatException
from lab0 import test as test_str

def hex_str_to_int_list(hexstr):
    return list(map(lambda x: int(x, base=16), delimiter(hexstr, 2)))

def xor(hex_str_1, hex_str_2):
    if len(hex_str_1) == len(hex_str_2):
        return "".join(list(map(lambda z: "0"*(2 - len(z)) + z, list(map(lambda x, y: hex(x ^ y)[2:], hex_str_to_int_list(hex_str_1), hex_str_to_int_list(hex_str_2))))))
    else:
        raise WrongFormatException

    '''
    bytes_list_1 = hex_str_to_int_list(hex_str_1)
    bytes_list_2 = hex_str_to_int_list(hex_str_2)
    xored_hex_str_list = list(map(lambda z: "0"*(2 - len(z)) + z, list(map(lambda x, y: hex(x ^ y)[2:], bytes_list_1, bytes_list_2))))
    return "".join(xored_hex_str_list)
    '''


str1 = "8f29336f5e9af0919634f474d248addaf89f6e1f533752f52de2dae0ec3185f818c0892fdc873a69"
str2 = "bf7962a3c4e6313b134229e31c0219767ff59b88584a303010ab83650a3b1763e5b314c2f1e2f166"
try:
    print(xor(str1, str2))
except WrongFormatException:
    print("Строки должны иметь одинаковую длину")