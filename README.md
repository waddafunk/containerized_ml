# containerized_ml

Template to containerize a Machine Learning algorithm and serve its predictions as an API using Docker and Flask.

## Quickstart

* `git clone https://github.com/waddafunk/containerized_ml.git`.
* `cd containerized_ml/app`
* `docker compose up`

Add the services you want to add editing `app/server.py`. Additional python libraries must be installed by editing `app/requirements.txt`.
