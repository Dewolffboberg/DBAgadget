#!/usr/bin/env python
# from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for

# from weather import query_api
app = Flask(__name__)
@app.route('/')
# def index():
#     return render_template('myprogram.html')
    # data=[{'name':'president'},{'name':'vice'},{'name':'chief'}, {'name':'executive'}]

@app.route('/', methods=['POST'])
def index():
    data =[]
    error = None
    if request.method == 'POST':
        title = request.form.get('title')
        site = request.form.get('site')
        resp = query_api(site,title)
        # pp(resp)
        if resp:
            data = resp
    # if len(data) <= 1:
    #         error = 'Did not get complete response'
    return render_template("myprogram.html",
                           data=data,
                           error=error)
# @app.route("/result" , methods=['GET', 'POST'])
# def result():
#     data = []
#     error = None
#     select = request.form.get('comp_select')
#     resp = query_api(select)
#     pp(resp)
#     if resp:
#         data.append(resp)
#         if len(data) != 2:
#             error = 'Bad Response from Weather API'
#     return render_template('result.html',data=data,error=error)
if __name__=='__main__':
    app.run(debug=True)
