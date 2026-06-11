def rank(article):

    score = 1

    if article["category"] == "Technology":
        score += 5

    if article["category"] == "Business":
        score += 4

    keywords = [
        "ai",
        "google",
        "apple",
        "microsoft",
        "meta",
        "spacex",
        "market",
        "stock",
        "tariff",
        "bank",
        "business"
    ]

    title = article["title"].lower()

    for keyword in keywords:
        if keyword in title:
            score += 3

    return score
