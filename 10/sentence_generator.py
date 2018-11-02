from argparse import ArgumentParser
import random


def get_parameters():
    parser = ArgumentParser(description='Random sentence generator')
    parser.add_argument('-n', '--number', type=int, default=1, help="Number of sentences")

    return parser.parse_args()


persons = ['I', 'You', 'He', 'She', 'It', 'We', 'They']
negations = ['don\'t', 'doesn\'t']
verbs = {
    'play': {
        'nouns': ['football', 'guitar', 'games'],
        'variations': ['play', 'plays']
    },
    'like': {
        'nouns': ['ice-cream', 'running', 'motorcycles'],
        'variations': ['like', 'likes']
    },
    'bake': {
        'nouns': ['cake', 'pie', 'cookies'],
        'variations': ['bake', 'bakes']
    },
    'read': {
        'nouns': ['book', 'newspaper', 'letter'],
        'variations': ['read', 'reads']
    },
}


def get_sentence():
    person = random.randint(0, 6)
    negation = random.randint(0, 1)
    third_person = person in [2, 3, 4]

    if negation or (not negation and not third_person):
        variation = 0
    else:
        variation = 1

    sentence = [persons[person]]
    verb = random.choice(list(verbs.keys()))

    if negation:
        if third_person:
            variation = not variation
        sentence.append(negations[variation])
        sentence.append(verbs[verb]['variations'][0])
    else:
        sentence.append(verbs[verb]['variations'][variation])

    sentence.append(random.choice(verbs[verb]['nouns']))

    return ' '.join(sentence)


number = get_parameters().number

for i in range(0, number):
    print(get_sentence())
