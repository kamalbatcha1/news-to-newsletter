# 📰 News Intelligence Pipeline (RSS → AI Newsletter System)

---

## 📌 Project Overview

This project simulates a real-world **news intelligence pipeline**, similar to platforms like **Google News** and **Flipboard**.

It ingests live RSS feeds, processes article data, applies lightweight NLP processing, computes relevance scores, and generates a structured newsletter output.

The system is designed using a **modular pipeline architecture**, making it easy to extend into ML/LLM-based systems in the future.

---

## 🏗️ Architecture
RSS Feeds
↓
Data Ingestion (feedparser)
↓
Processing Layer
├── Lightweight Classification (rule-based, extensible to ML/LLMs)
├── Extractive Summarization
↓
Ranking System (keyword + category-based scoring)
↓
Output Generation
├── Console Newsletter
├── Text File (newsletter.txt)
├── Streamlit Dashboard


---

## 🧰 Tech Stack

- Python 3.11
- feedparser (RSS ingestion)
- Streamlit (dashboard UI)
- Standard Python libraries
- Modular pipeline design

---

## ✨ Features

- 🔗 Real-time RSS feed ingestion  
- 🧠 Rule-based classification system  
- ✂️ Extractive summarization from headlines  
- 📊 Keyword + category-based ranking system  
- 🧾 Automated newsletter generation  
- 📺 Interactive Streamlit dashboard  
- 💾 Structured output (newsletter.txt)  
- 🧩 Fully modular and scalable architecture  

---

## 📁 Project Structure
.
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

---

## ⚙️ How It Works

1. RSS feeds are fetched using `feedparser`
2. Articles are extracted (title + link)
3. Articles are classified using source/category
4. Headlines are summarized
5. Relevance score is calculated using:
   - Category importance
   - Keyword matching
6. Articles are sorted by score
7. Output is generated in:
   - CLI newsletter
   - Text file (`newsletter.txt`)
   - Streamlit dashboard

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install feedparser streamlit

2. Run CLI newsletter generator
python main.py
3. Run Streamlit dashboard
streamlit run app.py
🔮 Future Improvements
Replace rule-based classification with transformer models (BERT / LLMs)
Add semantic deduplication using embeddings (Sentence-BERT)
Improve ranking using learning-to-rank models
Add personalization based on user behavior
Deploy using Streamlit Cloud or AWS
Automate newsletter delivery via email scheduling
🚀 Key Highlights
End-to-end data pipeline system
Modular production-style architecture
Ranking system simulating real-world relevance scoring
Interactive Streamlit dashboard
Clear ML/AI upgrade path
⚠️ Disclaimer

This project uses publicly available RSS feeds for educational purposes only.
All content belongs to their respective publishers.

👨‍💻 Author

Kamal Batcha
