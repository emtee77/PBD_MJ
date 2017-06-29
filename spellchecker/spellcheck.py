
words = open("spell.words").readlines()
words = map(lambda x: x.strip(), words)
#print words
print len(words)
print words[0]
print words[len(words)-1]

print ("zygotic" in words)
print ("mistasdas" in words)

# create a function to load the words and to check a word is in the dictionary
def load_words(file_name):
    words = open(file_name).readlines()
    words = map(lambda x: x.strip(), words)
    return words

#print load_words("spell.words")[0]


def check_word(words, word):
    return word in words


print load_words("spell.words")[0]
	
print check_word(words, "zygotic")
print check_word(words, "mistasdas")



def check_words(words, sentence):
    words_to_check = sentence.split(' ')
	failed_words = []
    for word in words_to_check:
        if not check_word(words, word):
            print('Word is misspelt : ' + word)
            #return False
			failed_words.append(word)
    #return True
	return failed_words
	
print check_words(words, "zygotic")
print check_words(words, "mistasdas")
print (check_words(words, 'zygotic mistasdas elementary'))
