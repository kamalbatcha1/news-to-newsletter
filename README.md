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
├── config.py
├── ingest.py
├── processor.py
├── ranking.py
├── pipeline.py
├── newsletter.py
├── main.py
├── app.py
└── newsletter.txt
