import random

words = ["dog","cat","bird","lizard","spider"]

while len(words) > 0:
    random_word = words[random.randrange(len(words))]
    print(random_word)
    words.remove(random_word)


