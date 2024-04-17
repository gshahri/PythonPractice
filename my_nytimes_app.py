import requests


def search_nytimes_articles(api_key, query):
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    params = {
        "q": query,
        "api-key": api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None


if __name__ == "__main__":
    api_key = input("Enter your New York Times API key: ")
    query = input("Enter search query: ")

    articles_data = search_nytimes_articles(api_key, query)

    if articles_data:
        print("Search Results:")
        for article in articles_data['response']['docs']:
            print("Headline:", article['headline']['main'])
            print("Abstract:", article['abstract'])
            print("Published Date:", article['pub_date'])
            print("URL:", article['web_url'])
            print("-------------------")
    else:
        print("Articles not found or API request failed.")
