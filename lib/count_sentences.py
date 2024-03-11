#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("The 'value' property must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the string based on '.', '!', or '?' using regular expressions
        sentences = re.split(r'[.!?]', self.value)
        # Remove empty strings from the list
        sentences = [sentence for sentence in sentences if sentence]
        return len(sentences)

