
class spellchecker:

	def load_words(self,file_name):
		words = open(file_name).readlines()
		words = map(lambda x: x.strip(), words)
		return words

#print load_words("spell.words")[0]


	def check_word(self,words, word):
		return word in words


#print load_words("spell.words")[0]
	
#print check_word(words, "zygotic")
#print check_word(words, "mistasdas")



	def check_words(self,words, sentence):
		words_to_check = sentence.split(' ')
		for word in words_to_check:
			if not self.check_word(words, word):
				print('Word is misspelt : ' + word)
				return False
		return True
	
spellcheck = spellchecker()
words = spellcheck.load_words("spell.words")

print words[0]	
print (spellcheck.check_words(words, "zygotic"))
print (spellcheck.check_words(words, "mistasdas"))
print (spellcheck.check_words(words, 'zygotic mistasdas elementary'))
