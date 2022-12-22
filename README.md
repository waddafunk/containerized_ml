# containerized_ml

Template to containerize a Tensorflow Machine Learning algorithm and serve its predictions as an API using Docker and Flask.

## Quickstart

* `git clone https://github.com/waddafunk/containerized_ml.git`.
* `cd containerized_ml/app`
* `docker compose up`
* `curl http://localhost:8000/cache_check` will print how many times the url has been visited
* `curl http://localhost:8000/tf_check` will print available resources

Add the services you want to add editing `app/server.py`. Additional python libraries must be installed by editing `app/requirements.txt`.

Could fail if no NVIDIA GPUs are present on the machine.
