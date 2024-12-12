""""""
import random

"""  		  	   		 	   		  		  		    	 		 		   		 		  
Test a learner.  (c) 2015 Tucker Balch  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	   		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		 	   		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	   		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		 	   		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		 	   		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		 	   		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   		  		  		    	 		 		   		 		  
or edited.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		 	   		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		 	   		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	   		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		 	   		  		  		    	 		 		   		 		  
"""  		  	   		 	   		  		  		    	 		 		   		 		  
import sys
import math  		  	   		 	   		  		  		    	 		 		   		 		  

  		  	   		 	   		  		  		    	 		 		   		 		  
import numpy as np  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import LinRegLearner as lrl
import DTLearner as dtl
import RTLearner as rtl
import BagLearner as bl
import InsaneLearner as il
import matplotlib.pyplot as plt
import time


def resample(data_x, data_y):

    subsample_x = np.empty((0, data_x.shape[1]))
    subsample_y = np.array([])
    resample = int(0.6 * data_x.shape[0])
    for z in range(resample):
        random_row = np.random.randint(0, data_x.shape[0])


        subsample_x = np.vstack((subsample_x, data_x[random_row, :]))
        subsample_y = np.append(subsample_y, data_y[random_row])

    return subsample_x, subsample_y

if __name__ == "__main__":

    if len(sys.argv) != 2:

        # print("Usage: python LinRegLearner.py <filename>")
        sys.exit(1)
    #data cleaning specifically for istanbul.csv
    np.random.seed(903967530)
    inf = open(sys.argv[1])
    data = np.array([])

    file = inf.readlines()

    arr = []
    for i in range(1, len(file)):


        tmp = list(map(float, file[i].strip().split(',')[1:]))

        arr.append(tmp)
    data = np.array(arr)





