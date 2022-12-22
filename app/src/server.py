from flask import Flask
import tensorflow as tf
import redis
import time

print(__name__)
server = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

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

@server.route("/")
def hello():
    return "Hello World!\n"

@server.route("/tf_check")
def list_GPUs():
    return tf.config.list_physical_devices()

@server.route("/cache_check")
def get_hits():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    print('Starting server...')
    server.run(host='0.0.0.0')


