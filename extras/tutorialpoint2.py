from googlesearch import *
import webbrowser
#to search, will ask search query at the time of execution
query = raw_input("Input your query:")
#iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
# chrome_path = r'/Applications/Firefox.app %s'
for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
    webbrowser.open("https://google.com/search?q=%s" %query)
