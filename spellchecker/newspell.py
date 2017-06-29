class spellchecker:
    def __init__(self):
        self.words = []

    def load_words(self, file_name):
        self.words = open(file_name).readlines()
        self.words = map(lambda x: x.strip(), self.words)

    def check_word(self, word):
        return word.strip('.').lower() in self.words

    def check_words(self, sentence):
        words_to_check = sentence.split(' ')
        for word in words_to_check:
            if not self.check_word(word):
                 print('Word is misspelt : ' + word)
                 return False
        return True

		
		
if __name__ == '__main__':
		
	spellcheck = spellchecker()
	spellcheck.load_words("spell.words")


	print (spellcheck.check_word("zygotic"))
	print (spellcheck.check_word("mistasdas"))
	print (spellcheck.check_word('zygotic mistasdas elementary'))