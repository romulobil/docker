from flask import Flask
import os
import redis

app = Flask(__name__)
redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = int(os.environ.get("REDIS_PORT", 6379))

cache = redis.Redis(host=redis_host, port=redis_port)

@app.route('/')
def visit_counter():
    visits = cache.incr('visits')
    return f"Esta página foi visitada {visits} vezes."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
