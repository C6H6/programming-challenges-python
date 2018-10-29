from argparse import ArgumentParser


def get_parameters():
    parser = ArgumentParser(description='FizzBuzz')
    parser.add_argument('-n', '--number', help="Limit number", type=int)

    return parser.parse_args()


number = get_parameters().number

for i in range(1, number):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
        continue
    elif i % 3 == 0:
        print('Fizz')
        continue
    elif i % 5 == 0:
        print('Buzz')
        continue
    print(i)
