# news-to-newsletter
AI-powered newsletter pipeline that ingests news from RSS feeds, processes and classifies articles, ranks relevance, and generates automated structured newsletters using a modular Python-based systems

## 🏗️ Architecture

RSS Feeds  
↓  
Data Ingestion (feedparser)  
↓  
Processing Layer  
- Classification (rule-based NLP)  
- Summarization (text processing)  
↓  
Ranking System (scoring logic)  
↓  
Newsletter Generation  
↓  
Output File (newsletter.txt)

---

## ⚙️ Features

-  RSS feed ingestion from multiple sources  
-  Article classification (Technology, Business, General)  
-  Text summarization  
-  Rule-based ranking system  
-  Automated newsletter generation  
-  Saves output as text file  
-  Modular pipeline architecture  

---

## 📁 Project Structure
project/
│
├── config.py # RSS feed configuration
├── ingest.py # Fetch data from RSS feeds
├── processor.py # Classification & summarization
├── ranking.py # Scoring system
├── pipeline.py # End-to-end pipeline
├── newsletter.py # Output generator
├── main.py # Entry point
└── newsletter.txt # Generated output file

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/newsletter-pipeline.git
cd newsletter-pipeline
