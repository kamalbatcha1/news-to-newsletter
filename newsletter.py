def generate_newsletter(articles):

    print("\n--- AUTOMATED NEWSLETTER ---\n")

    with open("newsletter.txt", "w", encoding="utf-8") as f:

        for article in articles:

            print(
                f"[{article['category']}] "
                f"{article['title']} "
                f"(Score: {article['score']})"
            )

            print(article["link"])
            print()

            f.write(
                f"[{article['category']}] "
                f"{article['title']}\n"
            )

            f.write(
                f"Summary: {article['summary']}\n"
            )

            f.write(
                f"Score: {article['score']}\n"
            )

            f.write(
                f"Link: {article['link']}\n\n"
            )

    print("Newsletter saved as newsletter.txt")
