# 📰 News Intelligence Pipeline (RSS → Newsletter Generator)
📌 Project Overview

This project simulates a real-world news intelligence pipeline, similar to content aggregation systems used in platforms like Google News and Flipboard.

It ingests live RSS feeds, processes article data, performs lightweight NLP-based processing, applies a relevance scoring system, and generates a structured newsletter output.

The system is designed using a modular pipeline architecture, making it easy to extend with ML/LLM-based components in the future.

🏗️ Architecture
RSS Feeds
   ↓
Data Ingestion (feedparser)
   ↓
Processing Layer
   ├── Lightweight Classification (rule-based, extensible to ML/LLMs)
   ├── Extractive Summarization (headline-based processing)
   ↓
Ranking System (keyword + category-based scoring)
   ↓
Newsletter Generation
   ↓
Output File (newsletter.txt + Streamlit Dashboard)
🧰 Tech Stack
Python 3.11
feedparser (RSS ingestion)
Streamlit (dashboard UI)
Standard Python libraries
Modular pipeline design
✨ Features
🔗 Real-time RSS feed ingestion from multiple sources
🧠 Lightweight rule-based classification (extensible to ML/LLMs)
✂️ Extractive summarization from headlines
📊 Keyword + category-based ranking system
🧾 Automated newsletter generation
📺 Interactive Streamlit dashboard
💾 Structured text output (newsletter.txt)
🧩 Fully modular and scalable architecture
📁 Project Structure
.
├── config.py         # RSS feed configuration
├── ingest.py         # RSS data ingestion layer
├── processor.py      # Classification & summarization logic
├── ranking.py        # Article scoring system
├── pipeline.py       # End-to-end pipeline orchestration
├── newsletter.py     # Newsletter generator (console + file)
├── main.py           # CLI entry point
├── app.py            # Streamlit dashboard UI
└── newsletter.txt    # Generated output file
⚙️ How It Works
RSS feeds are fetched using feedparser
Articles are extracted (title, link, source)
Articles are classified based on source category
Headlines are processed into short summaries
A relevance score is calculated using:
Category importance
Keyword matching (AI, markets, tech trends, etc.)
Articles are sorted by relevance score
Output is generated as:
Console newsletter
Text file (newsletter.txt)
Streamlit dashboard
▶️ How to Run
1. Install dependencies
pip install feedparser streamlit
2. Run CLI newsletter generator
python main.py
3. Run Streamlit dashboard
streamlit run app.py
📊 Example Output
[Business] AI regulations reshape global markets (Score: 9)
Summary: AI regulations reshape global...
Link: https://...

[Technology] Meta opens WhatsApp to AI integration (Score: 7)
Summary: Meta opens WhatsApp to...
Link: https://...
🔮 Future Improvements
Replace rule-based classification with transformer-based NLP models (BERT / LLMs)
Implement semantic deduplication using embeddings (Sentence-BERT)
Upgrade ranking system using learning-to-rank models or embeddings
Add personalization layer based on user reading behavior
Deploy using Streamlit Cloud or AWS
Automate newsletter delivery via email scheduling (cron / AWS Lambda)
🚀 Key Highlights
Built an end-to-end data pipeline from ingestion to visualization
Designed modular and scalable architecture
Implemented ranking system simulating real-world news relevance scoring
Developed interactive Streamlit dashboard for real-time insights
Structured project with future ML/LLM upgrade path
⚠️ Disclaimer

This project uses publicly available RSS feeds for educational and portfolio purposes only.
All content belongs to their respective publishers.

👨‍💻 Author

Kamal Batcha

## 👨‍💻 Author

Kamal Batcha

---
