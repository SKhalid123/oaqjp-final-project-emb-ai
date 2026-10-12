import unittest
from emotion_detection.emotion_detection import emotion_detector

class TestDominantEmotions(unittest.TestCase):
    def getemotion(self, text: str)->str:
        emotions = emotion_detector(text)
        return emotions.get('dominant_emotion')

    def test_joy(self):
        dominant_emotion = self.getemotion('I am glad this happened')
        self.assertEqual(dominant_emotion,'joy')
    
    def test_anger(self):
        dominant_emotion = self.getemotion('I am really mad about this')
        self.assertEqual(dominant_emotion,'anger')
    
    def test_disgust(self):
        dominant_emotion = self.getemotion('I feel disgusted just hearing about this')
        self.assertEqual(dominant_emotion,'disgust')
    
    def test_sadness(self):
        dominant_emotion = self.getemotion('I am so sad about this')
        self.assertEqual(dominant_emotion,'sadness')
    
    def test_fear(self):
        dominant_emotion = self.getemotion('I am really afraid that this will happen')
        self.assertEqual(dominant_emotion,'fear')

unittest.main()
    