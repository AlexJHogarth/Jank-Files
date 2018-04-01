import urllib.request
import json
import webbrowser
apikey = 'c446de5044e9cf5445a6247414e7b1fe'

MovieName = input("Movie Title:")
MovieName = MovieName.replace(" ", "+")

print("Loading...")

def GetTopURLs(Movies,number):
    URLList = [Movies[i]['hosterurls'][0]['url'] for i in range(0,number)]
    return URLList

response = urllib.request.urlopen('https://www.alluc.ee/api/search/stream/?apikey='+apikey+'&query='+MovieName+'&from=0&getmeta=0')
html = response.read()
html = html.decode()
#print(html)

Movies = json.loads(html)
Movies = Movies['result']

#print(Movies)

if len(Movies) != 0:
    URLS = GetTopURLs(Movies,len(Movies))
    for url in URLS:
        print(url)
        webbrowser.open(url)
        input("Hit Enter For Next Link")
else:
    print("No Links Found")
