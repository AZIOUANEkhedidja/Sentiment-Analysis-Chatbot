import tkinter as tk
from tkinter import messagebox
import spacy
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import emoji
import random
from spellchecker import SpellChecker
import os

# Download NLTK data
nltk.download('vader_lexicon')

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# SpellChecker setup
spell = SpellChecker()

# Function to correct text using SpellChecker and spaCy
def correct_text_with_spellchecker(text):
    # Correct spelling using SpellChecker
    words = text.split()
    corrected_words = [spell.correction(word) for word in words]
    corrected_text = " ".join(corrected_words)
    
    # Use spaCy for further processing
    doc = nlp(corrected_text)
    
    return " ".join([token.lemma_ if not token.is_stop and not token.is_punct else token.text for token in doc])

# Motivational advice lists for different sentiments
positive_advice_list = [
    "I'm so glad you're feeling good! Keep spreading that positivity and happiness!",
    "Great things are ahead of you, keep going!",
    "You're doing amazing, keep up the great work!",
    "Stay positive, great things are coming your way!",
    "Your energy is contagious, keep shining!",
    "You're on the right track, keep it up!",
    "Positivity is your superpower, use it wisely!",
    "You are unstoppable! Keep going!",
    "Your future is bright, stay positive!",
    "Keep believing in yourself, you’ve got this!"
]

negative_advice_list = [
    "It's okay to feel down, but remember that challenges are temporary. You are stronger than you think, and things will improve soon!",
    "Every setback is a setup for a comeback. You'll get through this!",
    "Tough times don't last, but tough people do. You are stronger than you know!",
    "It's okay to not be okay. Take your time, and things will get better!",
    "You are not alone in this. Keep pushing, things will improve!",
    "Difficult roads often lead to beautiful destinations. Keep going!",
    "You're resilient and capable of overcoming anything that comes your way!",
    "It’s okay to feel down, but don’t stay there. Better days are ahead!",
    "Keep moving forward, even if it’s one small step at a time.",
    "You are stronger than any challenge you face, and you will rise above it!"
]

neutral_advice_list = [
    "You're doing well! Sometimes it's okay to feel neutral, but always move forward with a positive mindset.",
    "Keep going at your own pace, things will get better over time.",
    "You're on the right track, just keep going!",
    "Sometimes it's okay to take a break and just be. You're doing fine!",
    "Life has its ups and downs, but you're handling it all beautifully.",
    "Stay calm and keep moving forward, you're doing great!",
    "Even when things feel neutral, you're still making progress.",
    "Remember, even the smallest steps forward are still steps in the right direction.",
    "Sometimes, just breathing and being present is enough. You're doing well!",
    "Keep your head up, things will shift for the better!"
]

anger_advice_list = [
    "It's okay to feel angry, but don’t let it control you. Take a deep breath, and let it go.",
    "Anger is a natural emotion, but it doesn't define you. Release it and move forward.",
    "Sometimes the best way to deal with anger is to step back and take a moment for yourself.",
    "You have the power to calm your mind. Take a pause and regain your inner peace.",
    "Anger doesn’t solve anything, but your calmness will help you think clearer and move ahead.",
    "Channel that energy into something productive. You are stronger than your emotions.",
    "Anger is temporary, but your strength and peace are lasting.",
    "Don't let anger take away your peace. Let it pass, and move on stronger.",
    "It's okay to express your anger, but don’t let it control your actions. Find your calm.",
    "Take a deep breath, let the anger fade, and remember: peace is within you."
]

# Function to analyze sentiment and return motivational advice
def analyze_sentiment_and_advice(text):
    corrected_text = correct_text_with_spellchecker(text)
    
    # Check for specific words related to anger or sadness
    anger_keywords = ["angry", "rage", "furious", "irritated", "enraged", "mad", "upset", "agitated", "annoyed", "outraged", "infuriated", "fuming", "livid", "seething", "exasperated", "raging", "frustrated", "boiling", "indignant", "vexed"]


    sad_keywords = ["sad", "down", "disappointed", "blue", "depressed"]
    
    # If keywords for anger or sadness are found, override the sentiment analysis
    if any(keyword in text.lower() for keyword in anger_keywords):
        sentiment = "anger"
        emoji_icon = emoji.emojize(":rage:")
        advice = random.choice(anger_advice_list)
    elif any(keyword in text.lower() for keyword in sad_keywords):
        sentiment = "sad"
        emoji_icon = emoji.emojize(":disappointed:")
        advice = random.choice(negative_advice_list)  # Sadness is treated as negative
    else:
        # Use SentimentIntensityAnalyzer for other cases
        sia = SentimentIntensityAnalyzer()
        sentiment_score = sia.polarity_scores(corrected_text)
        
        if sentiment_score['compound'] >= 0.05:
            sentiment = "positive"
            emoji_icon = "😊"
            advice = random.choice(positive_advice_list)
        elif sentiment_score['compound'] <= -0.05 and sentiment_score['compound'] > -0.75:
            sentiment = "negative"
            emoji_icon = "😞"
            advice = random.choice(negative_advice_list)
        elif sentiment_score['compound'] <= -0.75:
            sentiment = "anger"
            emoji_icon = "🤯"
            advice = random.choice(anger_advice_list)
        else:
            sentiment = "neutral"
            emoji_icon = emoji.emojize(":neutral_face:")
            advice = random.choice(neutral_advice_list)
    
    return corrected_text, sentiment, emoji_icon, advice

# Function to respond to user input
def respond_to_user():
    user_input = user_input_box.get("1.0", "end-1c")
    
    if user_input.strip() == "":
        messagebox.showwarning("Input Error", "Please enter some text to analyze!")
        return
    
    corrected_text, sentiment, emoji_icon, advice = analyze_sentiment_and_advice(user_input)
    
    # response_text = f"Corrected Text: {corrected_text}\n\n Sentiment: {sentiment} {emoji_icon}\n\n "
    
    # Insert user and bot messages into Listbox
    
    chat_listbox.insert(0, f"Bot: Corrected Text: {corrected_text}")
    chat_listbox.insert(0, f"Bot: Sentiment: {sentiment} {emoji_icon}")
    chat_listbox.insert(0, f"Bot: Advice: {advice}")
    chat_listbox.insert(0, f"You: {user_input}")  
    chat_listbox.insert(0, f"******************msg****************")  
    
    # Clear input box after sending text
    user_input_box.delete("1.0", "end")

# GUI setup
window = tk.Tk()
window.title("Sentiment Analysis Chatbot")
window.geometry("800x550")

# Listbox to display messages with a scrollbar
chat_listbox = tk.Listbox(window, width=120, height=23, selectmode="single")
chat_listbox.pack(pady=10)

# Scrollbar setup for Listbox
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side="right", fill="y")
chat_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=chat_listbox.yview)

# Text box for user input
user_input_box = tk.Text(window, height=4, width=50, wrap="word")
user_input_box.pack(pady=10)

# Button to analyze sentiment
send_button = tk.Button(window, text="Analyze Sentiment", command=respond_to_user)
send_button.pack(pady=10)

# Run the GUI
window.mainloop()
