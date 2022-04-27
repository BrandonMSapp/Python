# Might make your life easier for appending to lists
from collections import defaultdict

# Third party libraries
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, regularizers
from keras.layers import Dense, Input
from keras.models import Sequential

# Only needed if you plot your confusion matrix
import matplotlib.pyplot as plt

# our libraries
from lib.partition import split_by_day
import lib.file_utilities as util
from lib.buildmodels import build_model
# Any other modules you create


def dolphin_classifier(data_directory):
    """
    Neural net classification of dolphin echolocation clicks to species
    :param data_directory:  root directory of data
    :return:  None
    """

    ggFile = util.get_files('/Users/ikepalmer/CS550/dolphin_clicks/features/Gg')
    loFile = util.get_files('/Users/ikepalmer/CS550/dolphin_clicks/features/Lo')
    ggParsed = util.parse_files(ggFile)
    loParsed = util.parse_files(loFile)
    ggByDay = split_by_day(ggParsed)
    loByDay = split_by_day(loParsed)
    
    ggKeys = list()
    loKeys = list()
    for i in ggByDay.keys():
        ggKeys.append(i)
    for i in loByDay.keys():
        loKeys.append(i)
    

    ggValues = list()
    loValues = list()

    
    for i in ggByDay.keys():
        ggValues.append(ggByDay.get(i))
    for i in loByDay.keys():
        loValues.append(loByDay.get(i))
    
    
    gg_keys_train, gg_keys_test, gg_values_train, gg_values_test = train_test_split(ggKeys, ggValues)
    lo_keys_train, lo_keys_test, lo_values_train, lo_values_test = train_test_split(loKeys, loValues)


    
    gg_train_labels = np.array([])
    gg_train_examples = []
    lo_train_labels = np.array([])
    lo_train_examples = []
    gg_test_examples = []
    lo_test_examples = []
    gg_test_labels = []
    lo_test_labels = []


    for i in gg_values_train:
        for j in i[0].features:
            gg_train_labels = np.append(gg_train_labels, 0)
            gg_train_examples.append(j)

    for i in lo_values_train:
        for j in i[0].features:
            lo_train_labels = np.append(lo_train_labels, 1)
            lo_train_examples.append(j)

    for i in gg_values_test:
        for j in i[0].features:
            gg_test_labels.append(0)
            gg_test_examples.append(j)

    for i in lo_values_test:
        for j in i[0].features:
            lo_test_labels.append(1)
            lo_test_examples.append(j)

    gg_test_reshape = np.reshape(gg_test_labels, (len(gg_test_labels), 1))
    lo_test_reshape = np.reshape(lo_test_labels, (len(lo_test_labels), 1))
    gg_train_reshape = np.reshape(gg_train_labels, (len(gg_train_labels),1))
    lo_train_reshape = np.reshape(lo_train_labels, (len(lo_train_labels),1))

    labels = np.vstack((gg_train_reshape, lo_train_reshape))
    examples = np.vstack((gg_train_examples, lo_train_examples))
    testLabels = np.vstack((gg_test_reshape, lo_test_reshape))
    testExamples = np.vstack((gg_test_examples, lo_test_examples))
    
    model = Sequential()
    model.add(Input(shape=(20,)))
    model.add(Dense(100, activation='relu', kernel_regularizer=regularizers.L2(0.01)))
    model.add(Dense(100, activation='relu', kernel_regularizer=regularizers.L2(0.01)))
    model.add(Dense(1, activation='sigmoid', kernel_regularizer=regularizers.L2(0.01)))

    # model = build_model([(Dense, [100], {'activation':'relu', 'input_dim': 20}),
    #  (Dense, [100], {'activation':'relu', 'input_dim':100}),
    #  (Dense, [1], {'activation':'sigmoid', 'input_dim':100})
    # ])

    model.compile(optimizer = "Adam", loss = "binary_crossentropy", metrics = ["accuracy"])
    model.fit(examples, labels, batch_size=100, epochs=10, shuffle=True)
   
    results = model.predict(testExamples)
    print(results)
    print(testLabels)
    maxlog = 0
    for i in results:
        maxlog = maxlog + np.log(i)
    print(maxlog)

    
    plt.ion()   # enable interactive plotting

    use_onlyN = np.Inf  # debug, only read this many files for each species

    


if __name__ == "__main__":
    data_directory = "path\to\data"  # root directory of data
    dolphin_classifier(data_directory)