from argparse import ArgumentParser


def get_parameters():
    parser = ArgumentParser(description='Encryption/decryption algorithm - ROT64 on ASCII table')
    parser.add_argument('-t', '--text', help="Text for encryption/decryption")

    return parser.parse_args()


def encrypt(text_to_encrypt):
    result = ""
    for char in text_to_encrypt:
        result += chr((ord(char) + 64) % 128)

    return result


text = get_parameters().text
print(encrypt(text))
