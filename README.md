# news-to-newsletter
AI-powered newsletter pipeline that ingests news from RSS feeds, processes and classifies articles, ranks relevance, and generates automated structured newsletters using a modular Python-based systems

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
