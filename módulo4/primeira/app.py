import time
import redis
import os
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host=os.environ["REDIS_HOST"], port=os.environ["REDIS_PORT"])

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Olá alunos ADS17! Eu fui visto {} vezes.\n'.format(count)