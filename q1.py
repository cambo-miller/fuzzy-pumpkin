from collections import Counter

class TxtReport():
    def __init__(self):
        self.unique_words = set()
        self.master_counts = Counter(sentences=0, words=0, unique_words=0)

    def txt_analysis(self, file_path):
        counts_dict = Counter(sentences=0, words=0, unique_words=0)
        with open(file_path) as txt_file:
            for line in txt_file:
                self.update_counts(line, counts_dict)
            self.master_counts += counts_dict
            counts_dict['unique_words'] = len(self.unique_words)
        return counts_dict

    def update_counts(self, line, counts_dict):

        def update_words(word):
            counts_dict['words'] += 1
            self.unique_words.add(word)
            return ''

        word = ''
        for char in line:
            if char == '.':
                counts_dict['sentences'] += 1
            elif char == ' ':
                word = update_words(word)
            else:
                word += char.lower()
        update_words(word)

    def __len__(self):
        return len(self.unique_words)
