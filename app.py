import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re

class ProductPreprocessor:
    def __init__(self, filename):
        self.filename = filename
        self.df = pd.read_excel(self.filename)
        self._initialize_nltk_resources()
        
    @staticmethod
    def _initialize_nltk_resources():
        try:
            nltk.data.find('tokenizers/punkt')
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('punkt')
            nltk.download('stopwords')
    
    def clean_data(self, text):
        text = re.sub(r'<.*?>', '', text)
        text = re.sub(r'http\S+', '', text)
        text = text.replace('exmaple', 'example')  # Dummy typo correction, modify as needed
        return text

    def tokenize(self, text):
        return word_tokenize(text)

    def normalize(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text

    def remove_stopwords(self, tokens):
        stop_words = set(stopwords.words('english'))
        return [word for word in tokens if word not in stop_words]

    def stem(self, tokens):
        stemmer = PorterStemmer()
        return ' '.join([stemmer.stem(token) for token in tokens])

    def preprocess(self):
        self.df['Cleaned_Description'] = self.df['English Description (en-US)'].apply(self.clean_data)
        self.df['Normalized_Description'] = self.df['Cleaned_Description'].apply(self.normalize)
        self.df['Tokens'] = self.df['Normalized_Description'].apply(self.tokenize)
        self.df['Tokens_No_Stopwords'] = self.df['Tokens'].apply(self.remove_stopwords)
        self.df['Stemmed_Text'] = self.df['Tokens_No_Stopwords'].apply(self.stem)
        self.df = self.df[['Product ID', 'English Name (en-US)', 'Stemmed_Text', 'Tax Suggested Category']]
        return self.df

# Usage
preprocessor = ProductPreprocessor('path_to_your_file.xlsx')
processed_df = preprocessor.preprocess()
print(processed_df.head())
