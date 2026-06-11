# 📰 News Intelligence Pipeline (RSS → Newsletter Generator)


![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Project-Active-success)

---

## 🚀 Overview

This project simulates a real-world **news intelligence system** inspired by platforms like **Google News** and **Flipboard**.

It builds an end-to-end data pipeline that:

- Ingests live RSS feeds  
- Processes and classifies articles  
- Applies relevance scoring  
- Generates structured newsletters  
- Displays insights via Streamlit dashboard  

📌 Focus: Data Engineering + NLP + Ranking Systems + Visualization  

---

## 🧠 Architecture


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
Output Layer
├── CLI Newsletter
├── Text File Report
├── Streamlit Dashboard


---

## ✨ Key Features

- 🔗 Real-time RSS feed ingestion  
- 🧠 Rule-based classification system  
- ✂️ Lightweight NLP-based summarization  
- 📊 Custom ranking algorithm  
- 📺 Interactive Streamlit dashboard  
- 💾 Automated newsletter generation  
- 🧩 Modular and scalable architecture  
- 🔌 Ready for ML / LLM upgrades  

---

## 🧰 Tech Stack

- Python 3.11  
- feedparser (RSS ingestion)  
- Streamlit (UI dashboard)  
- Standard Python libraries  

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


---

## ⚙️ How It Works

1. RSS feeds are fetched using `feedparser`  
2. Articles are extracted (title + link)  
3. Articles are classified by category  
4. Headlines are summarized  
5. Relevance score is calculated using:
   - Category weight  
   - Keyword matching  
6. Articles are sorted by score  
7. Output generated in:
   - CLI newsletter  
   - Text file  
   - Streamlit dashboard  

---

## ▶️ How to Run

### 1. Clone repository

```bash
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
Automate newsletter delivery via email scheduling
⚠️ Disclaimer

This project uses publicly available RSS feeds for educational purposes only.
All content belongs to their respective publishers.
## 👨‍💻 Author

Kamal Batcha

---
