# 📚 Prep Predictor

**Prep Predictor** is an AI-powered roadmap generator built using **Streamlit** and **Langchain**. Just input your degree, year, current topics, duration, and goal — and the app generates a detailed, beginner-friendly **weekly study roadmap** including learning resources, exercises, and hands-on projects.

---

## 🚀 Features

- 🎓 Personalized study plans based on degree, year, and learning goals
- 📆 Week-by-week learning roadmap
- 📚 Recommended books, courses, and resources
- 🛠️ Includes hands-on projects and assessments
- 🤖 Powered by Langchain + Ollama LLM for dynamic content generation

---

## 🧠 How It Works

The app uses:
- `Langchain`'s `PromptTemplate` to define a custom prompt format
- `OllamaLLM` to generate structured learning content
- `Streamlit` to serve the interactive web interface

Prompt input includes:
- `degree`: Your degree program (e.g., B.Tech, B.Sc)
- `year`: Your current year of study
- `topics`: Topics you've already covered
- `duration`: Available weeks for preparation
- `goal`: Your learning objective (e.g., master NLP, crack GATE, etc.)

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/D-i-vyansh/prep_predictor.git
cd prep_predictor

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
