def generate_newsletter(articles):

    print("\n --- NEWSLETTER --- \n")

    with open("newsletter.txt", "w", encoding="utf-8") as f:

        for a in articles:

            print(a["category"], "|", a["title"], "|", round(a["score"], 2))

            f.write(f"[{a['category']}] {a['title']}\n")
            f.write(f"{a['summary']}\n")
            f.write(f"{a['link']}\n\n")
