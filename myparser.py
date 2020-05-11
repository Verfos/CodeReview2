import argparse

parser = argparse.ArgumentParser(description='Testing App')
parser.add_argument('port', type=int, default = 5000)
parser.add_argument('host', type=str, nargs='?',default = 'localhost')
