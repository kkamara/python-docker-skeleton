import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bar', help='Do the bar option')
    parser.add_argument('--foo', help='Foo the program')
    return parser.parse_args()

def run():
    args = parse_args()
    print(args)

if __name__ == '__main__':
    run()
