from datetime import datetime
import os
import pytz
import requests
import math
from googlesearch import *
import webbrowser
import os.path
import numpy as np
import HTMLParser
import warnings
warnings.filterwarnings("ignore")
from bs4 import BeautifulSoup
import json
from googleapiclient.discovery import build

my_api_key = "AIzaSyCkdnLEjG8iRYPPSfLRuDe80XPRlMZULf4"
my_cse_id = "015412766603364199948:gcwpmzkgfqe"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res
def highlight_title(search_word, text):

    mystring = text

    no_special_char = HTMLParser.HTMLParser().unescape(mystring)

    search_word_1 = search_word.lower()

    text_1 = no_special_char.lower()

    cleantext = BeautifulSoup(text_1, "html").text
    if search_word_1 in cleantext:
        highlight_text = cleantext.replace(search_word_1, '\033[44;33m{}\033[m'.format(search_word_1))
    else:
        highlight_text = cleantext
    return highlight_text

# API_KEY = 'AIzaSyCkdnLEjG8iRYPPSfLRuDe80XPRlMZULf4'
# API_URL = ('https://cse.google.com/cse?cx=015412766603364199948:z7aiktgcxpm')
def query_api(site,title):
    try:
        name = site +" "+title
        result = google_search("site:"+name, my_api_key, my_cse_id)
        data = []
        if result:
            i=0
            while(i<=10):
                try:
                    json_title = result['items'][i]['link']
                    json_title_1 = result['items'][i]['htmlTitle']
                    json_title_2 = result['items'][i]['snippet']
                    # cleantext = BeautifulSoup(json_title_1, "html").text
                    data.append(highlight_title(title,json_title))
                    data.append(highlight_title(title,json_title_1))
                    data.append(highlight_title(title,json_title_2))
                    i = i+1
                except:
                    i = i+1
                    # print "******"
    except Exception as exc:
        print(exc)
        data = 'k'
    return data


# print google_search('www.dbaresults.com vice',my_api_key,my_cse_id)
