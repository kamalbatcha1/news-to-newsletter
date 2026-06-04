from pipeline import run_pipeline
from newsletter import generate_newsletter

if __name__ == "__main__":
    articles = run_pipeline()
    generate_newsletter(articles)