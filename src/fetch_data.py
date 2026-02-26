import internetarchive as ia
import pandas as pd
import time
import os

def fetch_top_bands(max_items=5000):
    """Fetch a sample of shows to find popular bands quickly"""
    print(f"🎵 Fetching up to {max_items} shows from Archive.org...")
    
    # Search etree collection (no sorting parameter to avoid API errors)
    search = ia.search_items(
        'collection:etree',
        fields=['identifier', 'creator', 'title', 'date', 'downloads', 'venue']
    )
    
    results = []
    count = 0
    
    for item in search:
        count += 1
        
        # Stop early if we have enough data
        if count > max_items:
            print(f"  🛑 Stopped after {max_items} items (enough for demo).")
            break
            
        if count % 500 == 0:
            print(f"  Processed {count} items...")
        
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
        time.sleep(0.02)
    
    # Convert to DataFrame
    df = pd.DataFrame(results)
    print(f"  Total items fetched: {len(df)}")
    
    if len(df) == 0:
        print("❌ Error: No data found!")
        return None

    # Filter to top N bands by show count within our sample
    num_bands = 50
    top_bands = df['creator'].value_counts().head(num_bands).index.tolist()
    filtered_df = df[df['creator'].isin(top_bands)]
    
    return filtered_df

if __name__ == "__main__":
    df = fetch_top_bands(max_items=5000)
    
    if df is not None:
        output_path = os.path.join('..', 'data', 'live_music_archive.csv')
        df.to_csv(output_path, index=False)
        print(f"✅ Success! Saved {len(df)} shows to {output_path}")
        print(f"📀 Unique bands: {df['creator'].nunique()}")