import internetarchive as ia
import pandas as pd
import time
import os

def fetch_all_shows(max_items=20000):
    """Fetch shows from Archive.org without filtering by band popularity"""
    print(f"🎵 Fetching up to {max_items:,} shows from Archive.org...")
    
    search = ia.search_items(
        'collection:etree',
        fields=['identifier', 'creator', 'title', 'date', 'downloads', 'venue']
    )
    
    results = []
    count = 0
    
    for item in search:
        count += 1
        
        # Stop after max_items to keep it reasonable
        if count > max_items:
            print(f"  🛑 Stopped after {max_items:,} items.")
            break
            
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
        time.sleep(0.01)
    
    df = pd.DataFrame(results)
    print(f"  ✅ Total items fetched: {len(df):,}")
    print(f"  📀 Unique bands: {df['creator'].nunique()}")
    
    return df

if __name__ == "__main__":
    df = fetch_all_shows(max_items=20000)
    output_path = os.path.join('..', 'data', 'live_music_archive.csv')
    df.to_csv(output_path, index=False)
    print(f"✅ Success! Saved {len(df):,} shows to {output_path}")