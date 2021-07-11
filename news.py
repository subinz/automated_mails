# API: e7fc4d6eb8414e29b311aa620d234cc9
import requests

class NewsFeed:

    base_url = "https://newsapi.org/v2/everything"
    api_key = "e7fc4d6eb8414e29b311aa620d234cc9"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = f"{self.base_url}?" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        response = requests.get(url, headers=self.headers)
        content = response.json()

        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + '\n' + article['url'] + '\n\n'

        return(email_body)

if __name__ == "__main__":
    news_feed = NewsFeed(interest='nasa', from_date='2021-07-10', to_date='2021-07-11', language='en')
    print(news_feed.get())