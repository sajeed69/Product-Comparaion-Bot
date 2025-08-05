# Product Comparison Bot

A multi-agent AI system built with **CrewAI** that compares two products based on features and reviews, then recommends the best option. Powered by custom agents for info extraction, comparison, and recommendation, wrapped in an elegant **Streamlit** web app UI.

---

## Features

- Extracts product information (specs, reviews) using an Info Extractor agent.
- Compares products feature-by-feature via a Comparator agent.
- Recommends the best product with clear reasoning through a Recommender agent.
- Interactive, user-friendly Streamlit interface.
- Easy to extend with new agents or external data sources.

---

## Tech Stack

- [CrewAI](https://github.com/joaomdmoura/crewAI) for multi-agent orchestration
- OpenAI API for natural language understanding (API key required)
- Streamlit for the frontend UI
- Python for backend logic
- DuckDuckGo Search (placeholder for web data gathering)

---

## Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/product-comparison-bot.git
cd product-comparison-bot
