import json
import string

def make_new_words(word):
    new_words = []
    for i, letter in enumerate(word):
        word_as_list = list(word)
        for c in string.ascii_lowercase:
            if c != letter:
                word_as_list[i] = c
                new_words.append("".join(word_as_list))
    return list(dict.fromkeys(new_words))

if __name__ == "__main__":
    with open('./words_dictionary.json') as f:
        data = json.load(f)

    while True:
        try:
            # user input
            spell = input("Enter spell: ")
            components = spell.lower().split(' ')
            for i, word in enumerate(components):
                new_words = make_new_words(word)
                for w in new_words:
                    if w in data:
                        alt_spell = components[:]
                        alt_spell[i] = w
                        print(" ".join(alt_spell))
        except KeyboardInterrupt:
            break
    
    print("\n=== Mischief Managed ===")
