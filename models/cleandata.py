import re

class CleanData:
    def __init__(self):
        pass
    @staticmethod
    def custom_split_tokenize(sentence):
                """Replace default tokenize
                """
                tokens = sentence.strip().split()
                i=0
                while i < len(tokens):
                    tk= tokens[i]
                    if re.search(r'[0-9]|[\-\+\*\(\)\{\}\<\>\°\/\\\=\@\#\$\%\^\&\_\[\]\~\`]',tk):
                        tokens.remove(tk)
                        i-=1
                    i+=1
                return tokens