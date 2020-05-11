from views import *
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Testing App')
    parser.add_argument('port', type=int, nargs='?', default = 5000)
    parser.add_argument('host', type=str, nargs='?',default = 'localhost')
    arg = parser.parse_args()
    app.run(debug=False, host=arg.host, port = arg.port)
