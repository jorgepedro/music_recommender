# Live Music Concert Recommender

A concert discovery app that helps users find live music recordings from the [Internet Archive's Live Music Archive](https://archive.org/details/etree).

## Features

- Browse concerts from 50+ popular bands
- Filter by year, venue, and popularity
- Direct links to listen on Archive.org
- Built with Python, Streamlit, and Internet Archive API

## Tech Stack

- **Python** - Core programming language
- **Streamlit** - Web app interface
- **Pandas** - Data manipulation
- **Internet Archive API** - Concert metadata
- **Git/GitHub** - Version control

##  Project Structure

music_recommender/
├── data/ # Downloaded concert metadata
├── src/ # Data fetching scripts
├── app/ # Streamlit application
├── requirements.txt # Python dependencies
└── README.md # This file


## How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/jorgepedro/music_recommender.git
cd music_recommender

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

### 3. Install Dependencies
```bash
pip install -r requirements.txt

### 4. Fetch Data
```bash
cd src
python fetch_data.py

### 5. Run App
```bash
cd src
python fetch_data.py

## Data Source
- All concert metadata is fetched from the Internet Archive Live Music - Archive, a collection of over 100,000+ free live concert recordings.

## Current Status
- Project setup complete
- Data fetching script created
- Streamlit app in development
- Deployment to Streamlit Cloud

## What I Learned
- How to work with the Internet Archive API
- Building ETL pipelines (Extract, Transform, Load)
- Streamlit app development
- Git version control best practices

## Next Steps
-Add recommendation algorithm ("If you like X, try Y")
-Implement full-text search for venues
-Add visualization (concerts per year, popular venues)
-Deploy to Streamlit Cloud