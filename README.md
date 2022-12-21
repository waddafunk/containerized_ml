# containerized_ML

Experiments to containerize a Machine Learning algorithm and serve its prediction as an API using Docker and Flask

## Quickstart

* Clone the repository
* `cd app`
* `docker build -t myimage .` Here `myimage` can be substituted with any name you want to give the image (substitute also in later passages).
* `docker run --gpus all  -d -p 5000:5000 myimage` run the image with GPU acceleration
* `curl http://localhost:5000/tf_check` will print the available physical devices

Add the services you want to add editing `app/server.py` Additional python libraries must be installed by editing `app/requirements.txt`.

When modifying the code or installing python packages the *build/run* process above must be repeated in order for changes to take place. 
