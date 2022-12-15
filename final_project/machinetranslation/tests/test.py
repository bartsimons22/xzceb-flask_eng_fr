import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        test_value = 'Hello'
        error_message = 'Test value is none'
        self.assertIsNotNone(test_value, error_message)
        self.assertEqual(english_to_french(test_value)['translations'][0]['translation'], 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self):
        test_value = 'Bonjour'
        error_message = 'Test value is none'
        self.assertIsNotNone(test_value, error_message)
        self.assertEqual(french_to_english(test_value)['translations'][0]['translation'], 'Hello')
        
unittest.main()