import random


def attack(attacker, defencer, type='physical'):
    atk = attacker['atk']
    if type == 'magic':
        atk = attacker['mag']
    res = defencer['def']
    if type == 'magic':
        res = res * 0.8
    dmg = atk*(1-res/(100+res))*(random.random()+0.5)
    defencer['hp'] -= dmg
    print(attacker['name'] + ' 对 ' + defencer['name'] +
          ' 发起了攻击！造成了' + str(dmg) + '点伤害')