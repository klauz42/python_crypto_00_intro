#xor с повторяющмся ключем

from lab0 import delimiter

message = "Never trouble about trouble until trouble troubles you!"
key1 = "ICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEI"
key = "ICE"

def xor_repeated_key(msg, k):
    msg_list = list(map(lambda x: ord(x), delimiter(msg, 1)))
    k_list = list(map(lambda x: ord(x), delimiter(k, 1)))
    key_len = len(k)
    msg_len = len(msg)
    xored_list_tmp = []
    for i in range(msg_len):
        xored_list_tmp.append(hex(msg_list[i] ^ k_list[i % key_len])[2:])
    xored_list = list(map(lambda x: "0"*(2 - len(x)) + x, xored_list_tmp))
    return "".join(xored_list)


if __name__ == "__main__":
    print("Cообщение: {0}".format(message))
    print("Ключ: {0}".format(key))
    print("Результат XOR: {0}".format(xor_repeated_key(message, key)))