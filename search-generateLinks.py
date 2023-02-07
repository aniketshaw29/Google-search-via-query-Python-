#pip install google

from googlesearch import search

query = "Java"

for result in search(query, num=10, stop=10, pause=2):
    print(result)
