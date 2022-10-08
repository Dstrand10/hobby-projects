import hashlib

with open("input.txt") as f:
    secretKey = f.read()
    testnumber = 0
    while True:
        if "00000" == hashlib.md5((secretKey + str(testnumber)).encode('utf-8')).hexdigest()[0:5]:
            print("Answer 1: " + str(testnumber))
            break
        testnumber += 1

    testnumber = 0
    while True:
        if "000000" == hashlib.md5((secretKey + str(testnumber)).encode('utf-8')).hexdigest()[0:6]:
            print("Answer 2: " + str(testnumber))
            break
        testnumber += 1