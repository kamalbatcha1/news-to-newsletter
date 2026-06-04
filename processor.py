def classify(title):
    title = title.lower()

    if any(word in title for word in ["ai", "google", "apple", "microsoft"]):
        return "Technology"
    elif any(word in title for word in ["market", "business", "stock"]):
        return "Business"
    else:
        return "General"


def summarize(title):
    return " ".join(title.split()[:6]) + "..."