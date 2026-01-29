import random

import re

word_pattern = re.compile(r"[^\W\d_]+(?:['’][^\W\d_]+)*", re.UNICODE)


def read_novel(novel_path):
    lines = []
    with open(novel_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if line == '----------':
                break

            if line:
                if not line.lower().startswith("chapter"):
                    # normalise apostrophes + lowercase
                    line = line.lower().replace("’", "'")
                    lines.append(line)

    return lines


def tokenize(lines):
    words = []

    for line in lines:
        words.extend(word_pattern.findall(line))

    return words


novel_lines = read_novel("jane-eyre.txt")
print("number of lines =", len(novel_lines))

cleaned_text = tokenize(novel_lines)

print("Number of words =", len(cleaned_text))
# print(cleaned_text)

tokens = {}
words = cleaned_text
for i in range(len(words) - 3):
    curr_token = " ".join(words[i:i+3])
    next_token = words[i+3]
    if curr_token in tokens:
        if next_token in list(tokens[curr_token].keys()):
            tokens[curr_token][next_token] += 1
        else:
            tokens[curr_token][next_token] = 1
    else:
        tokens[curr_token] = {next_token: 1}

print(tokens)

starting_token = 'mr rochester and'
text = starting_token
last_token = starting_token
print(text)
for i in range(500):
    if last_token not in tokens:
        break

    next_words = list(tokens[last_token].keys())
    weights = list(tokens[last_token].values())

    next_token = random.choices(next_words, weights=weights, k=1)[0]

    text += " " + next_token
    words_in_text = text.split()
    last_token = " ".join(words_in_text[-3:])
print(text)
