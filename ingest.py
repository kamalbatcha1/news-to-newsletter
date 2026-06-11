import feedparser
from config import RSS_FEEDS

def ingest_data():
    articles = []

    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:
            articles.append({
                "source": source,
                "title": entry.title,
                "link": entry.link
            })

    return articles








