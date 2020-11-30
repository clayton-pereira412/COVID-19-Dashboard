import requests
url = ('http://newsapi.org/v2/top-headlines?'
       'country=in&''q=COVID-19&'
       'apiKey=a3c43b5a11c8458b8ea9de71bd6c2820')
response = requests.get(url).json()
#print (response)

article = response["articles"]

# empty list which will
# contain all trending news
results = []

for ar in article:
    results.append(ar["title"])

for i in range(len(results)):

    # printing all trending news
    print(i + 1, results[i])
