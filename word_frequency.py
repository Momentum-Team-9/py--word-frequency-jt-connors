STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    file = open(file)
    text = file.read()
    for word in text:
        text = text.lower()
    text = text.replace("\n", " ")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("?", "")
    text = text.replace("'", "")
    text = text.replace('"', "")
    text = text.replace('”', "")
    text = text.replace('“', "")
    text = text.replace("-", " ")
    text = text.replace(":", "")
    text = text.split(" ")
    for word in text:
        if word in STOP_WORDS:
            text.remove(word)
    print(text) 
    print(file)
    file.close()


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
