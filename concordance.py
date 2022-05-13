import sys

import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm", disable=['ner', 'parser', 'tagger'])
nlp.add_pipe('sentencizer')
doc = nlp(open(sys.argv[1]).read())

words_sentence = [(sent_id, token.text.lower()) for sent_id, sent in enumerate(doc.sents) for token in sent if ("\n" not in token.text and not token.is_punct)]
sentence_map = dict()
for t in words_sentence:
    si_list = str(sentence_map.get(t[1]) if t[1] in sentence_map else '')
    si_list = si_list + "," if si_list else si_list
    si_list = si_list + f'{t[0] + 1}'
    sentence_map.update({t[1]: si_list})

freq_map = Counter([w[1] for w in words_sentence])
sorted_keys = sorted(freq_map.keys())
letter_range = [*range(ord('a'), ord('z') + 1)]

for i in range(0, len(sorted_keys)):
    c = i if len(letter_range) > i else i % len(letter_range)
    times = int(i) / len(letter_range)
    times = 1 if times < 1 else 1 + int(round(times,0))
    letter_ordinal = ''
    for j in range(0,times):
        letter_ordinal = letter_ordinal + chr(letter_range[c])
    print(f'{letter_ordinal}.\t{sorted_keys[i]}\t{{{freq_map.get(sorted_keys[i])}:{sentence_map.get(sorted_keys[i])}}}')
