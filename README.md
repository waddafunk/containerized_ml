# containerized_ml

Template to containerize a Tensorflow Machine Learning algorithm and serve its predictions as an API using Docker and Flask.

## Quickstart

* `git clone https://github.com/waddafunk/containerized_ml.git`.
* `cd containerized_ml`
* `docker compose up`
* `curl http://localhost:8000/cache_check` will print how many times the url has been visited
* `curl http://localhost:8000/tf_check` will print available resources

Add the services you want to add editing `app/server.py`. The bind mount (line 7-8 of `docker-compose.yml`) ensures that changes in the code are automatically loaded in the Flask server without the need to tear all down and load it back up. Just edit, save, and changes will be reflected in the app. **This behaviour is for development only and must be removed before production**.

Additional python libraries must be installed by editing `app/requirements.txt`.

Could fail if no NVIDIA GPUs are present on the machine.
