from flask import Flask
import tensorflow as tf
import tensorflow_hub as hub
import redis
import time
import librosa
import numpy as np

print(__name__)
server = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

TFLite_model_path = './lite-model_ASR_TFLite_pre_trained_models_English_1.tflite'

interpreter = tf.lite.Interpreter(model_path=TFLite_model_path)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

sample_data, _ = librosa.load('./sample.wav', sr=16000, mono=True)

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

@server.route("/predict_sample")
def predict_sample(sample=sample_data):
    interpreter.resize_tensor_input(input_details[0]["index"], sample.shape)
    interpreter.allocate_tensors()
    interpreter.set_tensor(input_details[0]["index"], sample)
    interpreter.set_tensor(
        input_details[1]["index"],
        np.array(0).astype('int32')
    )
    interpreter.set_tensor(
        input_details[2]["index"],
        np.zeros([1,2,1,320]).astype('float32')
    )
    interpreter.invoke()
    hyp = interpreter.get_tensor(output_details[0]["index"])
    return "".join([chr(u) for u in hyp])

if __name__ == "__main__":
    print('Starting server...')
    server.run(host='0.0.0.0')


