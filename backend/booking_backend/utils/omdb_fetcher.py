"""This module handles fetching movie data from the OMDb API.
It integrates Redis for caching and rate limiting to prevent excessive external API calls.

Functions:
- fetch_random_movie(): Fetches a single random movie from a random franchise title using OMDb.
- is_rate_limited(): Checks and enforces API rate limits using Redis.
- rate_limited request(): Checks if the requests rate exceeds the quote and prevent overloading
"""


import random
import os
import time
import json
import requests
import redis

OMDB_API_KEY = os.getenv("OMDB_API_KEY")
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.environ.get("REDIS_DB", 0))
REDIS_EXPIRE = int(os.environ.get("REDIS_CACHE_EXPIRE_SECONDS", 600))

# Redis client
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)

# Rate limiting config
last_request_time = 0
RATE_LIMIT_SECONDS = 1

#Franchise titles to get a few results and randomize them
FRANCHISES = [
    "Mission Impossible", "Harry Potter", "Star Wars",
    "Avengers", "Batman"
]

def is_rate_limited(key: str, limit: int, period: int) -> bool:
    """
    Returns True if the request should be limited, False otherwise.
    """
    current = int(time.time())
    window_key = f"rate:{key}:{current // period}"

    count = redis_client.incr(window_key)
    if count == 1:
        redis_client.expire(window_key, period)

    return count > limit

def rate_limited_request(url):
    global last_request_time
    elapsed = time.time() - last_request_time
    if elapsed < RATE_LIMIT_SECONDS:
        time.sleep(RATE_LIMIT_SECONDS - elapsed)
    response = requests.get(url, timeout=5)
    last_request_time = time.time()
    return response

def fetch_random_omdb_movie():
    if is_rate_limited("omdb_api", limit=1, period=1):
        time.sleep(1)

    franchise = random.choice(FRANCHISES)
    res = rate_limited_request(f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&s={franchise}")
    data = res.json()

    if data.get("Response") == "True" and "Search" in data:
        choice = random.choice(data["Search"])
        imdb_id = choice.get("imdbID")
        if imdb_id:
            cached = redis_client.get(imdb_id)
            if cached:
                return json.loads(cached)

            if is_rate_limited("omdb_api", limit=1, period=1):
                time.sleep(1)

            detail_url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&i={imdb_id}"
            detail_res = requests.get(detail_url, timeout=5)
            detail = detail_res.json()
            if detail.get("Response") == "True":
                movie = {
                    "title": detail["Title"],
                    "description": detail.get("Plot", ""),
                    "runtime": detail.get("Runtime", ""),
                    "poster": detail.get("Poster", ""),
                    "year": detail.get("Year", "")
                }
                redis_client.setex(imdb_id, REDIS_EXPIRE, json.dumps(movie))
                return movie

    return None
