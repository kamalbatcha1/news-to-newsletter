# 📰 News Intelligence Pipeline (RSS → Newsletter Generator)

🚀 Overview

This project simulates a real-world news intelligence system inspired by platforms like Google News and Flipboard.

It builds an end-to-end data pipeline that:

Ingests live RSS feeds
Processes and classifies articles
Applies relevance scoring
Generates structured newsletters
Displays insights via a Streamlit dashboard

📌 Focus: Data Engineering + NLP + Ranking Systems + Visualization

🧠 Architecture
RSS Feeds
   ↓
Data Ingestion (feedparser)
   ↓
Processing Layer
   ├── Classification (rule-based, extensible to ML/LLMs)
   ├── Extractive Summarization
   ↓
Ranking Engine
   ├── Keyword + category scoring
   ↓
Output Generation
   ├── CLI Newsletter
   ├── Text File Report
   ├── Streamlit Dashboard
✨ Key Features
🔗 Real-time RSS feed ingestion
🧠 Rule-based classification system
✂️ Lightweight NLP-based summarization
📊 Custom ranking algorithm
📺 Interactive Streamlit dashboard
💾 Automated newsletter generation
🧩 Modular and scalable architecture
🔌 Ready for ML / LLM upgrades
🧰 Tech Stack
Python 3.11
feedparser (RSS ingestion)
Streamlit (UI dashboard)
Standard Python libraries
📁 Project Structure
.
├── config.py
├── ingest.py
├── processor.py
├── ranking.py
├── pipeline.py
├── newsletter.py
├── main.py
├── app.py
└── newsletter.txt
⚙️ How It Works
RSS feeds are fetched using feedparser
Articles are extracted (title + link)
Articles are classified by category
Headlines are summarized
Relevance score is calculated using:
Category weight
Keyword matching
Articles are sorted by score
Output generated in:
CLI newsletter
Text file
Web dashboard
▶️ How to Run
1. Clone repository
git clone https://github.com/kamalbatcha1/news-to-newsletter.git
cd news-to-newsletter
2. Install dependencies
pip install feedparser streamlit
3. Run CLI newsletter
python main.py
4. Run Streamlit dashboard
streamlit run app.py
📸 Dashboard Preview

🔮 Future Improvements
Replace rule-based classification with transformer models (BERT / LLMs)
Add semantic similarity using embeddings (Sentence-BERT)
Improve ranking using learning-to-rank models
Add personalization based on user behavior
Deploy using Streamlit Cloud / AWS
Automate newsletter delivery via email
🚀 Key Highlights
End-to-end data pipeline system
Modular production-style architecture
Ranking system simulating real-world news relevance
Interactive Streamlit dashboard
Clear ML/AI upgrade path
⚠️ Disclaimer

This project uses publicly available RSS feeds for educational purposes only.
All content belongs to their respective publishers.
## 👨‍💻 Author

Kamal Batcha

---
