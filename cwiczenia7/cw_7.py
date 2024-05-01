#!/usr/bin/env python
# coding: utf-8

# In[15]:


from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer

def get_wikipedia_article_text():
    # Endpoint URL for the MediaWiki API
    endpoint = "https://en.wikipedia.org/w/api.php"

    article_params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": "Web_scraping", #Here come the title you want to get
        "explaintext": True  # Return plain text instead of HTML
    }
    article_response = requests.get(endpoint, params=article_params)
    if article_response.status_code == 200:
        article_data = article_response.json()
        # Extract the text of the article
        article_text = next(iter(article_data["query"]["pages"].values()))["extract"]
        return article_text
    else:
        print("Failed to fetch article text")

def create_summary(article_text):    
    string = ""
    parser = PlaintextParser.from_string(article_text, Tokenizer("english"))
    summarizer = Summarizer()
    summary = summarizer(parser.document, sentences_count=5)
    for sentence in summary:
        string +=str(sentence)
    return string

article_text = get_wikipedia_article_text()
summary = create_summary(article_text)
    
    
with open("org.txt", "w", encoding="utf-8") as file:
    file.write(article_text)
    
with open("outcome.txt", "w", encoding="utf-8") as file:
    file.write(summary)


