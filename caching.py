import redis
import os
from dotenv import load_dotenv
import json

load_dotenv()

redis_hostname = os.getenv("HOST")
redis_port = os.getenv("PORT")
redis_db = os.getenv("DB")
key_value = "weather_data"

r = redis.StrictRedis(
    host=redis_hostname,
    port=redis_port,
    db=redis_db,
    decode_responses=True
)


def cache_to_redis(data):
    r.lpush(key_value, json.dumps(data))
    r.expire(key_value, 60*30)



def get_cache_data():
    stored_data = [json.loads(item) for item in r.lrange(key_value, 0, -1)]
    return stored_data    

def clear_recent_data():
    r.delete(key_value)
    