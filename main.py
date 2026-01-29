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

def create_model(cleaned_text, n_grams=3):
    model = {}
    words = cleaned_text
    for i in range(len(words) - n_grams):
        curr_token = " ".join(words[i:i+n_grams])
        next_token = words[i+n_grams]
        if curr_token in model:
            if next_token in list(model[curr_token].keys()):
                model[curr_token][next_token] += 1
            else:
                model[curr_token][next_token] = 1
        else:
            model[curr_token] = {next_token: 1}
    return model


def predict_text(model, starting_token, n_grams=3):
    text = starting_token
    last_token = starting_token
    for i in range(500):
        if last_token not in model:
            break

        next_words = list(model[last_token].keys())
        weights = list(model[last_token].values())

        next_token = random.choices(next_words, weights=weights, k=1)[0]

        text += " " + next_token
        words_in_text = text.split()
        last_token = " ".join(words_in_text[n_grams * -1:])
    return text

novel_lines = read_novel("jane-eyre.txt")
print("number of lines =", len(novel_lines))

cleaned_text = tokenize(novel_lines)

print("Number of words =", len(cleaned_text))

model = create_model(cleaned_text, 3)

starting_token = 'mr rochester and'
text = predict_text(model, starting_token, 3)
print(text)
