# 📰 News Intelligence Pipeline (RSS → Newsletter Generator)

🚀 Overview

This project simulates a real-world news intelligence system inspired by platforms like Google News and Flipboard.

It builds an end-to-end data pipeline that:

Ingests live RSS feeds
Processes and classifies articles
Applies a relevance scoring system
Generates structured newsletters
Displays insights via a Streamlit dashboard

📌 Focus: Data Engineering + NLP + Ranking Systems + UI Visualization

🧠 Architecture
RSS Feeds
   ↓
Data Ingestion (feedparser)
   ↓
Processing Layer
   ├── Classification (rule-based, extensible to ML/LLMs)
   ├── Extractive Summarization (headline-based NLP)
   ↓
Ranking Engine (keyword + category scoring)
   ↓
Output Generation
   ├── Console Newsletter
   ├── Text File Report
   ├── Streamlit Dashboard
   
✨ Key Features

🔗 Real-time RSS feed ingestion
🧠 Intelligent rule-based classification system
✂️ Lightweight NLP-based summarization
📊 Custom ranking algorithm for relevance scoring
📺 Interactive Streamlit dashboard
💾 Automated newsletter generation (TXT output)
🧩 Fully modular and scalable architecture
🔌 Easy upgrade path to ML / LLM-based system

🧰 Tech Stack

Python 3.11
feedparser (RSS ingestion)
Streamlit (UI dashboard)
Standard Python libraries
Modular pipeline design

📁 Project Structure
.
├── config.py         # RSS feed configuration
├── ingest.py         # RSS ingestion layer
├── processor.py      # Classification + summarization
├── ranking.py        # Scoring engine
├── pipeline.py       # End-to-end orchestration
├── newsletter.py     # Newsletter generator
├── main.py           # CLI entry point
├── app.py            # Streamlit dashboard
└── newsletter.txt    # Output file

⚙️ How It Works

RSS feeds are fetched using feedparser
Articles are extracted (title + link)
Articles are classified by category
Headlines are summarized (extractive method)
Relevance score is computed using:
Category weight
Keyword matching
Articles are sorted by score
Output is generated in multiple formats:
CLI newsletter
File-based report
Web dashboard

▶️ How to Run
1. Clone Repository
git clone https://github.com/kamalbatcha1/news-to-newsletter.git
cd news-to-newsletter
2. Install Dependencies
pip install feedparser streamlit
3. Run CLI Newsletter
python main.py
4. Launch Dashboard
   
streamlit run app.py
📸 Dashboard Preview

![Dashboard preview](newsletter1.png)

🔮 Future Improvements
Replace rule-based classification with transformer models (BERT / LLMs)
Add semantic similarity using embeddings (Sentence-BERT)
Improve ranking using learning-to-rank models
Add personalization based on user behavior
Deploy using Streamlit Cloud / AWS
Automate newsletter delivery via email scheduling

🚀 Key Highlights
Built a complete end-to-end data pipeline system
Designed modular and production-style architecture
Implemented ranking system simulating real-world news relevance scoring
Created interactive dashboard using Streamlit
Built with clear ML/AI upgrade path

⚠️ Disclaimer

This project uses publicly available RSS feeds for educational purposes only.
All content belongs to their respective publishers.
---

## 👨‍💻 Author

Kamal Batcha

---
