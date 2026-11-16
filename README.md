# Alenan-AI-Researcher
# 1. Project Overview
Alenan AI Researcher is an autonomous, multi-agent AI research system built to automate deep
web intelligence, content extraction, structured report synthesis, and critical quality evaluation—all
unified inside an interactive Streamlit studio.
Live Demo: [Launch Alenan AI Researcher] https://alenan-ai-researcher.streamlit.app/

# 2. System Architecture & Multi-Agent Workflow
The platform operates on a deterministic multi-agent orchestration pipeline powered by LangGraph
and LangChain:
### 1. Researcher Agent: Queries real-time web intelligence using Tavily Search to gather relevant,
high-authority sources on any given topic.
### 2. Scraper Agent: Automatically extracts clean, structured text content from discovered URLs using
BeautifulSoup.
### 3. Writer Agent: Synthesizes raw scraped data into a comprehensive, well-structured research
report powered by Groq (Llama 3.1).
### 4. Critic Agent: Evaluates the drafted report for factual accuracy, depth, and clarity, providing
structured feedback and quality scoring
# 3. Technology Stack
Component
Technologies & Libraries
Orchestration & Agents
LangGraph, LangChain
LLM Inference
Groq API (openai/gpt-oss-20b )
Web Search & Scraping
Tavily Search API, BeautifulSoup4, Requests
Frontend & Deployment
Streamlit, Streamlit Community Cloud
Language & Environment
Python 3.12

# 4. Repository Directory Structure
Alenan-AI-Researcher/
├── app.py               # Streamlit web application & UI
├── pipline.py           # LangGraph multi-agent workflow orchestration
├── Agents.py            # LLM definitions, prompts, and agent chains
├── tools.py             # Custom Tavily search and BeautifulSoup scraping tools
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation


# 5. Local Setup & Installation Guide
### 1. Clone the repository
git clone https://github.com/AbdulHanan0812/Alenan-AI-Researcher.git
cd Alenan-AI-Researcher
### 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS/Linux
### 3. Install dependencies
pip install -r requirements.txt

