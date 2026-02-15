# Advanced Mini Chatbot

A Python conversational agent with fuzzy string matching and dynamic response learning.

## Features

- **Fuzzy Matching**: Levenshtein distance-based intent recognition handling typos and variations
- **Dynamic Learning**: Real-time knowledge base expansion during conversations
- **Conversation Logging**: Persistent timestamped logs of all interactions
- **Modular Architecture**: Clean separation of logic, data, and logging layers

## Structure

├── chatbot.py          # Core conversation logic

├── responses.json      # Pattern-response knowledge base

├── logs/               # Conversation archives

└── requirements.txt    # Dependencies


## Quick Start

bash
git clone https://github.com/saharsistani137777-lab/advanced-mini-chatbot.git
cd advanced-mini-chatbot
pip install -r requirements.txt
python chatbot.py
`

Commands

Command Description
help Show available commands
add response Teach bot new patterns
quit Exit and save log

Dependencies

· fuzzywuzzy (string matching)
· python-Levenshtein (optional performance boost)

License

MIT
