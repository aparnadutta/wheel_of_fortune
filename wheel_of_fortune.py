from collections import Counter, defaultdict
from typing import List, DefaultDict

categories = ["around_the_house.txt",
              "before_and_after.txt",
              "book_title.txt",
              "character.txt",
              "classic_tv.txt",
              "college_life.txt",
              "event.txt"]


def count_chars(path: str):
    counts: Counter[str] = Counter()
    dists: DefaultDict = defaultdict()
    category = path[:-4].replace("_", " ").title()
    num_entries = 0
    with open(path, encoding="utf8") as file:
        for line in file:
            num_entries += 1
            phrase = line.replace(" ", "").rstrip("\n")
            counts.update(phrase)
    for char, count in counts.most_common(10):
        dists[char] = round(count / sum(counts.values()), 2)
    all_letters = [dist for dist in dists.items()]
    return category, num_entries, all_letters


def print_char_counts(paths: List[str]):
    all_paths = [count_chars(path) for path in paths]
    sorted_paths = sorted(all_paths, key=lambda tup: tup[1], reverse=True)
    for path in sorted_paths:
        print(f"Category: {path[0]} ({path[1]} data points)\n{path[2]}\n")
    print()


print_char_counts(categories)
