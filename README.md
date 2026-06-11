# news-to-newsletter
This project demonstrates a complete data pipeline that simulates a real-world content intelligence system used in news aggregators.

It ingests live RSS feeds, processes article data, applies rule-based classification, assigns relevance scores, and generates a clean, readable newsletter.

##  Architecture

RSS Feeds  
↓  
Data Ingestion (feedparser)  
↓  
Processing Layer  
- Classification (rule-based )  
- Summarization (text processing)  
↓  
Ranking System (scoring logic)  
↓  
Newsletter Generation  
↓  
Output File (newsletter.txt)

---

##  Features

-  RSS feed ingestion from multiple sources  
-  Article classification (Technology, Business, General)  
-  Text summarization  
-  Rule-based ranking system  
-  Automated newsletter generation  
-  Saves output as text file  
-  Modular pipeline architecture  

---
📁 Project Structure
.
├── config.py         # RSS feed configuration
├── ingest.py         # Data ingestion from RSS feeds
├── processor.py      # Classification and summarization logic
├── ranking.py        # Scoring and ranking system
├── pipeline.py       # End-to-end pipeline orchestration
├── newsletter.py     # Output generation (console + file)
├── main.py           # Entry point
└── newsletter.txt    # Generated output file

⚙️ How It Works
RSS feeds are fetched using feedparser
Each article is extracted (title + link)
Articles are classified based on source/category rules
A short summary is generated from the title
A relevance score is calculated using keywords + category
Articles are sorted by score
A structured newsletter is generated

▶️ How to Run
1. Clone the repository
git clone https://github.com/your-username/news-to-newsletter.git
cd news-to-newsletter
2. Install dependencies
pip install feedparser
3. Run the project
python main.py
## Future Improvements

-Replace rule-based logic with LLMs (GPT/Claude) ​
-Use embeddings for deduplication ​
-Improve ranking using semantic similarity ​
-Add personalization layer​

## Author
Kamal Batcha
