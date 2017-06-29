import unittest
from newspell import spellchecker
class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        self.spellchecker = spellchecker()
        self.spellchecker.load_words('spell.words')

    def test_spell_checker(self):
		self.assertTrue(self.spellchecker.check_word('zygotic'))
		failed_words = self.spellchecker.check_words('zygotic mistasdas elementary')
		self.assertEquals(1, len(failed_words))
		self.assertEquals('mistasdas', failed_words[0])
		self.assertEquals(0, len(self.spellchecker.check_words('our first correct sentence')))
        # handle case sensitivity
		self.assertEquals(0, len(self.spellchecker.check_words('Our first correct sentence')))
        # handle full stop
		self.assertEquals(0, len(self.spellchecker.check_words('Our first correct sentence.')))
		failed_words = self.spellchecker.check_words('zygotic mistasdas spelllleeeing elementary')
		self.assertEquals(2, len(failed_words))
		self.assertEquals('mistasdas', failed_words[0])
		self.assertEquals('spelllleeeing', failed_words[1])
		self.assertEqual(0, len(self.spellchecker.check_document('spell.words')))

        #self.assertFalse(self.spellchecker.check_words('zygotic mistasdas elementary'))
        #self.assertTrue(self.spellchecker.check_words('our first correct sentence'))
		# handle case sensitivity 
        #self.assertTrue(self.spellchecker.check_words('Our first correct sentence'))
        # handle full stop
        #self.assertTrue(self.spellchecker.check_words('Our first correct sentence.'))
		#to fix the errors, the code on newspell was modified on line 10--returning word.strip('.').lower() in self.words instead of word in self.words  
        #self.assertFalse(self.spellchecker.check_words('zygotic mistasdas spelllleeeing elementary'))

if __name__ == '__main__':
    unittest.main()
