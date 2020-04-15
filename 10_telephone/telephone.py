#!/usr/bin/env python3
"""
Author : None
Date   : 2020-04-15
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import string
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='input text or file')

    parser.add_argument('-m',
                        '--mutations',
                        help='Optional number of mutations',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Controls the randomness of the mutations',
                        metavar='int',
                        type=int,
                        default=0)



    args = parser.parse_args()

    parser.error(f'--mutations "{args.mutations}" must be between 0 and 1') if args.mutations < 0 or args.mutations > 1 else  ""
    parser.error(f'--seed "{args.seed}" must ') if args.seed < 0 else  ""


    args.text = open(args.text).read().strip() if os.path.isfile(args.text) else args.text

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    text = list(args.text)
    choices = string.ascii_letters + string.punctuation
    num_mutations = round(len(args.text) * args.mutations)
    indexes = random.sample(range(len(text)), num_mutations)

    for index in indexes:
        text[index] = random.choice(choices.replace(text[index], ''))

    print(f'You said: "{args.text}"')
    print(f'I heard : "{"".join(text)}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
