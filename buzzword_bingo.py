#
# Copyright 2019 Andrew Lin. All rights reserved.
#
# This software is released under the BSD 3-clause license. See LICENSE.txt or
# https://opensource.org/licenses/BSD-3-Clause for more information.
#
import argparse
import os

from server import bingo_server


def parse_command_line() -> argparse.Namespace:
    """Get command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('buzzwords', help='path to buzzword file.')
    parser.add_argument(
        '-p', '--port',
        type=int,
        default=5000,
        help='network port number'
    )

    args = parser.parse_args()
    args.buzzwords = os.path.abspath(os.path.expanduser(args.buzzwords))
    return args


def main() -> None:
    """Launch application."""
    args = parse_command_line()
    bingo_server.app.set_buzzwords(args.buzzwords)
    bingo_server.app.run(debug=False, host='0.0.0.0', port=args.port)


if __name__ == '__main__':
    main()
