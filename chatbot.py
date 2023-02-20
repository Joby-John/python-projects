import nltk

import random
from nltk.chat.util import Chat, reflections

# Define the conversation pairs
pairs = [
    ['my name is (.*)', ['Hi %1']],
    ['hi|hello', ['Hi there', 'Hello', 'I am glad to talk to you']],
    ['what is your name?', ['My name is Bot', 'I am a Bot created by OpenAI']],
    ['bye', ['Bye', 'Goodbye', 'It was nice talking to you']],
]

# Define the chatbot
class SimpleChatBot(Chat):
    def __init__(self, pairs, reflections={}):
        super().__init__(pairs, reflections)
        self._nltk_sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    def respond(self, str):
        # Tokenize input message
        sent_tokens = self._nltk_sent_tokenizer.tokenize(str)

        # Get response for each input sentence
        response = []
        for sentence in sent_tokens:
            response += super().respond(sentence)
        
        # Return concatenated responses
        return ' '.join(response)

# Run the chatbot
if __name__ == "__main__":
    bot = SimpleChatBot(pairs, reflections)
    bot.converse()
