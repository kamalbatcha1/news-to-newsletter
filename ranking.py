def rank(article):
    score = 1

    if article["category"] == "Technology":
        score += 5
    if article["category"] == "Business":
        score += 4

    keywords = ["ai", "google", "apple", "market"]

    for word in keywords:
        if word in article["title"].lower():
            score += 3

    return score