import jsonlines
import os
import random
from textstat.textstat import textstat
import numpy as np


# seed to shuffle the list of instances and truths
SEED = 473

# share of items used for training
TRAIN_TO_VAL_RATIO = 0.8

# dictionary containing lists of instances, truths and wordtypes
DATA = None  # {'instances': , 'truths': , 'wordtypes': , 'judgements': }


def read_data():

    global DATA

    dirname = os.path.dirname(__file__)
    data_path = os.path.join(dirname, '..','data')

    # Read files to retrieve lists of instance and truth dictionaries.
    instances_file_path = os.path.join(data_path, 'instances_sorted.jsonl')
    truths_file_path = os.path.join(data_path, 'truths_sorted.jsonl')
    wordtypes_file_path = os.path.join(data_path, 'wordtypes_sorted.jsonl')
    # judgements_file_path = os.path.join(data_path, 'judgements_sorted.jsonl')

    instances_reader = jsonlines.open(instances_file_path)
    truths_reader = jsonlines.open(truths_file_path)
    wordtypes_reader = jsonlines.open(wordtypes_file_path)
    # judgements_reader = jsonlines.open(judgements_file_path)

    instances_list = [instance for instance in instances_reader]
    truths_list = [truth for truth in truths_reader]
    wordtypes_list = [wordtypes for wordtypes in wordtypes_reader]
    judgements_list = [0 for instance in instances_list]  # [judgements for judgements in judgements_reader]

    # Combine lists to a list of tuples containing an instance and a truth dictionary.
    data_list = [(instance, truth, wordtypes, judgements)
                 for instance, truth, wordtypes, judgements
                 in zip(instances_list, truths_list, wordtypes_list, judgements_list)]

    # Shuffle list.
    random.seed(SEED)
    random.shuffle(data_list)

    # Remove broken instances.
    data_cleaned = []
    for (instance, truth, wordtypes, judgements) in data_list:
        if len(instance['postText'][0]) > 0 and textstat.lexicon_count(instance['postText'][0], True):
            data_cleaned += [(instance, truth, wordtypes, judgements)]

    # Part list into lists of instances and truths.
    instances_cleaned = [instance for (instance, truth, wordtypes, judgements) in data_cleaned]
    truths_cleaned = [truth for (instance, truth, wordtypes, judgements) in data_cleaned]
    wordtypes_cleaned = [wordtypes for (instance, truth, wordtypes, judgements) in data_cleaned]
    judgements_cleaned = [judgements for (instance, truth, wordtypes, judgements) in data_cleaned]

    DATA = {'instances': instances_cleaned,
            'truths': truths_cleaned,
            'wordtypes': wordtypes_cleaned,
            'judgements': judgements_cleaned}


def get_instances():

    if DATA is None:
        read_data()

    return DATA['instances']


def get_truths():

    if DATA is None:
        read_data()

    return DATA['truths']


def get_wordtypes():

    if DATA is None:
        read_data()

    return DATA['wordtypes']


def get_judgements():
    if DATA is None:
        read_data()

    return DATA['judgements']


def split_train_val(lst):

    train = lst[:int(len(lst) * TRAIN_TO_VAL_RATIO)]
    val = lst[int(len(lst) * TRAIN_TO_VAL_RATIO):]

    return train, val


def split_train_val_df(dataframe):

    train = dataframe.iloc[ :int(dataframe.shape[0] * TRAIN_TO_VAL_RATIO), :]
    val = dataframe.iloc[ int(dataframe.shape[0] * TRAIN_TO_VAL_RATIO):,:]

    return train, val


def load_glove_model():
    """
    Danke Stackoverflow https://stackoverflow.com/questions/37793118/load-pretrained-glove-vectors-in-python
    """

    dirname = os.path.dirname(__file__)
    data_path = os.path.join(dirname,'..','data')
    
    glovePath = os.path.join(data_path, 'glove.6B.100d.txt')
    print("Loading Glove Model")
    f = open(glovePath, 'r', encoding="utf8")
    model = {}
    for line in f:
        splitLine = line.split()
        word = splitLine[0]
        embedding = np.array([float(val) for val in splitLine[1:]])
        model[word] = embedding
    print ("Done.",len(model)," words loaded!")
    return model


def create_embedding_matrix(embedding):
    embedding_matrix = np.zeros((len(embedding.keys()) + 1, 100)) # glove6B.100d.txt => 100 dim
    i = 0
    for word in embedding.keys():
        embedding_vector = embedding.get(word)
        if embedding_vector is not None:
            # words not found in embedding index will be all-zeros.
            embedding_matrix[i] = embedding_vector
        ++i
    return embedding_matrix

def load_instances_from(path):
    instances_reader = jsonlines.open(path)
    instances_list = [instance for instance in instances_reader]
    instances = [i for i in instances_list if len(i['postText'][0]) > 0 and textstat.lexicon_count(i['postText'][0], True)]
    return instances

