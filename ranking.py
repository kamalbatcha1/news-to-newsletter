def rank(article):
    title = article["title"].lower()
    category = article["category"]

    category_weights = {
        "Technology": 10,
        "Business": 8
    }

    score = category_weights.get(category, 5)

    keywords = [
        "ai", "google", "apple", "microsoft",
        "meta", "spacex", "market", "stock",
        "tariff", "bank", "business"
    ]

    keyword_score = 0

    for keyword in keywords:
        if keyword in title:
            keyword_score += 1  

   
    keyword_score = min(keyword_score, 5)
    final_score = score + (keyword_score * 2)

    return final_score