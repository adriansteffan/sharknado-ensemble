import os
import sys
import jsonlines
import pandas
import helper.data
import pprint
from sklearn.metrics import mean_squared_error, accuracy_score, recall_score , precision_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import LinearSVR
from sklearn.externals import joblib
import subprocess


DOCKER_COMPOSE_VERSION = "3.3"


def print_evaluation(y_prediction, y_test, model_name):
    print(model_name+" MSE: %.7f" % mean_squared_error(y_test['truth_mean'], y_prediction))
    truth_classes = [0 if t < 0.5 else 1 for t in y_prediction]
    print(model_name+" Acc: %.7f" % accuracy_score(y_test['truth_class'], truth_classes))
    print(model_name+" Precision: %.7f" % precision_score(y_test['truth_class'], truth_classes))
    print(model_name+" Recall: %.7f" % recall_score(y_test['truth_class'], truth_classes))

dataset = {}



keys = open("models_active.txt","r").read().splitlines()

if (len(sys.argv) != 2 or sys.argv[1] == "-e"):
    with open('docker-compose.yml','w') as dc_yml:
        dc_yml.write("version: '"+DOCKER_COMPOSE_VERSION+"'\n\nservices:\n")
        for name in keys:
            dc_yml.write("    "+name+":\n        image: docker-"+name+"\n\n        volumes:\n            - ${PWD}/data:/home/"+name+"/data\n            - ${PWD}/out:/home/"+name+"/out\n\n")
        

    subprocess.run(["docker-compose", "up"])


if (len(sys.argv) != 2 or sys.argv[1] == "-t"):
    
    for key in keys:
        with jsonlines.open("out/"+key+"/results.jsonl", 'r') as fp:
            data = list(fp)
            dataset[key] = [post['clickbaitScore'] for post in data]


    df = pandas.DataFrame(dataset, columns=keys)

    truth_values = dict()
    truth_values['truth_mean'] = list()
    truth_values['truth_class'] = list()

    with jsonlines.open("data/truth.jsonl", 'r') as fp:
        for truth in fp:
            truth_values['truth_mean'].append(truth['truthMean'])
            truth_values['truth_class'].append(1 if truth['truthClass'] == "clickbait" else 0)


    data_X = df.astype(float)
    data_Y = pandas.DataFrame(truth_values, columns=["truth_mean", "truth_class"]).astype(float)
    #print(df.shape[0])
    #print(data_X.shape[0])


    X_train, X_test = helper.data.split_train_val_df(data_X)
    y_train, y_test = helper.data.split_train_val_df(data_Y)


    # Training and evaluation

    print("Fitting Random Forest Regressor...")
    ranforestregr = RandomForestRegressor(max_depth=20, random_state=2, n_estimators=400, n_jobs=-1)
    ranforestregr.fit(X_train, y_train['truth_mean'])

    print("Fitting Support Vector Machine...")
    svm = LinearSVR(C=0.1, loss='squared_epsilon_insensitive', dual=False, random_state=1)
    svm.fit(X_train, y_train['truth_mean'])

    print("Predicting...")
    random_forest_y_pred = ranforestregr.predict(X_test)
    svm_y_pred = svm.predict(X_test)

    print("Saving Models...")
    joblib.dump(ranforestregr, 'sharknado_models/clickbait_random_forest_regressor.pkl')
    joblib.dump(svm, 'sharknado_models/clickbait_svm.pkl')

    # Print features sorted by importance for the Random Forest Regressor

    pp = pprint.PrettyPrinter(indent=2)
    features = dict(zip(data_X.columns.values, ranforestregr.feature_importances_))
    features_sorted = sorted(features.items(), key=lambda x:x[1])
    pp.pprint(features_sorted)


    print_evaluation(random_forest_y_pred,y_test,"Random Forest Regressor")
    print_evaluation(svm_y_pred,y_test,"SVM")

