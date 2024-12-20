# Sentiment Analysis Chatbot

This project is a **Sentiment Analysis Chatbot** built using Python with a user-friendly GUI interface created using Tkinter. The chatbot analyzes user input text to determine its sentiment (positive, negative, neutral, or anger) and provides motivational advice accordingly. It includes advanced features like spelling correction and lemmatization for text preprocessing.

## Features
1. **Sentiment Analysis**:
   - Uses NLTK's `SentimentIntensityAnalyzer` to classify sentiments.
   - Detects anger and sadness keywords for enhanced sentiment accuracy.

2. **Spelling Correction**:
   - Employs `SpellChecker` to correct typos in user input.

3. **Text Preprocessing**:
   - Utilizes spaCy for lemmatization and token processing.

4. **Motivational Advice**:
   - Provides tailored advice based on detected sentiment (positive, neutral, negative, or anger).

5. **Graphical User Interface (GUI)**:
   - Developed with Tkinter for intuitive interaction.
   - Includes a chat-like interface to display responses.

## Libraries Used
- **Tkinter**: For building the GUI interface.
- **NLTK**: For sentiment analysis and lexicon-based processing.
- **spaCy**: For advanced text preprocessing, including lemmatization.
- **SpellChecker**: For correcting spelling errors.
- **Emoji**: To display emojis in chatbot responses.

## Installation and Setup
1. Install the required Python libraries:
   ```bash
   pip install tkinter spacy nltk pyspellchecker emoji
   ```
2. Download the NLTK lexicon:
   ```bash
   import nltk
   nltk.download('vader_lexicon')
   ```
3. Download the spaCy model:
  ```bash
  python -m spacy download en_core_web_sm
  ```
## How It Works
1. Users type a message in the input box.
2. The chatbot preprocesses the input:
    * Corrects spelling errors.
    * Analyzes the sentiment using keywords and sentiment scores.
3. Based on the sentiment, the chatbot responds with:
    * Corrected text.
    * Identified sentiment and an emoji.
    * Relevant motivational advice.
4. The chat history is displayed in a listbox for easy review.
## How to Run
run the file sentimentAnalysis.py : 
```bash
   pthon sentimentAnalysis.py
```
## Example Usage
* Input: I fel sp sad today.
* Output:
* Corrected Text: I feel so sad today.
* Sentiment: Sad 😞
* Advice: "It's okay to feel down, but remember that challenges are temporary. You are stronger than you think, and things will improve soon!"


