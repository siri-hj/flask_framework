from redis import Redis
from config import Config


redis_store = Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=0)