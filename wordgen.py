import random


# A WordGenerator instance uses a Markov chain to generate novel pronounceable
# words. Initialize the generator by supplying a set of sample input words.
class WordGenerator:

    def __init__(self):
        self.table = {}
        self.start = []

    # Feed a sample input word into the generator for analysis.
    def add_word(self, word):
        size = len(word)
        if size < 3:
            return
        self.start.append((word[0], word[1]))

        for i in range(0, size - 2):
            c1, c2, c3 = word[i], word[i + 1], word[i + 2]
            self.table.setdefault((c1, c2), []).append(c3)

        c1, c2 = word[size - 2], word[size - 1]
        self.table.setdefault((c1, c2), []).append(None)

    # Generate a new output word.
    def get_word(self, max_len=12):
        c1, c2 = random.choice(self.start)
        word = [c1, c2]

        while len(word) < max_len:
            next_char = random.choice(self.table[(c1, c2)])
            if next_char is None:
                break
            word.append(next_char)
            c1, c2 = c2, next_char

        return ''.join(word)


# The size of a WordGenerator instance as implemented above is unbounded - it
# continues appending characters to its internal lists every time a word is
# added. The implementation below avoids this issue by storing character
# frequencies instead.
class ImprovedGenerator:

    def __init__(self):
        self.table = {}
        self.start = []

    # Increment the count of how many times c3 has followed the tuple (c1, c2).
    def _inc_count(self, c1, c2, c3):
        freq_map = self.table.setdefault((c1, c2), {})
        if c3 in freq_map:
            freq_map[c3] += 1
        else:
            freq_map[c3] = 1

    # Feed a sample input word into the generator for analysis.
    def add_word(self, word):
        size = len(word)
        if size < 3:
            return
        self.start.append((word[0], word[1]))

        for i in range(0, size - 2):
            c1, c2, c3 = word[i], word[i + 1], word[i + 2]
            self._inc_count(c1, c2, c3)

        c1, c2 = word[size - 2], word[size - 1]
        self._inc_count(c1, c2, ' ')

    # Generate a new output word.
    def get_word(self, max_len=12):
        c1, c2 = random.choice(self.start)
        word = [c1, c2]

        while len(word) < max_len:
            freq_map = self.table[(c1, c2)]
            population = [*freq_map.keys()]
            weights = [*freq_map.values()]
            next_char = random.choices(population, weights)[0]
            if next_char == ' ':
                break
            word.append(next_char)
            c1, c2 = c2, next_char

        return ''.join(word)
