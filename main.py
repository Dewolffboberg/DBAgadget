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
@app.route('/dbasearch', methods=['GET','POST'])
def index():
    data1 = []
    data2 = []
    data3 = []
    sum = 0
    site = "google"
    title = "dbaresults "
    check_1 = 0
    check_2 = 0
    check_3 = 0
    error = None
    if request.method == 'POST':
        if request.form.get("check1"):
            check_1 = 1
        if request.form.get("check2"):
            check_2 = 10
        if request.form.get("check2"):
            check_3 = 100
        sum = check_1 + check_2 + check_3
        if sum == 1:
            title = "chief"
        elif sum == 10:
            title = "vice president"
        elif sum == 100:
            title = "leadership"
        elif sum == 11:
            title =  "chief OR vice president"
        elif sum == 101:
            title =  "chief OR leadership"
        elif sum == 110:
            title =  "leadership OR vice president"
        elif sum == 111:
            title =  "chief OR vice president OR leadership"
        else:
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
            while(i<=10):
                try:
                    data = []
                    json_title = result['items'][i]['link']
                    json_title_1 = result['items'][i]['htmlTitle']
                    json_title_2 = result['items'][i]['snippet']
                    data1.append(highlight_title(title,json_title))
                    data2.append(highlight_title(title,json_title_1))
                    data3.append(highlight_title(title,json_title_2))
                    i = i+1
                except:
                    i = i+1

    return render_template("dbasearch.html",
                            data1 = data1, data2 = data2, data3= data3 , error = error)

@app.route('/dbanews', methods=['GET','POST'])
def dbanews():
    data1 = []
    data2 = []
    data3 = []
    sum = 0
    check_1 = 0
    check_2 = 0
    check_3 = 0
    check_4 = 0
    error = None
    company_name = 'apple'
    news_site = 'google.com'
    if request.method == 'POST':
        if request.form.get('company_name'):
            company_name = request.form.get('company_name')
        if request.form.get("check1"):
            check_1 = 1
        if request.form.get("check2"):
            check_2 = 10
        if request.form.get("check3"):
            check_3 = 100
        if request.form.get("check4"):
            check_4 = 1000
        sum = check_1 + check_2 + check_3 + check_4
        if sum == 1:
            news_site = "site:PRnewswire.com"
        elif sum == 10:
            news_site = "site:wsj.com"
        elif sum == 100:
            news_site = "site:https://www.businesswire.com"
        # elif sum == 1000:
            # title = "(site:nasdaq.com)"
        elif sum == 11:
            news_site =  "site:PRnewswire.com OR site:wsj.com"
        elif sum == 101:
            news_site =  "site:PRnewswire.com OR site:https://www.businesswire.com"
        # elif sum == 1001:
            # news_site =  "(site:PRnewswire.com OR site:nasdaq.com)"
        elif sum == 110:
            news_site =  "site:wsj.com OR site:https://www.businesswire.com"
        # elif sum == 1010:
            # news_site =  "(site:wsj.com OR site:nasdaq.com)"
        elif sum == 111:
            news_site =  "site:wsj.com OR site:https://www.businesswire.com OR site:PRnewswire.com"
        else:
            news_site = request.form.get('news_source')
        company_name = request.form.get('company_name')
        query = company_name + news_site
        # site = request.form.get('site')
        my_api_key = "AIzaSyCkdnLEjG8iRYPPSfLRuDe80XPRlMZULf4"
        my_cse_id = "015412766603364199948:gcwpmzkgfqe"

        def google_search(search_term, api_key, cse_id, **kwargs):
            service = build("customsearch", "v1", developerKey=api_key)
            res = service.cse().list(q=search_term, cx=cse_id,sort = 'date',**kwargs).execute()
            return res

        def cleantext(text):
            # no_special_char = HTMLParser.HTMLParser().unescape(mystring)
            text_1 = text.encode('ascii', 'ignore')
            cleantext = BeautifulSoup(text_1, "html").text
            return cleantext
        name = news_site +" "+ company_name
        result = google_search(name, my_api_key, my_cse_id)
        if result:
            i=0
            while(i<=10):
                try:
                    data = []
                    json_title = result['items'][i]['link']
                    json_title_1 = result['items'][i]['htmlTitle']
                    json_title_2 = result['items'][i]['snippet']
                    data1.append(cleantext(json_title))
                    data2.append(cleantext(json_title_1))
                    data3.append(cleantext(json_title_2))
                    i = i+1
                except:
                    i = i+1
    return render_template("dbanews.html",
                            data1 = data1, data2 = data2, data3= data3 , error = error)

if __name__=='__main__':
    app.run(debug=True)
