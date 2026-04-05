<title>AI Job Assistant</title>
  <style>
    body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; background: #f9f9f9; color: #333; }
    h1, h2, h3 { color: #2c3e50; }
    code { background: #eee; padding: 2px 5px; border-radius: 3px; }
    pre { background: #eee; padding: 10px; border-radius: 5px; overflow-x: auto; }
    a { color: #3498db; text-decoration: none; }
    a:hover { text-decoration: underline; }
    .section { margin-bottom: 30px; }
  </style>
</head>
<body>

  <h1>AI Job Assistant</h1>
  <p><strong>Author:</strong> Natasha Saini</p>
  <p><strong>GitHub:</strong> <a href="https://github.com/natashasaini/ai-job-assistant" target="_blank">https://github.com/natashasaini/ai-job-assistant</a></p>

  <div class="section">
    <h2>🌟 Features</h2>
    <ul>
      <li>Scrape job descriptions from any URL using BeautifulSoup and requests.</li>
      <li>Score resumes against job descriptions using OpenAI GPT-4.1.</li>
      <li>Provide AI-driven suggestions for resume improvement.</li>
      <li>Generate tailored answers for job application questions.</li>
      <li>Structured JSON outputs for easy backend integration.</li>
    </ul>
  </div>

  <div class="section">
    <h2>🛠 Tech Stack</h2>
    <ul>
      <li>Python 3.14</li>
      <li>BeautifulSoup4, requests, lxml</li>
      <li>OpenAI API</li>
      <li>LangChain / LangGraph for agent workflows</li>
      <li>Pydantic for data validation</li>
    </ul>
  </div>

  <div class="section">
    <h2>⚡ Installation</h2>
    <pre>
# Clone repo
git clone https://github.com/natashasaini/ai-job-assistant.git
cd ai-job-assistant

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
    </pre>
  </div>

  <div class="section">
    <h2>▶️ Usage</h2>
    <pre>
# Make sure you have a resume file
echo "Your resume text here" > resume.txt

# Run main script
python app/main.py

# Example output:
{
  "score": 70,
  "suggestions": [
    "Tailor the resume to the job description",
    "Highlight additional technical skills and experience"
  ]
}
    </pre>
  </div>

  <div class="section">
    <h2>📁 Project Structure</h2>
    <ul>
      <li><code>app/agents/</code> - LLM agents like resume scorer & answer generator</li>
      <li><code>app/tools/</code> - Scraper and utility functions</li>
      <li><code>app/models/</code> - Data schemas (Pydantic models)</li>
      <li><code>app/main.py</code> - Entry point script</li>
      <li><code>resume.txt</code> - Sample resume input</li>
      <li><code>requirements.txt</code> - Python dependencies</li>
    </ul>
  </div>

  <div class="section">
    <h2>💡 Next Steps</h2>
    <ul>
      <li>Convert project to a FastAPI API for web requests.</li>
      <li>Add a frontend UI for interactive resume scoring.</li>
      <li>Deploy the project live for portfolio demonstration.</li>
    </ul>
  </div>

  <div class="section">
    <h2>⚖️ License</h2>
    <p>MIT License</p>
  </div>

</body>
</html>
