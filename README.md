
# AI Job Assistant 🚀

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.101-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4.1-red)

Author: **Natasha Saini**  
GitHub: [https://github.com/natashasaini/ai-job-assistant](https://github.com/natashasaini/ai-job-assistant)

---

## 🌟 Features

- Scrape job descriptions from any URL using **BeautifulSoup** and **requests**
- Score resumes against job descriptions using **OpenAI GPT-4.1**
- Provide AI-driven suggestions for resume improvement
- Generate tailored answers for job application questions
- Structured **JSON outputs** for backend integration

---

## 🛠 Tech Stack

- Python 3.14
- BeautifulSoup4, requests, lxml
- OpenAI API
- FastAPI / LangChain / LangGraph for agent workflows
- Pydantic for data validation

---

## ⚡ Installation

```bash
# Clone repo
git clone https://github.com/natashasaini/ai-job-assistant.git
cd ai-job-assistant

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
