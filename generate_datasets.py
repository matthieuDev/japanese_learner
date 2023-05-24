import json

from japanese_learner.data.load_data import load_most_used_words_fr
from japanese_learner.command_prompt_learner.french_to_katana import french_to_katana

most_used_words_fr = load_most_used_words_fr()
f2k = french_to_katana()

to_save_most_used_words_fr = [
    {
        "model": "japanese2latin.QuestionJapanese2latin",
        "pk": i,
        "fields": {
            "latin_text": word,
            "japanese_text": f2k.fr2katakana(word)
        }
    }
    for i, word in enumerate(most_used_words_fr)
]

with open('japanese_learner_site/japanese2latin/data_init.json', 'w', encoding='utf8') as f :
    json.dump(to_save_most_used_words_fr, f, indent=2)