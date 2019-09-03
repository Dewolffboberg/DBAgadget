#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, request, url_for
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
import pandas as pd
warnings.filterwarnings("ignore")
from bs4 import BeautifulSoup
import json
from googleapiclient.discovery import build


app = Flask(__name__)
@app.route('/')
@app.route('/', methods=['POST'])
def index():
    data =[]
    data1 = []
    # data2 = []
    # data3 = []
    # data = pd.DataFrame(columns=['Output'])
    error = None
    if request.method == 'POST':
        title = request.form.get('title')
        site = request.form.get('site')
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
            text_2 = text_1.encode('ascii', 'ignore')
            cleantext = BeautifulSoup(text_2, "html").text
            if search_word_1 in cleantext:
                # highlight_text = cleantext.replace(search_word_1, '\033[44;33m{}\033[m'.format(search_word_1))
                highlight_text = cleantext
            else:
                highlight_text = cleantext
            return highlight_text

        name = site +" "+title
        result = google_search("site:"+name, my_api_key, my_cse_id)
        if result:
            i=0
            # j = 0
            # k = 0
            while(i<=10):
                try:
                    data = []
                    json_title = result['items'][i]['link']
                    json_title_1 = result['items'][i]['htmlTitle']
                    json_title_2 = result['items'][i]['snippet']
                    # df.loc[j] = highlight_title(title,json_title)
                    # df.loc[k] = [highlight_title(title,json_title_1)]
                    # cleantext = BeautifulSoup(json_title_1, "html").text
                            # listappend
                    data.append(highlight_title(title,json_title))
                    data.append(highlight_title(title,json_title_1))
                    data.append(highlight_title(title,json_title_2))

                    i = i+1
                    # j = j+1
                    # k = k+1
                except:
                    i = i+1
                data1.append(data)

    return render_template("myprogram.html",
                            data = data1 , error = error)

if __name__=='__main__':
    app.run(debug=True)
