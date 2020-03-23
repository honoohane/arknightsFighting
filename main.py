from scripts.fightingLogic import init

def main():
    red1 = init.input_name()
    atk, spd, mag, inte, hp, defe = init.status(red1)


if __name__ == "__main__":
    main()