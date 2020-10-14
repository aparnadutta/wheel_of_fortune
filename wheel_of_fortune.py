import os
from collections import Counter
from typing import List, Tuple

# Gets all .txt files in the current directory and sorts them by file size.
CATEGORIES = [file for file in os.listdir(os.getcwd()) if file[-3:] == "txt"]
CATEGORIES.sort(key=lambda f: os.stat(f).st_size, reverse=True)

VOWELS = set("AEIOU")

# Computes the probability of each vowel and consonant in the category.
def count_chars(path: str) -> Tuple[str, int, List, List]:
    category = path[:-4].replace("_", " ").title()
    all_counts: Counter[str] = Counter()
    num_entries = 0
    with open(path, encoding="utf8") as file:
        for line in file:
            num_entries += 1
            all_counts.update("".join(line.split()))
    total = all_counts.most_common(10)
    v_list = [(v, prob(count, all_counts)) for v, count in total if v in VOWELS]
    c_list = [(c, prob(count, all_counts)) for c, count in total if c not in VOWELS]
    return category, num_entries, v_list, c_list

# Calculates the probability of one character.
def prob(n: int, total: Counter):
    return round(100*n / sum(total.values()), 2)

# Prints the result of count_chars.
def print_char_counts(paths: List[str]):
    all_paths = [count_chars(path) for path in paths]
    for path in all_paths:
        print(f"Category: {path[0]} ({path[1]} data points)")
        print(f"Vowels:\t\t{path[2]}\nConsonants:\t{path[3]}\n")
    print()


print_char_counts(CATEGORIES)
