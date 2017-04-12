#Конвертирование из hex в base64 и наоборот

class WrongFormatException(Exception):
    def __init__(self):
        pass

test = "0123456789abcdef"
base64alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

def dlmtr(string, step, checklen):
    strlen = len(string)
    if strlen % checklen != 0:
        raise WrongFormatException
    res = strlen % step
    if res == 0:
        return [int((string[i * step: (i + 1) * step]), base=16) for i in range(strlen // step)]
    else:
        lst = []
        lst = [int((string[i * step: (i + 1) * step]), base=16) for i in range(strlen // step)]

        lst.append(string[-res:])
        return lst

def hex_to_b64(hexstr):
    hexlist = dlmtr(hexstr, 6, 2)
    b64list = []
    tmp = ""
    if len(hexstr) % 6 == 0:
        for h in hexlist:
            tmp = ""
            for i in range(4):
                j = h % 64
                tmp += base64alphabet[j]
                h = h // 64
            tmp = tmp[::-1]
            b64list.append(tmp)
    elif len(hexstr) > 6:
        hexlist0 = hexlist[:-1]
        for h in hexlist0:
            tmp = ""
            for i in range(4):
                j = h % 64
                tmp += base64alphabet[j]
                h = h // 64
            tmp = tmp[::-1]
            b64list.append(tmp)
        if len(hexlist[-1]) == 4:
            h = int(hexlist[-1], base=16)
            tmp = ""
            tmp += "="
            j = h % 16
            j = j << 2
            tmp += base64alphabet[j]
            h = h // 16
            for i in range(2):
                j = h % 64
                tmp += base64alphabet[j]
                h = h // 64
            tmp = tmp[::-1]
            b64list.append(tmp)
        elif len(hexlist[-1]) == 2:
            h = int(hexlist[-1], base=16)
            tmp = ""
            tmp += "=="
            j = h % 4
            j = j << 4
            tmp += base64alphabet[j]
            h = h // 4
            j = h % 64
            tmp += base64alphabet[j]
            h = h // 64
            tmp = tmp[::-1]
            b64list.append(tmp)

    else:
        if len(hexlist[0]) == 4:
            h = int(hexlist[0], base=16)
            tmp = ""
            tmp += "="
            j = h % 16
            j = j << 2
            tmp += base64alphabet[j]
            h = h // 16
            for i in range(2):
                j = h % 64
                tmp += base64alphabet[j]
                h = h // 64
            tmp = tmp[::-1]
            b64list.append(tmp)
        elif len(hexlist[0]) == 2:
            h = int(hexlist[-1], base=16)
            tmp = ""
            tmp += "=="
            j = h % 4
            j = j << 4
            tmp += base64alphabet[j]
            h = h // 4
            j = h % 64
            tmp += base64alphabet[j]
            h = h // 64
            tmp = tmp[::-1]
            b64list.append(tmp)


    return "".join(b64list)

#создание словаря {'base64': 'bin'}
listbin = [("0"*(8-len(bin(i))) + bin(i)[2:(len(bin(i))+1)]) for i in range(64)]
b64tobin_dict = {chr(65 + i): listbin[i] for i in range(26)}
b64tobin_dict.update({chr(97 + i): listbin[i + 26] for i in range(26)})
b64tobin_dict.update({str(i): listbin[i + 52] for i in range(10)})
b64tobin_dict['+'] = '111110'
b64tobin_dict['/'] = '111111'
b64tobin_dict['='] = ''


def delimiter(string, step):
    if len(string) % step == 0:
        return [string[i * step: (i + 1) * step] for i in range(len(string) // step)]
    else:
        raise WrongFormatException


def hexToBinStringList(hexStr):
    hexStrList = delimiter(hexStr, 2)
    return list(map(lambda x: bin(int(x, base=16))[2:].rjust(2, "0"), hexStrList))


def bslToB64(bsl):
    numstep = len(bsl) // 3
    by3 = [bsl[i * 3] + bsl[i * 3 + 1] + bsl[i * 3 + 2] for i in range(numstep)]
    res = len(bsl) % 3
    resSum = ""
    if res != 0:
        for i in range(res):
            resSum += bsl[-(res - i)]

        if res == 2:
            resSum += '00'
        elif res == 1:
            resSum += '0000'
        by3.append(resSum)

    intList = list(map(lambda x: int(x, base=2), by3))

    b64List = []
    tmp = []
    for i in range(numstep):
        for j in range(4):
            tmp.append(intList[i] % 64)
            intList[i] //= 64
        tmp.reverse()
        b64List.extend(tmp)
        tmp.clear()
    if res != 0:                            #добавить "достоточные символы"

        if res == 1:
            for j in range(2):
                tmp.append(intList[-1] % 64)
                intList[-1] //= 64
            tmp.reverse()
            b64List.extend(tmp)
            tmp.clear()
            b64List.extend([64, 64])
        else:
            for j in range(3):
                tmp.append(intList[-1] % 64)
                intList[-1] //= 64
            tmp.reverse()
            b64List.extend(tmp)
            tmp.clear()
            b64List.extend([64])
            tmp.reverse()
            b64List.extend(tmp)
    b64strList = list(map(lambda x: base64alphabet[x], b64List))
    b64str = "".join(b64strList)
    return b64str


def b64tohex(b64string):
    b64len = len(b64string)
    if len(b64string) % 4 != 0:
        raise WrongFormatException
    binstr = ""
    for i in range(b64len-2):
       if b64string[i] == '=' or (b64string[i] not in base64alphabet):
           raise WrongFormatException
       else:
            binstr += b64tobin_dict[b64string[i]]
    for i in range(2):
        binstr += b64tobin_dict[b64string[b64len - 2 + i]]
    if b64string[-2] == '=':
        binstr = binstr[:-4]
    elif b64string[-1] == '=':
        binstr = binstr[:-2]
    #разделяем двоичную строку на байты
    bytes = delimiter(binstr, 8)

    hexList = list(map(lambda x: hex(int(x, base=2))[2:].rjust(2, "0"), bytes)) #ssssska
    hexstr = "".join(hexList)
    return hexstr

def tudasuda(string):
    print("HEX: {0}".format(string))
    b64 = hex_to_b64(string)
    print("Base64: {0}".format(b64))
    hexStr = b64tohex(b64)
    print("HEX again: {0}\n\n".format(hexStr))

def sudatuda(b64):
    print("Base64: {0}".format(b64))
    hexStr = b64tohex(b64)
    print("HEX: {0}".format(hexStr))
    b64new = hex_to_b64(hexStr)
    print("Base64 again: {0}\n\n".format(b64new))

if __name__ == "__main__":
    try:
        test = "0123456789abcdef"
        string = "faea8766efd8b295a633908a3c0828b22640e1e9122c3c9cfb7b59b7cf3c9d448bf04d72cde3aaa0"
        tudasuda(string)
        tudasuda(test)

        while True:
            s1 = input("Введите строку в HEX-формате: ")
            if s1 == "exit":
                break
            else:
                tudasuda(s1)

            s2 = input("Введите строку в Base64-формате: ")
            if s2 == "exit":
                break
            else:
                sudatuda(s2)

    except WrongFormatException:
        print("Строка имеет неверный формат!")
    except ValueError:
        print("Строка имеет неверный формат!!")
