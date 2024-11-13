
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            try:
                with open(i, 'r', encoding= 'utf-8') as file:
                    text = file.read().lower()
                    punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for j in punct:
                        text.replace(j, '')
                        words = text.split()
                        all_words[i] = words
            except FileNotFoundError:
                    print(f"Файл '{i} не найден")
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        word = word.lower()
        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word) + 1
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        word = word.lower()
        for name, words in all_words.items():
             result[name] = words.count(word)
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего