from flask import Flask
import tensorflow as tf
server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello World!\n"

@server.route("/tf_check")
def list_GPUs():
    return tf.config.list_physical_devices()

if __name__ == "__main__":
   server.run(host='0.0.0.0')