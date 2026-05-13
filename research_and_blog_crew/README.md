# 🤖 Research & Blog Crew — CrewAI

> A multi-agent AI system that autonomously **researches any topic** and **writes a reader-friendly blog post** using a sequential crew of specialized AI agents — powered by [CrewAI](https://crewai.com) and Google Gemini.

---

## 📌 Overview

**Research & Blog Crew** is a production-style CrewAI project that demonstrates how to orchestrate two autonomous AI agents working in sequence:

1. **Report Generator Agent** — conducts deep research on a given topic and produces a structured, ~1000-word report covering current facts, multi-dimensional insights, and future trends.
2. **Blog Writer Agent** — transforms the research report into a fun, accessible ~500-word blog post written in an *"Explain Like I'm 5"* style, making complex topics simple for any audience.

The result is automatically saved as a `.md` file in the `blogs/` directory — ready to publish.

---

## ✨ Features

- 🔗 **Sequential multi-agent pipeline** — agents pass context between each other automatically
- 🧠 **YAML-driven configuration** — define agents and tasks without touching Python
- 📝 **Auto-saved blog output** — generated markdown saved directly to `blogs/`
- 🔌 **Pluggable LLM backend** — powered by Google Gemini via `crewai[google-genai]`
- 🛠️ **Custom tool scaffold** — ready-to-extend `custom_tool.py` for adding capabilities
- 📚 **Knowledge base support** — user preferences injected via `knowledge/user_preference.txt`
- ⚡ **UV-managed dependencies** — fast, reproducible installs with `uv`

---

## 🏗️ Project Structure

```
research_and_blog_crew/
│
├── src/research_and_blog_crew/
│   ├── config/
│   │   ├── agents.yaml          # Agent roles, goals & backstories
│   │   └── tasks.yaml           # Task descriptions & expected outputs
│   ├── tools/
│   │   └── custom_tool.py       # Scaffold for custom tools
│   ├── crew.py                  # Crew orchestration (agents + tasks + process)
│   ├── main.py                  # Entry point — set your topic here
│   └── __init__.py
│
├── blogs/
│   └── ai_engineering_career_path.md   # Sample generated blog post
│
├── knowledge/
│   └── user_preference.txt      # User context for agent personalization
│
├── pyproject.toml               # Project metadata & dependencies
├── uv.lock                      # Locked dependency tree
├── .gitignore
└── README.md
```

---

## 🤝 Agent Architecture

```
User Input (topic)
       │
       ▼
┌─────────────────────────┐
│   Report Generator      │  ← Role: Expert Researcher
│   Agent                 │    Goal: Create a detailed ~1000-word report
│                         │    covering facts, trends & future outlook
└────────────┬────────────┘
             │  report (context passed automatically)
             ▼
┌─────────────────────────┐
│   Blog Writer           │  ← Role: Expert Blog Writer
│   Agent                 │    Goal: Write a fun ~500-word blog post
│                         │    in "Explain Like I'm 5" style
└────────────┬────────────┘
             │
             ▼
    blogs/<output>.md
```

**Process:** `Process.sequential` — agents run one after the other, with the output of the first feeding into the second.

---

## 🚀 Getting Started

### Prerequisites

- Python `>=3.10, <3.14`
- [UV](https://docs.astral.sh/uv/) package manager
- A **Google Gemini API key** (or swap for another supported LLM)

### 1. Clone the Repository

```bash
git clone https://github.com/a-r-ashik/ai-framework-vault.git
cd ai-framework-vault/research_and_blog_crew
```

### 2. Install UV (if not already installed)

```bash
pip install uv
```

### 3. Install Dependencies

```bash
crewai install
# or
uv sync
```

### 4. Configure Your API Key

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Then add your key:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

### 5. Set Your Topic

Open `src/research_and_blog_crew/main.py` and update the `inputs` dictionary:

```python
inputs = {
    'topic': 'Your Topic Here',
}
```

### 6. Run the Crew

```bash
crewai run
```

The generated blog post will be saved to `blogs/` as a `.md` file.

---

## 📄 Sample Output

The included sample blog — [`blogs/ai_engineering_career_path.md`](blogs/ai_engineering_career_path.md) — was generated with:

```python
topic = "AI Engineering Career Path and Opportunities in Bangladesh 2026"
```

It covers:
- What AI Engineers do
- Bangladesh's Smart Bangladesh initiative
- Career specializations (Computer Vision, NLP, MLOps)
- Industries hiring AI Engineers
- A beginner's roadmap into the field

---

## ⚙️ Configuration Reference

### `config/agents.yaml`

Defines each agent's persona using interpolated `{topic}` variables:

```yaml
report_generator:
  role: Expert report generator on {topic}
  goal: Creating detailed report on {topic}
  backstory: >
    You are an expert researcher who has developed detailed research
    reports on various topics, covering multi-dimensional views,
    current and future trends, with good analogies.

blog_writer:
  role: Expert Blog Writer on {topic}
  goal: Creating well crafted blog on {topic}
  backstory: >
    You are an expert at creating blogs that are fun to read,
    full of facts in a simple way — even a 5-year-old can understand.
```

### `config/tasks.yaml`

Defines what each agent is asked to do:

```yaml
report_task:
  description: Generate a comprehensive ~1000-word report on {topic} with clear headings.
  expected_output: A 1000-word structured report on {topic}.
  agent: report_generator

blog_writing_task:
  description: Using the report, write a simplified ~500-word "ELI5" style blog post on {topic}.
  expected_output: A 500-word fun blog post with a creative heading.
  agent: blog_writer
```

---

## 🛠️ Extending the Project

### Add a Custom Tool

Edit `src/research_and_blog_crew/tools/custom_tool.py`:

```python
from crewai.tools import BaseTool

class MyCustomTool(BaseTool):
    name: str = "My Tool Name"
    description: str = "What this tool does — agents read this to decide when to use it."

    def _run(self, argument: str) -> str:
        # Your tool logic here
        return "tool output"
```

Then assign it to an agent in `crew.py`:

```python
from .tools.custom_tool import MyCustomTool

@agent
def report_generator(self) -> Agent:
    return Agent(
        config=self.agents_config["report_generator"],
        tools=[MyCustomTool()],
        verbose=True,
    )
```

### Switch the LLM

In `crew.py`, pass an `llm` parameter to any agent:

```python
from crewai import LLM

@agent
def report_generator(self) -> Agent:
    return Agent(
        config=self.agents_config["report_generator"],
        llm=LLM(model="openai/gpt-4o"),
        verbose=True,
    )
```

---

## 📦 Dependencies

| Package | Version | Purpose |
|---|---|---|
| `crewai[google-genai,tools]` | `1.13.0` | Core multi-agent framework + Gemini + tools |
| Python | `>=3.10, <3.14` | Runtime |
| UV | latest | Dependency management |

---

## 🗺️ Roadmap

- [ ] Add web search tool (SerperDev / Tavily) to the researcher agent
- [ ] Add Streamlit UI for topic input and live output display
- [ ] Add a third **Editor Agent** for fact-checking and tone refinement
- [ ] Support multiple output formats (HTML, PDF, Twitter thread)
- [ ] Integrate LangGraph for conditional routing between agents

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📚 Resources

- [CrewAI Documentation](https://docs.crewai.com)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewai)
- [Google Gemini API](https://ai.google.dev/)
- [UV Package Manager](https://docs.astral.sh/uv/)
- [Join CrewAI Discord](https://discord.com/invite/X4JWnZnxPb)

---

## 📝 License

This project is open-source and available under the [MIT License](../LICENSE).

---

<div align="center">
  <strong>Part of the <a href="https://github.com/a-r-ashik/ai-framework-vault">AI Framework Vault</a> — a curated collection of LangChain, LangGraph, CrewAI & Streamlit tutorials.</strong>
</div>
