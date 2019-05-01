# Sharknado Ensemble

The sharknado is a continuation of the work we did in Greifswald at a summer academy of the German Scholarship Foundation in 2018. The aim was to develop a classifier that detects clickbaity twitter posts linking to news articles. 

Rather than processing the post itself, the sharknado consults the evaluations of all models submitted to the [Clickbait Challenge 2017](https://www.clickbait-challenge.org/) and runs a machine learning algorithm across those to classify a given post. As the competition teams used certain species of fish as the names for their models, sharknado seemed like a fitting name for this approach.

The data pipeline makes up the main portion of the project as of now: Most of the submitted models have been migrated from their competition vms to docker images. This simplifies access to the predictions they offer. The sharknado utilizes docker compose to first get the evaluation of the standalone models submitted by the competing teams and then runs a random forest regressor across those results. 

The testrun we did on the final competition evaluation data in summer 2018 outperformed the standalone models by a respectable margin and we are currently trying to replicate this in a fully functional implementation of the sharknado.

## Prerequisites

The ensemble was developed and tested on a Ubuntu 18.04, so it is strongly recommend that you use that.

Recent versions of the following packages are required to run this project:
```
python3 
python3-pip
docker
docker-compose
```

If you do not have them already, simply paste the below into your console:
```
 sudo apt-get install python3 python3-pip docker docker-compose
```


# Quick setup 

1. Clone this repository and cd into the root directory
2. Run
    ``` 
    ./setup_first.sh 
    ```
3. Download the prebuilt docker images from [TODO] and place the tar into the root of the project
4. Put your dataset into the "data" directory (download the datasets from [the official challenge page](https://www.clickbait-challenge.org/))
5. Choose the models for the ensemble and put their names into [models_active.txt](models_active.txt).



# Detailed Setup
## Using the prebuilt docker images

#TODO A bundle of the docker images will be provided as soon as an agreement is met on how and where to host it.

## (Optional) Creating the docker images from the competition VMs using premade files

This repository holds the files required to build your own docker images if you have acess to the Clickbait 2017 VMS on [TIRA](https://www.tira.io/task/clickbait-detection/). They are located in their corresponding folders in [image-buildfiles](image-buildfiles). 
( Replace "VMNAME" with the username of the entry you are trying to containerize in the next steps).

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

## (Optional) Creating your own buildfiles from the competition VMs

Alternatively, you can create the Dockerfile and the requirements.txt yourself. This is advisable if you either want to customize them or if they are simply missing from this repository.

1. SSH into the vm in question and cd into the home/VMNAME directory.
2. Create a requirements.txt, there are mainly two ways to achieve this:
    * ```pip(3) freeze > requirements.txt``` (Not recommended, as it leads to lots of unnecessary errors)
    * Using pipreqs: 
        ```
        pip(3) install pipreqs
        python(3)
        >>> import pipreqs
        >>> pipreqs.__file__
        ```
        This will print out the filepath of the package. There should be a "bin" directory on the same level as  "lib". cd in there and run
        ```
        ./pipreqs /path/to/project/root
        ```
        A tailored requirements.txt will be created at the project root. 

    (note: Some of the vms use anaconda instead of a regular python environment. Step 2 can be skipped in this case. Any errors downlaoding 2 specific files of these vms are probably caused by broken symlinks in the anaconda directory, you can savely ignore those.)

3. Choose one of the Dockerfiles in [image-buildfiles](image-buildfiles) based on the python version used and fit it to the VM you are working with. The CMD line requires the command that ultimately runs the model, you can find it on the TIRA dashboard of the VM.

After creating both of these files, you can continue the same as above and start fixing any errors that come up during the building of the docker image. Be warned though, as this step can be rather tedious.

# Preperation

Create a "data" directory in the root of the project and add your instances.jsonl and the media directory (download them from [the challange page](https://www.clickbait-challenge.org/)).

Creat the directories "out" and "sharknado_models" in the root of the project.

To install the python packages needed to run the scripts, run the following in the project root:
```
pip3 install -r requirements.txt
```

# Training the ensemble

Choose the models for the ensemble and put their names into [models_active.txt](models_active.txt).

 

After that, run 
```
python3 train.py
```

For testing purposes:

```python3 train.py -e```     
(only generates the results.json files with the ensemble)

```python3 train.py -t```   
(only trains the models without first generating results)



# Using the sharknado

Put your instances.jsonl and (optional) the media folder in the "data" directory.

Then, run 
```
python3 predict.py OUTPUTPATH
```

