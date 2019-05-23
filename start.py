from bin.Player import Player
import argparse
#player = Player()
#player.start()

def main(args):
    player = Player()
    if args.init:
        print("Initialize the config")
        player.init()
        #player.adbscreen.get_screen()
    else:
        print("No Arguments passed")
        player.start()

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