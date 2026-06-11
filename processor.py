def classify(article):
    """
    Use RSS feed source as the main category.
    """

    return article["source"]


def summarize(title, max_words=8):
    words = title.split()

    if len(words) <= max_words:
        return title

    return " ".join(words[:max_words]) + "..."
