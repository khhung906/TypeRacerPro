from argparse import ArgumentParser
from Bot import Bot

def main(args):
    typePro = Bot(args.drive_path, args.speed)
    typePro.run()
    
def parse_args():
    parser = ArgumentParser()

    parser.add_argument(
        "--speed", 
        type=int, 
        default=60, 
        help = 'expeted speed for type racer'
    )

    parser.add_argument(
        "--drive_path", 
        default="./chromedriver", 
        help = 'expeted spped for type racer'
    )

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)