# compute how much of the data is training and testing

    train_rows = int(0.6 * data.shape[0])
    test_rows = data.shape[0] - train_rows

    # separate out training and testing data
    train_x = data[:train_rows, 0:-1]
    train_y = data[:train_rows, -1]
    print(train_x.shape)
    print(train_y.shape)


    test_x = data[train_rows:, 0:-1]
    test_y = data[train_rows:, -1]

    '''
    SHUFFLE THE DATA 1 time
    '''
    train_x, train_y = resample(train_x, train_y)
    test_x, test_y = resample(test_x, test_y)


    '''
    
    Experiment 1
    
    '''
    leaf_sizes = []
    rmse_records_in = []
    rmse_records_out = []

    for i in range(1, 80):
        learner = dtl.DTLearner(leaf_size = i)
        learner.add_evidence(train_x, train_y)  # train it

        #insample calcs
        pred_y = learner.query(train_x)
        rmse_in = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])


        rmse_records_in.append(rmse_in)
        leaf_sizes.append(i)

        #out of sample calc

        pred_y = learner.query(test_x)
        rmse_out = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
        rmse_records_out.append(rmse_out)



    plt.plot(leaf_sizes, rmse_records_in, label = "In-sample RMSE")
    plt.plot(leaf_sizes, rmse_records_out, label = "Out-sample RMSE")
    plt.legend()
    plt.title('DTLearner Across Various Leaf Sizes')

    # plt.text(100, 0.008, 'tcheng99@gatech.edu', fontsize=40, color='gray', rotation=10)
    plt.xlim(80, 0)
    plt.xlabel('Leaf Size')
    plt.ylabel('Sample RMSE')

    plt.savefig('exp1.png')
    plt.close()

    '''
    Experiment 2
    '''

    leaf_sizes = np.array([])
    rmse_records_in = np.array([])
    rmse_records_out = np.array([])

    learners = []
    for k in range(80):

        learner = bl.BagLearner(learner = dtl.DTLearner, kwargs = {"leaf_size":k}, bags = 20, boost = False, verbose = False)
        learner.add_evidence(train_x, train_y)  # train it
        learners.append(learner)

    for i in range(80):
        learner = learners[i]
        pred_y = learner.query(train_x)
        rmse_in = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])

        rmse_records_in = np.append(rmse_records_in, rmse_in)
        leaf_sizes = np.append(leaf_sizes, i)

        pred_y = learner.query(test_x)
        rmse_out = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])

        rmse_records_out = np.append(rmse_records_out, rmse_out)

    plt.plot(leaf_sizes, rmse_records_in, label="In-sample RMSE")
    plt.plot(leaf_sizes, rmse_records_out, label="Out-sample RMSE")
    plt.legend()
    plt.title('Evaluating Bagging Performance Across RMSE')
    plt.xlim(80, 0)
    plt.xlabel('Leaf Size')
    plt.ylabel('Sample RMSE')

    plt.savefig('exp2.png')
    plt.close()

    '''
    experiment 3
    '''
    #https://pythonhow.com/how/measure-elapsed-time-in-python/
    train_x, train_y = resample(train_x, train_y)
    test_x, test_y = resample(test_x, test_y)


    '''
    experiment 3a - Time to build
    '''

    #np metod
    leaf_sizes = np.empty((1, 80))
    build_times = np.empty((2, 80), dtype = float)
    learners = np.empty((2, 80), dtype = object) #row 1 = DT, row 2 = RT

    # model inits
    for i in range(80):
        #leaf sie

        leaf_sizes[0, i] = i
        # DT learner setup
        learner = dtl.DTLearner(leaf_size=i)
        start_time = time.time()
        learner.add_evidence(train_x, train_y)
        end_time = time.time()
        learners[0, i] = learner

        time_diff = end_time - start_time
        build_times[0, i] = time_diff

        #RT learner setup

        learner = rtl.RTLearner(leaf_size=i)
        start_time = time.time()
        learner.add_evidence(train_x, train_y)
        end_time = time.time()
        learners[1, i] = learner

        time_diff = end_time - start_time
        build_times[1, i] = time_diff


    #Training models

    plt.plot(leaf_sizes[0, :], build_times[0, :], label = 'dtlearner')
    plt.plot(leaf_sizes[0, :], build_times[1, :], label='rtlearner')
    plt.legend()
    plt.title('Comparing Random Tree vs. Decisions Based on Tree Building Times')
    plt.xlabel('Leaf Sizes')
    plt.ylabel('Time to build decision tree')
    plt.xlim(80, 0)

    plt.savefig('exp3_build_time.png')
    plt.close()

    '''
    experiment 3b - mean absolute error
    '''

    # np metod
    leaf_sizes = np.empty((1, 50))
    maes = np.empty((4, 50), dtype=float)
    '''
    row 1 - DT - in sample mae
    row 2 -  DT out sample
    row 3 -  RT in smaple mae
    row 4 -  RT out of sample mae
    '''


    learners = np.empty((2, 50), dtype=object)  # row 1 = DT, row 2 = RT

    # model inits
    for i in range(50):
        # leaf sie

        leaf_sizes[0, i] = i
        # DT learner setup
        learner = dtl.DTLearner(leaf_size=i)
        learner.add_evidence(train_x, train_y)
        learners[0, i] = learner



        # RT learner setup

        learner = rtl.RTLearner(leaf_size=i)
        learner.add_evidence(train_x, train_y)
        learners[1, i] = learner

    #predictions

    for i in range(50):
        #Dt insample
        y_pred = learners[0, i].query(train_x)
        mae = (np.sum(np.absolute((train_y-y_pred)))) / train_y.shape[0] #true values - pred values

        maes[0, i] = mae

        #dt out of sample
        y_pred = learners[0, i].query(test_x)
        mae = (np.sum(np.absolute((test_y - y_pred)))) / test_y.shape[0]  # true values - pred values

        maes[1, i] = mae

        # rt insample
        y_pred = learners[1, i].query(train_x)
        mae = (np.sum(np.absolute((train_y - y_pred)))) / train_y.shape[0]  # true values - pred values

        maes[2, i] = mae

        # rt out of sample
        y_pred = learners[1, i].query(test_x)
        mae = (np.sum(np.absolute((test_y - y_pred)))) / test_y.shape[0]  # true values - pred values

        maes[3, i] = mae

    plt.plot(leaf_sizes[0, :], maes[0, :], label = 'DT In-sample MAE')
    plt.plot(leaf_sizes[0, :], maes[1, :], label='DT Out-sample MAE', linestyle = '--')
    plt.plot(leaf_sizes[0, :], maes[2, :], label='RT In-sample MAE')
    plt.plot(leaf_sizes[0, :], maes[3, :], label='RT Out-sample MAE', linestyle = '--')
    plt.title('RTLearner vs. DTLearner MAE Comparison')
    plt.xlim(50, 0)
    plt.ylabel('Sample MAE')
    plt.xlabel('Leaf Size')
    plt.legend()

    plt.savefig('exp3_mae.png')