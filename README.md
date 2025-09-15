# NLTK Chatbot

A simple, extensible chatbot built with Python and the Natural Language Toolkit (NLTK). This project is great for learning the basics of NLP preprocessing and rule-based conversational flows, and it serves as a foundation you can extend with custom intents and responses.

## Features

- Basic NLP preprocessing (tokenization, normalization)
- Simple rule-based responses
- Easily extendable intents and patterns
- Runs locally from a single Python script

## Repository Structure

- `nltk_chatbot.py` — Main application script
- `README.md` — Project documentation (this file)

## Prerequisites

- Python 3.8+ (3.10+ recommended)
- pip (Python package installer)

## Setup

1) Clone the repository
```bash
git clone https://github.com/devpandey347/NLTK-Chatbot.git
cd NLTK-Chatbot
```

2) (Optional) Create and activate a virtual environment
```bash
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3) Install dependencies
```bash
pip install --upgrade pip
pip install nltk
```

4) Download common NLTK data
You can download within Python:
```python
import nltk
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("stopwords")
# If your script uses POS tagging:
nltk.download("averaged_perceptron_tagger")
```

…or via the downloader CLI:
```bash
python -m nltk.downloader punkt wordnet omw-1.4 stopwords averaged_perceptron_tagger
```

## Running the Chatbot

```bash
# Windows
python nltk_chatbot.py

# macOS/Linux
python3 nltk_chatbot.py
```

Depending on how the script is implemented, you’ll typically see a prompt in your terminal. Type a message and press Enter to chat.

## Customization

- Add or modify patterns/intents: Extend the rules or patterns in `nltk_chatbot.py` to recognize new intents and produce customized responses.
- Update preprocessing: Adjust tokenization, normalization (lowercasing, lemmatization), and stopword handling to better suit your domain.
- Add persistence or context: Track conversation state or user preferences if needed.

## Example (sample conversation)

```
You: hello
Bot: Hi there! How can I help you today?

You: what can you do?
Bot: I can respond to common greetings and basic questions. Try asking for help or say goodbye.

You: bye
Bot: Goodbye! Have a nice day.
```

Note: Your actual outputs may differ based on the rules implemented in `nltk_chatbot.py`.

## Troubleshooting

- Missing NLTK resources:
  - Error like “Resource punkt not found”: Run the NLTK downloader commands listed above.
- Multiple Python versions:
  - Ensure you’re installing packages and running the script with the same interpreter (`which python` / `where python`).
- Encoding issues on Windows:
  - Try running your terminal in UTF-8 or set `PYTHONIOENCODING=utf8`.

## Roadmap Ideas

- Replace/augment rules with a simple ML intent classifier
- Add a small intents dataset (JSON/YAML)
- Introduce context tracking and session memory
- Provide a minimal web or GUI interface (Streamlit/FastAPI)

## Contributing

Contributions are welcome!
- Fork the repo
- Create a feature branch
- Commit changes with clear messages
- Open a pull request describing your changes

## License

No license file is currently provided. If you plan to share or reuse this project, consider adding a LICENSE file (e.g., MIT, Apache-2.0).

## Acknowledgments

- [NLTK](https://www.nltk.org/) for powerful NLP tools and corpora
