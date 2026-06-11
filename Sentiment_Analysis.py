import pandas as pd
import pyodbc
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon for sentiment analysis if not already present.
nltk.download('vader_lexicon')

# Setting up the database connection
def fetch_data_from_sql():
    conn_str = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=localhost;"
        "Database=PortfolioProject_MarketingAnalytics;"
        "Trusted_Connection=yes;"
    )
    
    conn = pyodbc.connect(conn_str)
    
    query = "SELECT ReviewID, CustomerID, ProductID, ReviewDate, Rating, ReviewText FROM customer_reviews"
    
    df = pd.read_sql(query, conn)
    
    conn.close()
    
    return df

customer_reviews_df = fetch_data_from_sql()

SIA = SentimentIntensityAnalyzer()

def calculate_sentiment(review):
    sentiment = SIA.polarity_scores(review)
    return sentiment['compound']

def categorize_sentiment(score, rating):
    if score > 0.05:  
        if rating >= 4:
            return 'Positive'  
        elif rating == 3:
            return 'Mixed Positive'  
        else:
            return 'Mixed Negative'  
    elif score < -0.05:  
        if rating <= 2:
            return 'Negative'  
        elif rating == 3:
            return 'Mixed Negative'  
        else:
            return 'Mixed Positive'  
    else:  
        if rating >= 4:
            return 'Positive'  
        elif rating <= 2:
            return 'Negative'  
        else:
            return 'Neutral'  
       
       
def sentiment_bucket(score):
    if score >= 0.5:
        return '0.5 to 1.0' 
    elif 0.0 <= score < 0.5:
        return '0.0 to 0.49'  
    elif -0.5 <= score < 0.0:
        return '-0.49 to 0.0'  
    else:
        return '-1.0 to -0.5'  
    
customer_reviews_df['SentimentScore'] = customer_reviews_df['ReviewText'].apply(calculate_sentiment)

customer_reviews_df['SentimentCategory'] = customer_reviews_df.apply(
    lambda row : categorize_sentiment(row['SentimentScore'], row['Rating']), axis=1)

customer_reviews_df['SentimentBucket'] = customer_reviews_df['SentimentScore'].apply(sentiment_bucket)

# print(customer_reviews_df.head())

customer_reviews_df.to_csv('customer_reviews_with_sentiment.csv', index=False)