#xor по одному символу/детектирование

from lab0 import delimiter
from lab0 import WrongFormatException
from lab0 import test as test_str

string = "041811045013111e5003110615501815025000151f001c1550111e1450021503041f0215"
s = "abcdfacd"

eng_letter_frequency = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074 ]


def count_letter_frequency(string):
    frequencies = []
    letters_list = list(string)
    for i in range(97, 97+26):
        frequencies.append(round(letters_list.count(chr(i))/26, 4) * 100)

    t = 0
    for letter in string:
        if ord(letter) < 97 or ord(letter) > 123:
            frequencies[0] += 50
        t +=1
        if t > 50:
            break
    return frequencies


def count_error(frq, expected_frq=eng_letter_frequency):
    return sum(list(map(lambda x, y: abs(x-y), frq, expected_frq)))


def xor_decode_str_to_list(hex_str, key):
    return list(map(lambda x: chr(int(x, base=16) ^ key), delimiter(hex_str, 2)))


def decode(hex_string):
    prob_list = []
    for i in range(256):
        ansii_list = xor_decode_str_to_list(hex_string, i)
        let_frq = count_letter_frequency(ansii_list)
        prob_list.append(count_error(let_frq))
    index = prob_list.index(min(prob_list))
    return "".join(xor_decode_str_to_list(hex_string, index)), index, min(prob_list)

def decode_by_single(hex_string):
    prob_list = []
    for i in range(256):
        ansii_list = xor_decode_str_to_list(hex_string, i)
        let_frq = count_letter_frequency(ansii_list)
        prob_list.append(count_error(let_frq))
    index = prob_list.index(min(prob_list))
    return "".join(xor_decode_str_to_list(hex_string, index))


if __name__ == "__main__":
    string = "130c14061143170c4307061017110c1a43020d43060d170a110643130f020d06174d"
    print("Зашифрованная строка в HEX формате: {0}".format(string))
    decoded_str, i, prob = decode(string)
    print("Расшифрованная строка (ANSII): {0}".format(decoded_str))
    print("Ключ (код ANSII-символа в DEC): {0}".format(i))
    print(decode_by_single(string))


