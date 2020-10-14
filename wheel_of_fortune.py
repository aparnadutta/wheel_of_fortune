from collections import Counter, defaultdict
from typing import List, DefaultDict

CATEGORIES = ["around_the_house.txt",
              "before_and_after.txt",
              "book_title.txt",
              "character.txt",
              "classic_tv.txt",
              "college_life.txt",
              "event.txt"]

VOWELS = set("AEIOU")


def count_chars(path: str):
    all_counts: Counter[str] = Counter()
    all_dists = defaultdict()
    category = path[:-4].replace("_", " ").title()
    num_entries = 0
    with open(path, encoding="utf8") as file:
        for line in file:
            num_entries += 1
            phrase = line.replace(" ", "").rstrip("\n")
            all_counts.update(phrase)
    for char, count in all_counts.most_common(10):
        all_dists[char] = round((count / sum(all_counts.values())*100), 2)
    vowel_dist = {vowel: dist for vowel, dist in all_dists.items() if vowel in VOWELS}
    cons_dist = {cons: dist for cons, dist in all_dists.items() if cons not in VOWELS}
    list_v = [v for v in vowel_dist.items()]
    list_c = [c for c in cons_dist.items()]
    return category, num_entries, list_v, list_c


def print_char_counts(paths: List[str]):
    all_paths = [count_chars(path) for path in paths]
    sorted_paths = sorted(all_paths, key=lambda tup: tup[1], reverse=True)
    for path in sorted_paths:
        print(f"Category: {path[0]} ({path[1]} data points)\nVowels:{path[2]}\nConsonants:{path[3]}\n")
    print()


print_char_counts(CATEGORIES)
