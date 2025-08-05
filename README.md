# Product Comparison Bot

A multi-agent AI system built with **CrewAI** that compares two products based on features and reviews, then recommends the best option. Powered by custom agents for info extraction, comparison, and recommendation, wrapped in an elegant **Streamlit** web app UI.

---
<img width="949" height="440" alt="Product-1" src="https://github.com/user-attachments/assets/4328d499-60d9-4c8f-9a02-7bf363da85c0" />
<img width="876" height="313" alt="product-2" src="https://github.com/user-attachments/assets/695f1284-330d-4d7b-a996-e29982dba11e" />

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
