from scripts.fightingLogic import init
from scripts.skills import common

def main():
    # chara1 = init.input_name()
    red1 = init.status('baja')
    # chara2 = init.input_name()
    red2 = init.status('pwn')
    red3 = init.status('bin')
    blue1 = init.status('baozale')
    blue2 = init.status('chouzi')
    blue3 = init.status('niconi')
    red = init.position(red1, red2, red3, color='red')
    blue = init.position(blue1, blue2, blue3, color='blue')
    init.battle(red, blue)

if __name__ == "__main__":
    main()