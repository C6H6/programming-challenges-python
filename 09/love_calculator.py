from argparse import ArgumentParser


def get_parameters():
    parser = ArgumentParser(description='Love calculator')
    parser.add_argument('-n1', '--name1', help="Name 1")
    parser.add_argument('-n2', '--name2', help="name 2")

    return parser.parse_args()


names = get_parameters()
merged = sorted(names.name1.lower() + names.name2.lower())

letters_sum = 0
for letter in merged:
    letters_sum += ord(letter)

score = letters_sum % 101
print("Score: " + str(score) + "%")
