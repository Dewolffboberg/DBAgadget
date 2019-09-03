from googlesearch import search
# class Gsearch_python:
#    def __init__(self,name_search):
#        self.name = name_search
#    def Gsearch(self):
#        count = 0
#       # try :
#       #    from googlesearch import search
#       # except ImportError:
#       #    print("No Module named 'google' Found")
#        for i in search(query=self.name,tld='com',lang='en',num=10,stop=5,pause=2):
#            count += 1
#            print (count)
#            print(i + '\n')
#
# if __name__=='__main__':
#    query = raw_input("Input your query:")
#    gs = Gsearch_python(query)
#    gs.Gsearch()
#


from googlesearch import *
import webbrowser
#to search, will ask search query at the time of execution
query = raw_input("Input your query:")
title = raw_input("Title:")
#iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
# chrome_path = r'/Applications/Firefox.app %s'
for url in search(query, tld="com", num=1, stop = 1, pause = 2.5):
    webbrowser.open("https://google.com/search?q=site:%s %s" % (query,title))
