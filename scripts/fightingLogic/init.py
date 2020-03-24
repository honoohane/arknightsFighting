import hashlib
import random
from scripts.skills import common


def input_name():
    name = input("input Red 1:")
    return name


def status(name):
    hashresult = hashlib.sha256(name.encode('utf-8')).hexdigest()
    dic = {}
    dic['name'] = name
    hphash = int(hashresult[24:30], 16) % 3000
    dic['hp'] = 1000 + hphash  # hp 1000-4000
    atkhash = int(hashresult[0:6], 16) % 900
    dic['atk'] = 100 + atkhash  # atk 100-1000
    maghash = int(hashresult[12:18], 16) % 900
    dic['mag'] = 100 + maghash  # mag 100-1000
    defehash = int(hashresult[30:36], 16) % 400
    dic['def'] = defehash  # def 0-400
    spdhash = int(hashresult[6:12], 16) % 30
    dic['spd'] = 10 + spdhash  # dex 10-40
    intehash = int(hashresult[18:24], 16) % 90
    dic['int'] = 10 + intehash  # int 10-100
    classjudge(dic)
    print(dic)
    return dic


def classjudge(dic):
    strength = dic['hp']/3000+dic['def']/400
    physical = dic['atk']/900+dic['spd']/30
    magic = dic['mag']/900+dic['int']/90
    if strength >= physical and strength >= magic:
        if dic['hp']/3000 > dic['def']/400:
            dic['class'] = '重装'
        else:
            dic['class'] = '先锋'
    elif physical >= magic:
        if dic['atk']/900 > dic['spd']/30:
            dic['class'] = '近卫'
        else:
            dic['class'] = '狙击'
    else:
        if dic['mag']/900 > dic['int']/90:
            dic['class'] = '法师'
        else:
            dic['class'] = '治疗'


def position(*args, color='red'):
    order = ['重装','先锋','近卫','治疗','狙击','法师']
    team = []
    for item in order:
        for chara in args:
            if chara['class'] == item:
                team.append(chara)
    for i in range(len(team)):
        team[i]['team'] = color+str(i+1)
    print(team)
    return team


def spdjudge(red, blue):
    chara = red+blue
    list = []
    for item in chara:
        for i in range(item['spd']):
            list.append(item['team'])
    return random.choice(list)


def defenderjudge(team):
    number = random.random()
    if len(team) == 1:
        return team[0]
    elif len(team) == 2:
        if number < 0.7:
            return team[0]
        else:
            return team[1]
    elif len(team) == 3:
        if number < 0.7:
            return team[0]
        elif number > 0.85:
            return team[1]
        else:
            return team[2]


def dropoutcheck(team):
    for i in range(len(team)-1, -1, -1):
        if team[i]['hp'] < 0:
            del team[i]



def battle(red, blue):
    while red and blue:
        attacker_team = spdjudge(red, blue)
        for item in red+blue:
            if item['team'] == attacker_team:
                attacker = item
        if attacker in red:
            defender = defenderjudge(blue)
        elif attacker in blue:
            defender = defenderjudge(red)
        common.attack(attacker, defender)
        dropoutcheck(red)
        dropoutcheck(blue)





