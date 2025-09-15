import nltk
import random
import sys
import datetime
import wikipedia
from nltk.corpus import wordnet 
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

#Download required data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')

#---
#Utilities 
#----
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    """Lowercase, tokenize, remove punctuation tokens, and lemmatize."""
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if any(c.isalnum() for c in t)]  # drop pure punctuation
    lemmas = [lemmatizer.lemmatize(t) for t in tokens]
    return lemmas

def synonyms_for(word):
    """Return a set of synonyms for the given word using WordNet."""
    syns = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            syns.add(lemma.name().lower().replace("_", " "))
    return syns

#Precompute synonyms sets for common intent words
INTENT_KEYWORDS = {
    "ai": {"ai", "artificial intelligence", "artificial", "intelligence", "machine learning", "ml"},
    "python": {"python", "py"},
    "time": {"time", "clock"},
    "date": {"date", "day", "today"},
    "greeting": {"hi", "hello", "hey", "hii", "yo"},
    "goodbye": {"bye", "goodbye", "quit", "exit"},
    "sad": {"sad", "unhappy", "depressed", "down", "bored"},
    "happy": {"happy", "good", "great", "fine", "awesome"},
    "joke": {"joke", "funny", "laugh"},
}

#Expand with synonyms
for key in ("ai", "python", "time", "date", "sad", "happy", "joke"):
    expanded = set()
    for base in list(INTENT_KEYWORDS[key]):
        expanded |= synonyms_for(base)
    INTENT_KEYWORDS[key] |= expanded

#A small jokes list
JOKES = [
    "Why don't scientists trust atoms? Because they make up everything! 😂",
    "I told my computer I needed a break, and it said: 'No problem, I'll go to sleep!' 😴",
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
]

#----
# Dynamic response functions
#------
def get_time():
    return datetime.datetime.now().strftime("The current time is %H:%M:%S. ⏰")

def get_date():
    return datetime.datetime.now().strftime("Today's date is %B %d, %Y. 📅")

def wiki_search(query):
    """Search wikipedia and return a short summary or an apology message."""
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.DisambiguationError as e:
        try:
            choice = e.options[0]
            return f"I found multiple results for '{query}'. Here's a summary for '{choice}':\n\n" + wikipedia.summary(choice, sentences=2)
        except Exception:
            return "I found many possible results — can you be more specific?"
    except wikipedia.PageError:
        return "Sorry, I couldn't find information on that."
    except Exception:
        return "Sorry, something went wrong while looking that up."

#---
# Core intelligent responder
#---
def intent_match(tokens, intent_key):
    """Return True if any token or its synonyms match the intent keywords."""
    keyword_set = INTENT_KEYWORDS.get(intent_key, set())
    for t in tokens:
        if t in keyword_set:
            return True
        syns = synonyms_for(t)
        if syns & keyword_set:
            return True
    return False

def chatbot_response(user_input):
    tokens = preprocess(user_input)

    if not tokens:
        return "Say something, bro — I'm listening 😄"

    #Exit
    if intent_match(tokens, "goodbye") or any(t in ("bye", "quit", "exit") for t in tokens):
        return random.choice(["Bye! It was nice chatting with you. 👋", "Goodbye! Come back soon 😄"])

    #Greeting
    if intent_match(tokens, "greeting"):
        return random.choice(["Hello! How can I help you today?", "Hey there! What do you want to build today?", "Hi 👋 — ready to hack?"])

    #Time & Date
    if intent_match(tokens, "time") or "time" in tokens:
        return get_time()
    if intent_match(tokens, "date") or any(t in ("date", "day", "today") for t in tokens):
        return get_date()

    #Jokes
    if intent_match(tokens, "joke") or any(t in ("joke", "funny", "laugh") for t in tokens):
        return random.choice(JOKES)

    #Tech questions
    if intent_match(tokens, "ai") or any(t in ("ai", "artificial", "intelligence", "machine", "learning", "ml") for t in tokens):
        return ("AI (Artificial Intelligence) is about building systems that can perform tasks requiring human-like intelligence.\n"
                "Examples: classification, prediction, natural language processing. Want a short example or links?")
    if intent_match(tokens, "python") or "python" in tokens:
        return ("Python is a high-level language used in web dev, data science, and AI/ML. It's great for rapid prototyping. "
                "Want a sample snippet for something specific?")  

    #Feelings
    if intent_match(tokens, "sad"):
        return random.choice([
            "Don't worry bro, take a short break and play some music 🎧",
            "If you're feeling down, talk to someone you trust or take a walk 🌿",
        ])
    if intent_match(tokens, "happy"):
        return random.choice(["That's awesome! Keep the energy up 🔥", "Nice! Keep going 😎"])

    #Explicit Wikipedia queries
    if "tell me about" in user_input.lower() or "Who is" in user_input.lower():
        query = user_input.lower().replace("tell me about", "").replace("who is", "").strip()
        return wiki_search(query)

    #General unknown queries → Wikipedia
    if "?" in user_input or len(user_input.split()) > 1:
        return wiki_search(user_input)

    # Final fallback
    return "I didn't catch that exactly. Ask me about AI, Python, time, or try a general question."

#-------------
# Main loop
#-------------
def main():
    print("🤖 NLTK-Bot (Console) — type 'quit' or 'bye' to exit.")
    print("Pro tip: Ask about 'AI', 'Python', or ask a general question and I'll try Wikipedia.")
    try:
        while True:
            user_input = input("\nYou: ").strip()
            if not user_input:
                print("🤖 NLTK-Bot: Say something, bro.")
                continue
            response = chatbot_response(user_input)
            print("\n🤖 NLTK-Bot:", response)
            if any(k in user_input.lower() for k in ("bye", "quit", "exit")):
                break
    except KeyboardInterrupt:
        print("\n\n🤖 NLTK-Bot: Bye — good luck at the hackathon!")
        sys.exit(0)

if __name__ == "__main__":
    main()
