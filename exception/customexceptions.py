class VowelNotAccepted(Exception):
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = message
        self.status = status

def cheack_chars(word):
    for char in word:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            raise VowelNotAccepted('Vowel is Not Accepted!', 1021)
    return word

try:
    print(cheack_chars('mnds'))
except Exception as e:
    print('Error Type: ', e.message)
