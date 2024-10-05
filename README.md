
# FAQ Chatbot

This is a simple FAQ chatbot built using Python, SpaCy, and Streamlit. The chatbot helps users find answers to frequently asked questions (FAQs) by using natural language processing (NLP) to compare the user's question with predefined FAQs and return the most relevant answer.

## Features

- Uses SpaCy for natural language processing (NLP) to detect similarity between user input and predefined FAQ questions.
- Simple and interactive interface created with Streamlit for real-time question and answer interaction.
- Supports handling common FAQs related to business operations like return policies, order tracking, shipping, and payment methods.

## Requirements

Before you start, ensure you have the following installed:

- Python 3.x
- [SpaCy](https://spacy.io/)
- [Streamlit](https://streamlit.io/)
- SpaCy English model (`en_core_web_sm`)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/faq-chatbot.git
cd faq-chatbot
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Download the SpaCy English model:

```bash
python -m spacy download en_core_web_sm
```

## How to Run

To run the FAQ chatbot locally:

```bash
streamlit run app.py
```

Once Streamlit runs the app, it will open in your browser. Type your question in the provided text area, and click "ASK" to see the chatbot’s response.

## Project Structure

```
📂 faq-chatbot
 ├── 📄 app.py                # Main script to run the FAQ chatbot
 ├── 📄 README.md             # Project documentation
 ├── 📄 requirements.txt      # Python package dependencies
```

### `app.py`

The main application script that:

- Loads the SpaCy language model
- Defines a dictionary of FAQs
- Compares the user's input with the predefined FAQs using similarity scores
- Returns the best matching FAQ answer

### `requirements.txt`

List of Python libraries required to run the project:

```txt
spacy
streamlit
```

## Usage

1. Run the chatbot with the command:

```bash
streamlit run app.py
```

2. Type your question into the text area.
3. Click the **ASK** button, and the chatbot will respond with the most relevant FAQ answer.

## Example FAQs

Here are the questions the chatbot currently understands:

- What is your return policy?
- How do I track my order?
- Do you ship internationally?
- What payment methods do you accept?

## Future Improvements

- Add more FAQs to cover additional topics.
- Improve the similarity detection algorithm for better accuracy.
- Implement multi-lingual support.
- Add integration with a backend FAQ management system to dynamically update FAQs.
