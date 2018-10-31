import getpass


def list2str(list_to_display):
    return ''.join(list_to_display)


def check_letter(full_phrase, covert_phrase, input_letter):
    for i in range(0, len(full_phrase)):
        if full_phrase[i] == input_letter:
            covert_phrase[i] = input_letter

    return covert_phrase


tries = 10
win = False

phrase = getpass.getpass('Phrase: ')
masked_phrase = list("*" * len(phrase))
print("Phrase: " + list2str(masked_phrase))

while tries > 0:
    letter = input("Letter: ")[0]
    old = masked_phrase.copy()
    masked_phrase = check_letter(phrase, masked_phrase, letter)
    print(list2str(masked_phrase))
    if old == masked_phrase:
        tries -= 1

    print("Tries: " + str(tries))

    if phrase == list2str(masked_phrase):
        win = True
        break

if win:
    print("You won")
else:
    print("You lose")
