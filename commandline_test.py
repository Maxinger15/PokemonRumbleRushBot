
import argparse
from bin.Player import Player


def main(args):
    player = Player()
    if args.init:
        #player.init()
        player.adbscreen.get_screen()
    else:
        print("no")

        #player.start()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        '--init',
        help="Creates a empty screen Template for your device",
        action="store_true"
    )
    args = parser.parse_args()
    main(args)
