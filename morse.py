from __future__ import print_function

ALL_WORDS = {
    'shell': '3.505',
    'halls': '3.515',
    'slick': '3.522',
    'trick': '3.532',
    'boxes': '3.535',
    'leaks': '3.542',
    'strobe': '3.545',
    'bistro': '3.552',
    'flick': '3.555',
    'bombs': '3.565',
    'break': '3.572',
    'brick': '3.575',
    'steak': '3.582',
    'sting': '3.592',
    'vector': '3.595',
    'beats': '3.600',
}

LETTERS = 'acbegfihkmlonsrtvx'
PAIRS = [a + b for a in LETTERS for b in LETTERS]
TRIPLES = [a + b + c for a in LETTERS for b in LETTERS for c in LETTERS]

def match(substring, words):
    matching = [word for word in words if substring in word + word]
    if len(matching) == 1:
        return matching[0]

def matches(substrings, words, ignore):
    result = []
    for substring in substrings:
        skip = False
        for sub in ignore:
            if sub in substring:
                skip = True
                break
        if skip:
            continue
        word = match(substring, words)
        if word:
            result.append((substring, word))
    return result

ignore = set()

uniques = []

def consider(substrings):
    for (substring, word) in matches(substrings, ALL_WORDS, ignore):
        uniques.append((substring, word))
        ignore.add(substring)

consider(LETTERS)
consider(PAIRS)
consider(TRIPLES)

for (substring, word) in sorted(uniques):
    print('{0} & {1} & {2} \\\\'.format(substring.upper(), word,
                                        ALL_WORDS[word]))
