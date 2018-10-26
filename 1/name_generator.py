import random

first_name_syllables = ['mon', 'fay', 'shi', 'zag', 'blarg', 'rash', 'izen']
last_name_syllables = ['malo', 'zak', 'abo', 'wonk']


def get_name(name_set):
    name = ""
    syllables = random.randint(2, 3)
    for x in range(syllables):
        name += random.choice(name_set)
    return name.title()


first_name = get_name(first_name_syllables)
last_name = get_name(last_name_syllables)

print(first_name + " " + last_name)
