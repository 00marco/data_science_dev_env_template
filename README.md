# FAQ
### How do build the Docker container?
    - create Dockerfile
    - cd to project folder
    - run:
        sudo docker build -t socmed_ml_pipeline -f socmed_ml_pipeline.Dockerfile .
        sudo docker system prune

### How do I run commands in this container?
    - sudo docker run --rm {{insert command}}
    - sudo docker run --rm --mount "type=bind,source=$(pwd),target=/src" socmed_ml_pipeline {{insert command}}

### How do I update the installed dependencies?
    - open Docker container terminal
    - install desired package
    - pip freeze to requirements.txt (inside this project folder)
    - rebuild docker container

### How do I run the docker container bash?
    - sudo docker run --rm --entrypoint=/bin/bash --memory-swap=-1 --mount "type=bind,source=$(pwd),target=/src" -it socmed_ml_pipeline

### I want to experiment on something -- how do I open a Jupyter notebook instance?
    - Run docker container bash terminal while exposing desired port (eg 8888)
        sudo docker run --rm -p 8888:8888 --entrypoint=/bin/bash --memory-swap=-1 --mount "type=bind,source=$(pwd),target=/src" -it socmed_ml_pipeline
    - Open Jupyter notebook instance
        jupyter notebook --port=8888 --ip=0.0.0.0 --allow-root
    - File > Jupytext > pair Notebook with light script
    - Python script should be automatically generated every time you make changes to your Jupyter notebook.
    - You can also just open the py file and an ipynb notebook will automatically be generated
    - To be safe, just move to the ipynb file

