from sklearn.externals import joblib
import helper.data
import os
import jsonlines
import sys
import pandas
import subprocess

if __name__ == "__main__":

    if len(sys.argv) == 1:
        output_path = "results.json"
    else:
        output_path = sys.argv[1]+"/results.json"

        
    
    data_path = "data/"
    models_path = "sharknado_models/"
    dataset = {}
    keys = open("models_active.txt","r").read().splitlines()

    for key in keys:
        with jsonlines.open("out/"+key+"/results.jsonl", 'r') as fp:
            data = list(fp)
            dataset[key] = [post['clickbaitScore'] for post in data]


    subprocess.run(["docker-compose", "up"])
    
    df = pandas.DataFrame(dataset, columns=keys)
    data_X = df.astype(float)


    print("Predicting...")
    pred = joblib.load(models_path+"clickbait_random_forest_regressor.pkl")
    predictions = pred.predict(data_X)
    print("Finished predicting....")
    
    with jsonlines.open("data/instances.jsonl", "r") as fp:
        raw_instances = [instance for instance in fp]
    ids = [instance['id'] for instance in raw_instances]
    
    data = list()
    for i in range(0,len(ids)):
        data.append({"clickbaitScore": predictions[i], "id": ids[i]})

    with jsonlines.open(output_path, mode='w') as writer:
        writer.write(data)
