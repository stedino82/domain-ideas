import itertools


def compose(combos, tlds):
    for words in combos:
        for tld in tlds:
            if len(words) > 1:
                yield f"{'-'.join(words)}.{tld}"
            yield f"{''.join(words)}.{tld}"


def domain_ideas(keywords, tlds):
    for combo in [c.strip() for c in keywords.splitlines()]:
        words = [w.strip() for w in combo.split(' ')]
        for n in range(1, len(words) + 1):
            yield from compose(itertools.permutations(words, n), tlds)


if __name__ == "__main__":
    my_tlds = "it,org,net".split(',')
    my_keywords = '''extra moenia pisa
    pisa fuori le mura'''

    for w in domain_ideas(my_keywords, my_tlds):
        print(w)
