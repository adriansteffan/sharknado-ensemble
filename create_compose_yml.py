# TODO: Format compose file according to model_names_active

DOCKER_COMPOSE_VERSION = "3.3"

models = open("models_active.txt","r").read().splitlines()

with open('docker-compose.yml','w') as dc_yml:
    dc_yml.write("version: '"+DOCKER_COMPOSE_VERSION+"'\n\nservices:\n")
    for name in models:
        dc_yml.write("    "+name+":\n        image: docker-"+name+"\n\n        volumes:\n            - ${PWD}/data:/home/"+name+"/data\n            - ${PWD}/out:/home/"+name+"/out\n\n")
    

    
