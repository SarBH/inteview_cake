import unittest

def reverse_chars(message):
    for idx in range(len(message) // 2):
        reverse_idx = len(message) - 1 - idx
        
        message[idx], message[reverse_idx] = message[reverse_idx], message[idx]
    pass


def reverse_words(message):

    # Decode the message by reversing the words
    reverse_chars(message)
    
    start_idx = 0
    try:
        end_idx = message[start_idx:].index(' ')
    except ValueError:
        end_idx =  -1

    # if theres at least more than one word:
    while end_idx != -1:
        for idx in range(len(message[start_idx:end_idx]) // 2):
            reverse_idx = len(message[start_idx:end_idx]) - 1 - idx
            message[start_idx + idx], message[start_idx + reverse_idx] = message[start_idx + reverse_idx], message[start_idx + idx]

        start_idx = end_idx + 1
        
        try:
            end_idx = message.index(' ', start_idx)
        except ValueError:
            end_idx = -1
    
    # this reverses the last word
    for idx in range(len(message[start_idx:]) // 2):
            reverse_idx = len(message[start_idx:]) - 1 - idx
            message[start_idx + idx], message[start_idx + reverse_idx] = message[start_idx + reverse_idx], message[start_idx + idx]

    pass







# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)