import internetarchive as ia
import pandas as pd
import time
import os

def fetch_top_bands():
    """Fetch ALL etree records to find true top 50 bands"""
    print("🎵 Fetching ALL concerts from Archive.org (this takes ~10-15 min)...")
    
    search = ia.search_items(
        'collection:etree',
        fields=['identifier', 'creator', 'title', 'date', 'downloads', 'venue']
    )
    
    results = []
    count = 0
    
    for item in search:
        count += 1
        
        # Show progress every 1,000 items
        if count % 1000 == 0:
            print(f"  ⏳ Processed {count:,} items...")
        
        creator = item.get('creator')
        if creator and isinstance(creator, list):
            creator = creator[0]
        if creator and creator.strip():
            results.append({
                'identifier': item['identifier'],
                'creator': creator.strip(),
                'title': item.get('title', 'Unknown'),
                'date': item.get('date', 'Unknown'),
                'downloads': item.get('downloads', 0),
                'venue': item.get('venue', 'Unknown')
            })
        time.sleep(0.01)  # Be polite to API
    
    df = pd.DataFrame(results)
    print(f"  ✅ Total items fetched: {len(df):,}")
    
    # Now get TRUE top 50 bands
    num_bands = 50
    top_bands = df['creator'].value_counts().head(num_bands).index.tolist()
    filtered_df = df[df['creator'].isin(top_bands)]
    
    return filtered_df

if __name__ == "__main__":
    df = fetch_top_bands()
    output_path = os.path.join('..', 'data', 'live_music_archive.csv')
    df.to_csv(output_path, index=False)
    print(f"✅ Success! Saved {len(df):,} shows to {output_path}")
    print(f"📀 Unique bands: {df['creator'].nunique()}")