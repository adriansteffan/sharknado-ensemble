# Sharknado Ensemble

## Prerequisites

The ensemble was developed and tested on a Ubuntu 18.04, so it is strongly recommend that you use that.

Recent versions of the following packages are required to run this project:
```
python3 
docker
docker-compose
```


# Quick setup 

1. Clone this repository and cd into the root directory
2. Run
    ``` 
    ./setup_first.sh 
    ```
3. Download the prebuilt docker images from [TODO] and place the tar into the root of the project
4. Put your dataset into the "data" directory (download the datasets from [the official challange page](https://www.clickbait-challenge.org/))
5. Choose the models for the ensemble and put their names into [models_active.txt](models_active.txt).
6.  Run
    ``` 
    ./setup_second.sh 
    ```
7. TODO


# Detailed Setup
## Using the prebuilt docker images

#TODO

## Creating the docker images from the competition VMs

This repository holds the files required to build your own dockerfiles if you have acess to the Clickbait 2017 VMS on [TIRA](https://www.tira.io/task/clickbait-detection/). They are located in their corresponding folders in [image-buildfiles](image-buildfiles). 
Replace "VMNAME" with the username of the entry you are trying to containerize.

1. Download the /home/VMNAME folder from the VM
2. copy the contents of the image-buildfiles/VMNAME into the downloaded folder
3. Run
    ```
    docker build -t docker-VMNAME .
    ```
4. (Optional) You can package the image by using
    ```
    docker save -o VMNAME-image docker-VMNAME
    ```





## Creating the docker-compose.yml

Choose the models for the ensemble and put their names into [models_active.txt](models_active.txt).

After that, run
```
python3 create_compose_yml.py
```

## Training the ensemble
## Using the classifier

Create a "data" directory in the root of the project and add your instances.jsonl and the media directory (download them from [the challange page](https://www.clickbait-challenge.org/)).

Creat a directory called "out" in the root of the project. 