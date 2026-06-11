# 📰 News Intelligence Pipeline (RSS → Newsletter Generator)

## 📌 Project Overview

This project demonstrates a complete end-to-end **data pipeline system** that simulates a real-world **content intelligence engine** used in modern news aggregators.

It ingests live RSS feeds, processes article data, applies rule-based classification, assigns relevance scores, and generates a structured and readable newsletter.

---

## 🏗️ Architecture

```
RSS Feeds
   ↓
Data Ingestion (feedparser)
   ↓
Processing Layer
   ├── Classification (rule-based)
   ├── Summarization (text processing)
   ↓
Ranking System (scoring logic)
   ↓
Newsletter Generation
   ↓
Output File (newsletter.txt)
```

---

## ✨ Features

* 🔗 RSS feed ingestion from multiple sources
* 🧠 Rule-based article classification (Technology, Business, General)
* ✂️ Lightweight text summarization from headlines
* 📊 Custom ranking system using keyword scoring
* 🧾 Automated newsletter generation
* 💾 Saves structured output to a text file
* 🧩 Fully modular pipeline architecture

---

## 📁 Project Structure

```
.
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
```

---

## ⚙️ How It Works

1. RSS feeds are fetched using `feedparser`
2. Each article is extracted (title + link)
3. Articles are classified using rule-based logic
4. A short summary is generated from the title
5. A relevance score is calculated using keywords + category
6. Articles are sorted based on score
7. A structured newsletter is generated and saved

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/news-to-newsletter.git
cd news-to-newsletter
```

1. Install dependencies
pip install feedparser streamlit
2. Run CLI newsletter generator
python main.py
3. Run Streamlit dashboard
streamlit run app.py
```


## 🔮 Future Improvements

* Replace rule-based classification with LLMs (GPT / Claude)
* Use embeddings for deduplication of similar news
* Improve ranking using semantic similarity
* Add personalization layer for users
* Deploy as a web app (Streamlit / FastAPI)
* Automate email newsletter delivery

---

## ⚠️ Disclaimer

This project uses publicly available RSS feeds for educational and portfolio purposes only.
All article titles and links belong to their respective publishers.

---

## 👨‍💻 Author

Kamal Batcha

---
