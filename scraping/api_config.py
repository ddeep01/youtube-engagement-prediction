import os
from dotenv import load_dotenv

load_dotenv()


class YouTubeAPIConfig:
    @staticmethod
    def get_api_keys():
        keys = []
        i = 1
        while True:
            key = os.getenv(f"YOUTUBE_API_KEY_{i}")
            if not key:
                break
            keys.append(key.strip())
            i += 1

        if not keys:
            single = os.getenv("YOUTUBE_API_KEY")
            if single:
                keys.append(single.strip())

        if not keys:
            raise ValueError("No YouTube API keys found. Add YOUTUBE_API_KEY or YOUTUBE_API_KEY_1 to .env.")

        return keys
