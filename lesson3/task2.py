

def thesaurus(*args):
    dictionary = {}
    for name in args:
        first_letter = name[0]
        dictionary.setdefault(first_letter, [])
        dictionary[first_letter].append(name)
    return dictionary

print(thesaurus("Иван", "Мария", "Петр", "Илья"))

