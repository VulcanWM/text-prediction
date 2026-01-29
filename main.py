# training:
# - split text into 3 words (or 2 or 1)
# - remove all punctuation (except for '), just the words, keep the fancy letters ë and stuff
# - for each 3 words, and next 3 words, create a 2d dict in format {"3 words": {"next words 1": 5, "next words 2": 3}} (done this)

# text prediction:
# - when you input a word, it finds all tokens beginning with word, chooses starting one randomly
# - then calculates random num from 1 to sum(dict[token].values()) and uses this to calculate the next token and loops this until required word length is done

import random

# first let's create the markov chain itself
sentence = "as i walked across the park the morning air felt cool and gentle against my face and the sky stretched wide above me glowing with soft light that promised a calm day ahead and i listened to the quiet sounds of the world waking up leaves brushing together grass shifting under the breeze and distant laughter echoing from somewhere beyond the trees and it was then that i noticed a young bird walking near me not flying but stepping quickly with tiny determined movements as if it had decided that today was meant for exploring and every so often it looked up at me with bright curious eyes and i found myself matching its pace without even thinking because it felt wrong to rush past such a small fearless creature and for a moment it seemed like we were sharing the same path with an unspoken understanding that neither of us would disturb the peaceful rhythm of the morning and i wondered where it had come from and whether it had a nest nearby or if it was discovering the world for the first time guided only by instinct and courage and as we moved forward together the park appeared larger than usual each tree standing like a quiet guardian and each patch of sunlight forming warm shapes across the ground and i realised how rarely people slow down enough to notice these simple details and i promised myself that i would remember this feeling of patience long after the walk had ended but suddenly the calm shifted when i heard the fast steady pounding of paws against the earth and the sound grew stronger until it filled the space around us and when i turned i saw a dog racing toward us with incredible energy its brown coat shining and its unusual blue hair rippling as it ran while its red eyes caught the light in a way that made it seem almost unreal like something from a legend told to children on stormy nights and my first instinct was surprise rather than fear because there was something mysterious about the animal that did not feel entirely threatening yet could not be ignored and the little bird paused clearly unsure what to do and i stepped slightly ahead wanting to create a sense of safety even though i had no plan and the dog slowed as it approached circling with alert focus not aggressive but intense as if it were searching for answers only it understood and the air seemed warmer around us carrying a faint glow that shimmered each time the dog breathed out and in that strange moment i became aware of a trident resting in my hands its surface smooth and steady as though it had always belonged there and instead of questioning it i accepted it with quiet confidence feeling grounded rather than alarmed and the dog stopped a short distance away studying me and i studied it in return noticing that beneath its fierce appearance there was also curiosity and intelligence and i wondered if it too was trying to understand why our paths had crossed on such an ordinary morning that had suddenly become extraordinary and when it opened its mouth a swirl of warm light drifted outward not harsh or destructive but bright like the glow of a campfire on a cool evening and the colours reflected across the trident forming gentle patterns that danced in the air and i realised that this was not a moment for panic but for calm presence so i held the trident upright not as a weapon but as a signal that i would stand firm and the park seemed to hold its breath leaves stilled birds quiet and even the wind softened as though the world itself was watching to see what would happen next and for several long seconds nothing moved until the young bird stepped closer to me showing more bravery than i expected and the dog tilted its head the intensity fading just enough to reveal something softer and i spoke quietly though i was not sure whether the dog could understand words yet the tone felt important because sometimes calm travels farther than sound and the glow around the dog dimmed gradually like embers settling after a fire and its breathing slowed matching the peaceful rhythm that had filled the park earlier and i lowered the trident slightly sensing that the tension had begun to dissolve and the dog took one careful step forward then another no longer charging but simply approaching and there was a silent question in its eyes not a challenge but an invitation to trust and i realised that not every strange encounter must become a battle and that strength can mean choosing steadiness over fear and patience over reaction and after a moment the dog looked toward the small bird who now seemed less frightened and more fascinated than anything else and with a final soft breath the last traces of light faded into the morning air and the dog turned away trotting back across the grass with the same energy it had arrived with yet leaving behind only quiet rather than chaos and i watched until it disappeared between the trees feeling a mixture of relief wonder and gratitude for a moment that reminded me how unpredictable the world can be and how important it is to meet the unknown with courage and thoughtfulness rather than haste and when i glanced down the bird gave a quick flutter of its wings before continuing along its path as if nothing unusual had happened and i smiled returning the trident to my side though i could not say where it would go next and as i resumed my walk the park felt peaceful once more but also brighter somehow as though the morning had shared a secret meant only for those willing to notice and i carried that quiet sense of meaning with me step after step aware that even the most ordinary journeys can open into stories of surprise reflection and calm strength if we remain attentive to the world unfolding around us"
tokens = {}
words = sentence.split()
for i in range(0, len(words)-3, 3):
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

print(starting_tokens)
starting_token = random.choice(starting_tokens)
text = starting_token
print(text)
# for i in range(30):
#     # pick a token, then do
#     # text += " " + token
