import streamlit as st
import pandas as pd
import os

st.title("🎵 Live Music Concert Recommender")

# Load data with correct path
@st.cache_data
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, '..', 'data', 'live_music_archive.csv')
    return pd.read_csv(csv_path)

df = load_data()

st.write(f"📊 Loaded {len(df)} concerts from {df['creator'].nunique()} bands")

# Band selector
selected_band = st.selectbox("Select a band", sorted(df['creator'].unique()))

# Filter by selected band
filtered_df = df[df['creator'] == selected_band]

st.write(f"### {selected_band} - {len(filtered_df)} concerts")

# Show concerts table
st.dataframe(filtered_df[['date', 'title', 'venue', 'downloads']])

# Add listen link
st.write("### Listen on Archive.org")
for _, row in filtered_df.head(10).iterrows():
    st.write(f"🎧 [{row['title']}]({row['identifier']}) - {row['date']}")