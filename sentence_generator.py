from collections import defaultdict
import os
import random

max_number_of_iterations = 100000


class SentenceGenerator:
    def __init__(self):
        self.transitions = defaultdict(list)
        self.starts = []

    def fit(self, tokens):
        trigrams = zip(tokens, tokens[1:], tokens[2:])
        for prev, current, next in trigrams:
            if prev == '.':
                self.starts.append(current)
            self.transitions[(prev, current)].append(next)

    def generate_any_sentence(self, number_to_skip=0):
        current = random.choice(self.starts)
        prev = "."
        result = [current]
        if number_to_skip > 0:
            result.pop()
            number_to_skip -= 1

        while True:
            next_word_candidates = self.transitions[(prev, current)]
            next_word = random.choice(next_word_candidates)
            prev, current = current, next_word
            if current == '.':
                return ' '.join(result) + '.'
            if number_to_skip > 0:
                number_to_skip -= 1
            else:
                result.append(current)

    def bad_sentence_generated(self, prefix_length, sentence, length):
        return prefix_length + len(sentence.split()) > length or prefix_length + len(
            sentence.split()) <= 1 or prefix_length + len(sentence.split()) == length - 1

    def generate(self, prefix, length):
        answer = prefix
        prefix_length = len(prefix.split())
        sentence = self.generate_any_sentence(prefix_length)
        while len(sentence.split()) < prefix_length < 4 or self.bad_sentence_generated(prefix_length, sentence, length):
            sentence = self.generate_any_sentence(prefix_length)
        answer += (' ' if len(answer) > 0 and sentence != '.' else '') + sentence
        length -= len(answer.split())

        iterations = 0
        while length > 0:
            if iterations > max_number_of_iterations:
                return answer + '.'
            sentence = self.generate_any_sentence()
            if not self.bad_sentence_generated(0, sentence, length):
                answer += ' ' + sentence
                length -= len(sentence.split())
            iterations += 1

        return answer


def is_valid_file(parser, arg, mode):
    if not os.path.exists(arg):
        parser.error('The file %s does not exist!' % arg)
    else:
        return open(arg, mode)  # return an open file handle
