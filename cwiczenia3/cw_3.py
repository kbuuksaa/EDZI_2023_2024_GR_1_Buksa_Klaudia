#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import json


def imdb_top_100():
    url = "https://m.imdb.com/chart/top/?ref_=nv_mv_250"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3', 'Accept-Language': 'en-US,en;q=0.9'}
    response = requests.get(url, headers = headers)
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(url))

    doc = BeautifulSoup(response.text, 'html.parser')
    movies_dict = {
        'Title': get_movies(doc),
        'Rating': get_ratings(doc)
    }
    return pd.DataFrame(movies_dict)

def get_movies(im):
    movies_names = im.select('.ipc-title-link-wrapper h3.ipc-title__text')[:100]
    movies_list = [x.text.strip().split('. ', 1)[1] for x in movies_names]
    return movies_list   

def get_ratings(im):
    ratings = im.select('.ratingGroup--imdb-rating')[:100]
    ratings_list = [x.text.strip().split('(',1)[0] for x in ratings]
    return ratings_list

def rotten_tomatoes(movie_title):
    url = "https://www.rottentomatoes.com/m/" + movie_title.lower().replace(' ', '_')
#     print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3', 'Accept-Language': 'en-US,en;q=0.9'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None

    doc = BeautifulSoup(response.text, 'html.parser')
    scoreboard = doc.find('score-board-deprecated')
    
    if scoreboard:
        tomatometer_score = scoreboard.get('tomatometerscore')
        return tomatometer_score
    else:
        return None



# def get_score(im):
#     score_element = im.select('#topSection .thumbnail-scoreboard-wrap #scoreboard')
#     print(score_element)

# for title in top_100_df['Title']:
#     score = rotten_tomatoes(title)
#     if score is not None:
#         print(f"{title}:{score}")

def process_and_save_to_json():
    top_100_df = imdb_top_100()
    top_100_df['ranking_imdb'] = range(1, 101)
    results = []
    for rank, title, imdb_rating in zip(top_100_df['ranking_imdb'], top_100_df['Title'], top_100_df['Rating']):
        rotten_tomatoes_score = rotten_tomatoes(title)
        if rotten_tomatoes_score is not None:
            results.append({
                'ranking_imdb': rank,
                'tytul_filmu': title,
                'ocena_rotten_tomatoes': rotten_tomatoes_score,
                'ocena_imdb': float(imdb_rating)
            })
        else:
            results.append({
                'ranking_imdb': rank,
                'tytul_filmu': title,
                'ocena_rotten_tomatoes': 'Page not found on Rotten_Tomatoes',
                'ocena_imdb': float(imdb_rating)
            })

    with open('top_100_scores.json', 'w') as f:
        json.dump(results, f, indent=4)

process_and_save_to_json()

