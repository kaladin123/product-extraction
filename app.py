import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re

# Load the Excel data
df = pd.read_excel('path_to_your_file.xlsx')

# Function for cleaning the data
def clean_data(text):
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    
    # Correct common typos or domain-specific ones (this is just a dummy example)
    text = text.replace('exmaple', 'example')
    
    return text

# Function for tokenization
def tokenize(text):
    return word_tokenize(text)

# Function for normalization
def normalize(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    return text

# Function for removing stopwords
def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word not in stop_words]

# Function for stemming
def stem(tokens):
    stemmer = PorterStemmer()
    return ' '.join([stemmer.stem(token) for token in tokens])

# Apply preprocessing
df['Cleaned_Description'] = df['English Description (en-US)'].apply(clean_data)
df['Normalized_Description'] = df['Cleaned_Description'].apply(normalize)
df['Tokens'] = df['Normalized_Description'].apply(tokenize)
df['Tokens_No_Stopwords'] = df['Tokens'].apply(remove_stopwords)
df['Stemmed_Text'] = df['Tokens_No_Stopwords'].apply(stem)

# Retain only the required columns
df = df[['Product ID', 'English Name (en-US)', 'Stemmed_Text', 'Tax Suggested Category']]

# Save or further process your preprocessed data
print(df.head())
