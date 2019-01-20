import string
import re

class Nana:
    def __init__(self):
        # Файлаас зогсох үг буюу туслах үгнүүдийг унших
        with open('./dict/stopwords.txt', 'r') as f:
            self.stopwords = f.read().split('\n')
        # Файлаас залгаваруудыг унших
        with open('./dict/rules.txt', 'r') as f:
            self.rules = f.read().split('\n')
        # Залгавар үгнүүдийн REGEX үүсгэх 
        self.rulesREGEXP = '$|'.join(self.rules)+'$'

    def parse(self, text):
        text_sentences = text.split('.')
        sentences = []
        for text_sentence in text_sentences:
            # өгүүлбэрийн текстийг үгүүд болгож хувиргах
            tokens = text_sentence.split(' ')
            # том үсгүүдийг болиулах
            tokens = [w.lower() for w in tokens]
            # үг бүрээс тэмдэгтүүдийг хасах
            table = str.maketrans('', '', string.punctuation)
            stripped = [w.translate(table) for w in tokens]
            # текст бус үгүүдийг хасах
            words = [word for word in tokens if word.isalpha()]
            # stopword уудыг хасах
            words = [w for w in words if not w in self.stopwords]
            # stemming
            words = [re.sub(self.rulesREGEXP, '', w) for w in words if len(w) >= 6]
            sentences.append(words)
        return sentences


        

        


