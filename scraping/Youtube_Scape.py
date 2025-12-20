from googleapiclient.discovery import build
import pandas as pd
import time
import random
from datetime import datetime, timezone
import isodate
import os
from pathlib import Path
from api_config import YouTubeAPIConfig

# Create data/raw directory if it doesn't exist
RAW_DATA_DIR = Path(__file__).parent.parent / "data" / "raw"
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Load API keys from .env file.
try:
    API_KEYS = YouTubeAPIConfig.get_api_keys()
    print(f" Loaded {len(API_KEYS)} API key(s) from .env file")
except ValueError as e:
    print(e)
    exit(1)

# Group API keys into chunks of 5
KEY_GROUPS = [API_KEYS[i:i+5] for i in range(0, len(API_KEYS), 5)]


SEARCH_QUERIES = [
    "Cooking Recipes","Travel Vlogs","Daily Vlog","Fitness Motivation",
    "Study Tips","Educational Lectures","Music Covers","Dance Tutorials",
    "Stand Up Comedy","Home Workouts",

    "Healthy Diet","Gardening Tips","Tech Reviews","Movie Reviews",
    "Gaming Walkthrough","Car Vlogs","Motivational Talks","Stock Market Analysis",
    "Yoga Sessions","Art Tutorials",

    "Sports Highlights","Book Reviews","DIY Crafts","Fashion & Style",
    "Nature Documentary","Photography Tips","Luxury Travel","Street Food Tour",
    "Mental Health Advice","Career Guidance"

    "Finance","Self Improvement",
    "History Documentaries","Science Experiments","Language Learning",
    "Database Management System","Artificial Intelligence","Machine Learning",
    "Web Development","Mobile App Development","Cloud Computing","Cybersecurity",
    "Data Science","Blockchain Technology","Internet of Things","Virtual Reality",
    "Augmented Reality","DevOps","Software Testing","UI/UX Design",

    "Digital Marketing","Social Media","Entrepreneurship",
    "Project Management","Leadership Skills","Business Analytics",
    "E-commerce","Startups","Productivity","Time Management",

    "Photography","Travel","Food Reviews","Makeup Tutorials",
    "Fitness Challenges","Tech Unboxing","Movie Trailers","Gaming Reviews",
    "Music Videos","Comedy Skits","Documentaries","DIY Projects"
]

# Break queries into chunks of 10
QUERY_GROUPS = [SEARCH_QUERIES[i:i+10] for i in range(0, len(SEARCH_QUERIES), 10)]

# Static configuration
DURATION_FILTERS = ["medium", "long"]
VIDEOS_PER_QUERY = 3000
SAFE_DELAY = (0.15, 0.45)


GLOBAL_SEEN = set()   # Prevent duplicates globally

def yt(api_key):
    return build("youtube", "v3", developerKey=api_key)

def parse_duration(duration):
    try:
        return int(isodate.parse_duration(duration).total_seconds())
    except:
        return 0

def fetch_batch(y, query, duration_filter, limit):
    results = []
    next_page = None
    count = 0

    while count < limit:
        try:
            search = y.search().list(
                q=query, type="video", part="snippet",
                maxResults=50, pageToken=next_page,
                videoDuration=duration_filter
            ).execute()

            video_ids = [
                x["id"]["videoId"] for x in search["items"]
                if x["id"]["videoId"] not in GLOBAL_SEEN
            ]

            if not video_ids:
                break

            data = y.videos().list(
                part="snippet,statistics,contentDetails,topicDetails",
                id=",".join(video_ids)
            ).execute()

            for v in data.get("items", []):
                vid = v["id"]
                s = v["snippet"]
                st = v.get("statistics", {})
                cd = v.get("contentDetails", {})

                dur = parse_duration(cd.get("duration",""))
                if dur < 60:   #  Skip Shorts
                    continue

                views = int(st.get("viewCount",0))
                if views < 1000:  #  Skip Junk
                    continue

                #  Real Topic Extraction
                topic_raw = v.get("topicDetails", {}).get("topicCategories", [])
                topic_clean = [t.split("/")[-1].replace("_"," ") for t in topic_raw]
                topic_label = topic_clean[0] if topic_clean else "Unknown"

                # Channel Data
                ch_id = s["channelId"]
                ch = y.channels().list(part="statistics,snippet", id=ch_id).execute()
                c = ch["items"][0]
                subs = int(c["statistics"].get("subscriberCount",0))
                total_vids = int(c["statistics"].get("videoCount",0))
                created = c["snippet"]["publishedAt"]
                age_days = (datetime.now(timezone.utc)-datetime.fromisoformat(created.replace("Z","+00:00"))).days

                results.append({
                    "video_id": vid,
                    "title": s.get("title",""),
                    "topic": topic_label,
                    "category_id": s.get("categoryId",""),
                    "published_at": s.get("publishedAt",""),
                    "duration_seconds": dur,
                    "video_definition": cd.get("definition",""),
                    "captions_flag": cd.get("caption",""),

                    "channel_id": ch_id,
                    "channel_title": s.get("channelTitle",""),
                    "subscriber_count": subs,
                    "total_videos": total_vids,
                    "channel_age_days": age_days,

                    "views": views,
                    "likes": int(st.get("likeCount",0)),
                    "comments": int(st.get("commentCount",0)),
                })

                GLOBAL_SEEN.add(vid)
                count += 1

            next_page = search.get("nextPageToken")
            if not next_page:
                break

            time.sleep(random.uniform(*SAFE_DELAY))

        except Exception as e:
            print("Error:", e)
            break

    return results

# ========================================================
# MAIN SCRAPING LOOP 
# ========================================================
for i, query_group in enumerate(QUERY_GROUPS):
    api_group = KEY_GROUPS[i % len(KEY_GROUPS)]
    print(f"\n Using API Key Group #{i+1}\n")
    for query in query_group:
        for d in DURATION_FILTERS:
            print(f"\n Query: {query} | Duration: {d}")
            y = yt(random.choice(api_group))
            batch = fetch_batch(y, query, d, VIDEOS_PER_QUERY)

            df = pd.DataFrame(batch)
            filename = f"{query.replace(' ','_')}_{d}.csv"
            filepath = RAW_DATA_DIR / filename
            df.to_csv(filepath, index=False)

            print(f" Saved {len(df)} → data/raw/{filename}")

print("\n DONE! All category CSV files saved successfully.")
