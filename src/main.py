import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--bar', help='Do the bar option')
parser.add_argument('--foo', help='Foo the program')

args = parser.parse_args()

def run():
    print(args)

if __name__ == '__main__':
    run()
