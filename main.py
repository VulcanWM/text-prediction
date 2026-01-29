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
for i in range(len(words) - 6):
    curr_token = " ".join(words[i:i+3])
    next_token = " ".join(words[i+3:i+6])
    if curr_token in list(tokens.keys()):
        if next_token in list(tokens[curr_token].keys()):
            tokens[curr_token][next_token] += 1
        else:
            tokens[curr_token][next_token] = 1
    else:
        tokens[curr_token] = {next_token: 1}

print(tokens)

starting_word = 'i'
starting_tokens = []
for token in list(tokens.keys()):
    if token.startswith(starting_word + " "):
        starting_tokens.append(token)

starting_token = random.choice(starting_tokens)
text = starting_token
last_token = starting_token
print(text)
for i in range(30):
    next_words = list(tokens[last_token].keys())
    weights = list(tokens[last_token].values())

    next_token = random.choices(next_words, weights=weights, k=1)[0]

    text += " " + next_token
    last_token = next_token
print(text)
