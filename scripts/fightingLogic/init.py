import hashlib


def input_name():
    name = input("input Red 1:")
    return name


def status(name):
    hashresult = hashlib.sha256(name.encode('utf-8')).hexdigest()
    atkhash = int(hashresult[0:6], 16) % 900
    atk = 100 + atkhash  # atk 100-1000
    spdhash = int(hashresult[6:12], 16) % 30
    spd = 10 + spdhash  # dex 10-40
    maghash = int(hashresult[12:18], 16) % 900
    mag = 100 + maghash  # mag 100-1000
    intehash = int(hashresult[18:24], 16) % 90
    inte = 10 + intehash  # int 10-100
    hphash = int(hashresult[24:30], 16) % 3000
    hp = 1000 + hphash  # hp 1000-4000
    defehash = int(hashresult[30:36], 16) % 400
    defe = defehash  # def 0-400
    print('HP:' + str(hp))
    print('ATK:' + str(atk))
    print('MAG:' + str(mag))
    print('DEF:' + str(defe))
    print('SPD:' + str(spd))
    print('INT:' + str(inte))
    return atk, spd, mag, inte, hp, defe