import requests
import api
import data
#import main
from main import speak

base_url = 'https://newsapi.org/v2/top-headlines'

# Specify the parameters for your news query
params = {
    'apiKey': api.newsapikey,
    'country': 'in',  # Change the country code as needed
}

try:
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        news_data = response.json()

        articles = news_data['articles']

        for idx, article in enumerate(articles, start=1):
            if(idx<=data.current_affair_limit):
                print(f"Article {idx}:")
                speak(f"Article {idx}:")
                print(f"Title: {article['title']}")
                speak(f"{article['title']}")
                print(f"Source: {article['source']['name']}")
                speak(f"Source: {article['source']['name']}")
                print(f"Description: {article['description']}")
                print(f"URL: {article['url']}")
                print("\n")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        speak("I can not response you at this moment")

except Exception as e:
    print(f"An error occurred: {str(e)}")
    speak("I can not response you at this moment")
