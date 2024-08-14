import random
import nltk
import spacy
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

# Load the spacy model for English
nlp = spacy.load('en_core_web_sm')

# A small collection of possible responses
responses = [
    "Hello! How can I help you today?",
    "I'm doing great, thanks for asking! How about you?",
    "Can you tell me more about that?",
    "That's interesting! Tell me more.",
    "I see! How can I assist you further?"
]

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return set(synonyms)

def process_input(user_input):
    tokens = word_tokenize(user_input)
    pos_tags = nltk.pos_tag(tokens)
    
    response = ""
    
    # Analyze the input
    doc = nlp(user_input)
    for token in doc:
        print(f"Word: {token.text}, POS: {token.pos_}, Lemma: {token.lemma_}")

    # Generate a basic response (can be improved)
    if "hello" in tokens or "hi" in tokens:
        response = "Hi there! How can I assist you?"
    elif any(get_synonyms(word) & {"happy", "good", "great"} for word in tokens):
        response = "I'm glad to hear that!"
    else:
        response = random.choice(responses)
    
    return response

def chatbot():
    print("Hello! I'm a chatbot. Type 'exit' to stop the conversation.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = process_input(user_input)
        print(f"Chatbot: {response}")

if _name_ == "_main_":
    chatbot()