
# AI Job Assistant 🚀

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.101-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4.1-red)

**Author:** Natasha Saini  
**GitHub:** https://github.com/NATASHASAINI/ai-job-assistant  

---

## 🧠 Overview

AI Job Assistant is an **agentic AI system** that acts as the intelligence layer (“brain”) of a job search assistant.

It combines:
- Web scraping
- LLM reasoning (GPT-4o-mini / GPT-4.1)
- Agent-based workflows
- Structured JSON outputs

to analyze resumes and generate personalized job insights.

---

## ⚙️ System Architecture (Agentic Pipeline)
                  ## 🧠 System Architecture

```text
                    ┌──────────────────────┐
                    │     User Input       │
                    └─────────┬────────────┘
                              │
                              ▼
                    ┌──────────────────────┐
                    │   FastAPI Layer      │
                    │   (API Gateway)      │
                    └─────────┬────────────┘
                              │
          ┌───────────────────┴───────────────────┐
          │                                       │
          ▼                                       ▼
┌──────────────────────┐              ┌──────────────────────┐
│ Resume Endpoint      │              │ Answer Endpoint      │
└─────────┬────────────┘              └─────────┬────────────┘
          │                                       │
          ▼                                       ▼
┌──────────────────────────────┐   ┌──────────────────────────────┐
│ Job Scraper Tool             │   │ Job Scraper Tool             │
│ (BeautifulSoup + Requests)   │   │ (BeautifulSoup + Requests)   │
└─────────┬────────────────────┘   └─────────┬────────────────────┘
          │                                       │
          └───────────────────┬───────────────────┘
                              ▼
                    ┌──────────────────────┐
                    │     Agent Layer      │
                    │  - Resume Scorer     │
                    │  - Answer Generator  │
                    └─────────┬────────────┘
                              ▼
                    ┌──────────────────────┐
                    │      LLM Layer       │
                    │ GPT-4o-mini / GPT-4.1│
                    │ Few-shot Prompting   │
                    └─────────┬────────────┘
                              ▼
                    ┌──────────────────────┐
                    │ Parsing & Validation │
                    │ (Pydantic Schema)    │
                    └─────────┬────────────┘
                              ▼
                    ┌──────────────────────┐
                    │ Final JSON Response  │
                    └──────────────────────┘
```
<img width="977" height="791" alt="Screenshot 2026-04-26 at 1 41 25 PM" src="https://github.com/user-attachments/assets/78606932-67e8-4a52-834d-b43c61fb23b5" />

## 🌟 Features

### 🧠 Resume Intelligence Agent
- Scores resume vs job description (0–100)
- Identifies strengths & gaps
- Provides improvement suggestions

### 💬 AI Answer Generator
- Generates human-like job application answers
- Context-aware responses using job + profile data

### 🌐 Smart Web Scraper
- Extracts clean job descriptions from URLs
- Removes noise (ads, navigation, scripts)

### 📦 Structured Output System
- Strict JSON validation using Pydantic
- Backend-ready response format

---

## 🛠 Tech Stack

- Python 3.14
- FastAPI
- OpenAI GPT-4o-mini / GPT-4.1
- BeautifulSoup4
- Requests
- Pydantic

---

## ⚡ Installation

```bash
# Clone repo
git clone https://github.com/NATASHASAINI/ai-job-assistant.git
cd ai-job-assistant

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
