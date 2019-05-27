
import argparse
from bin.Player import Player


def main(args):
    player = Player()
    player.adbscreen.get_screen_size()

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
