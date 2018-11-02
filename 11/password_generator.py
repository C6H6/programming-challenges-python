import argparse
import random


def length_type(x):
    x = int(x)
    if x < 8:
        raise argparse.ArgumentTypeError("Minimum length is 8")
    return x


def get_parameters():
    parser = argparse.ArgumentParser(description='Password generator')
    parser.add_argument('-l', '--length', type=length_type, default=8, help="Password length (min. 8)")

    return parser.parse_args()


charsets = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "0123456789", "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"]

length = get_parameters().length
groups = [length // 4 + (1 if x < length % 4 else 0) for x in range(4)]

password = []

for i in range(0, 4):
    password += random.sample(charsets[i], groups[i])

random.shuffle(password)
print(''.join(password))
