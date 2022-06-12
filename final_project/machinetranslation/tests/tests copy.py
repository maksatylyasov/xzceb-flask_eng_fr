import unittest
from translator import englishToFrench,frenchToEnglish

#englishToFrench(None)

class TestMyModule(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        #self.assertIsNotNone(englishToFrench(None),"Test Value is None")

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

if __name__=='__main__':
    unittest.main()

    