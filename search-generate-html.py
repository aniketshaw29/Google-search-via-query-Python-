#pip install requests

import requests

def google_search(query):
    query = query.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return None

search_query = "Python programming language"
result = google_search(search_query)

if result:
    html_file = open("index.html", "w")
    html_file.write(result)
    html_file.close()

else:
    print("Search failed")
