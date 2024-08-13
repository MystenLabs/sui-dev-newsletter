
import sys
import requests
from bs4 import BeautifulSoup


def collect_data(since, until):

    url = "https://blog.sui.io/page/2/"
    req = requests.request(url=url, method="GET")
    soup = BeautifulSoup(req.text, "html.parser")
    articles = soup.find_all('article')
    data = []
    for a in articles:

        title = a.find("h3", class_='gh-card-title').text
        date = a.find("time", class_='gh-card-date').get("datetime")
        url = "https://blog.sui.io" + \
            a.find("a", {"class": "gh-card-link"}).get("href")
        # print(date)
        if date >= since and date <= until:
            print("* [{}]({})".format(title, url))


def main():
    if len(sys.argv) != 3:
        print("Please provide as input a since date and an until date. E.g: python3 fetch-blog-posts.py 2023-01-01 2023-01-08")
        sys.exit(1)
    since = sys.argv[1]
    until = sys.argv[2]
    if until < since:
        print("Second argument ({}) needs to be a date later in time than the first argument ({})".format(
            until, since))
        sys.exit(1)
    collect_data(since, until)


if __name__ == "__main__":
    main()
