import re

class CleanData:
    def __init__(self):
        pass
    @staticmethod
    def custom_split_tokenize(sentence):
                """Replace default tokenize
                """
                tokens = sentence.strip().split()
                for tk in tokens:
                    if re.search(r'[0-9]|[\+\-\+\(\)\{\}\<\>\°\/\\]',tk):
                        tokens.remove(tk)
                return tokens