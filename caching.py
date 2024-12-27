import redis
import os

redis_hostname = os.getenv("HOSTNAME")
redis_port = os.getenv("PORT")
redis_db = os.getenv("DB")

r = redis.Redis(
    host=redis_hostname,
    port=redis_port,
    db=redis_db
)