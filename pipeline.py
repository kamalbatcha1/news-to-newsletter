from ingest import ingest_data
from processor import classify, summarize
from ranking import rank

def run_pipeline():

    articles = ingest_data()
    processed = []

    for a in articles:

        article = {
            "title": a["title"],
            "link": a["link"],
            "category": classify(a["title"]),
            "summary": summarize(a["title"])
        }

        article["score"] = rank(article)
        processed.append(article)

    processed.sort(key=lambda x: x["score"], reverse=True)

    return processed
