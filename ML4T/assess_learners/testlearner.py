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

def print_five():
    print(5)

def resample(data_x, data_y):
    np.random.seed(0)
    subsample_x = np.empty((0, data_x.shape[1]))
    subsample_y = np.array([])
    resample = int(0.6 * data_x.shape[0])
    for i in range(resample):
        random_row = np.random.randint(0, data_x.shape[0])

        # print('random index is', random_row)

        subsample_x = np.vstack((subsample_x, data_x[random_row, :]))
        subsample_y = np.append(subsample_y, data_y[random_row])

    return subsample_x, subsample_y

if __name__ == "__main__":

    if len(sys.argv) != 2:

        print("Usage: python LinRegLearner.py <filename>")
        sys.exit(1)
    #data cleaning specifically for istanbul.csv
    inf = open(sys.argv[1])
    data = np.array([])

    file = inf.readlines()

    arr = []
    for i in range(1, len(file)):


        tmp = list(map(float, file[i].strip().split(',')[1:]))
        # float(tmp)
        arr.append(tmp)
    data = np.array(arr)


    # #code for simple csv to run
    # inf = open(sys.argv[1])
    # data = np.array(
    #     [list(map(float, s.strip().split(","))) for s in inf.readlines()]
    # )



# compute how much of the data is training and testing


    train_rows = int(0.6 * data.shape[0])
    test_rows = data.shape[0] - train_rows

    # separate out training and testing data
    train_x = data[:train_rows, 0:-1]
    train_y = data[:train_rows, -1]

    # train_x, train_y = resample(train_x, train_y)

    test_x = data[train_rows:, 0:-1]
    test_y = data[train_rows:, -1]
    # test_x, test_y = resample(test_x, test_y)
    # train_y = train_y.reshape(-1, 1)

    print(f"{test_x.shape}")
    print(f"{test_y.shape}")
    train_x, train_y = resample(train_x, train_y)
    test_x, test_y = resample(test_x, test_y)
    '''
    
    Experiment 1
    
    '''
    leaf_sizes = np.array([])
    rmse_records_in = np.array([])
    corr_records_in = np.array([])
    rmse_records_out = np.array([])
    corr_records_out = np.array([])
    # create a learner and train it
    # learner = lrl.LinRegLearner(verbose=True)  # create a LinRegLearner

    # for i in range(len(leaf_size)):
    for i in range(1, 100):
        learner = dtl.DTLearner(leaf_size = i)
        learner.add_evidence(train_x, train_y)  # train it


        pred_y = learner.query(train_x)
        rmse_in = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])

        rmse_records_in = np.append(rmse_records_in, rmse_in)
        leaf_sizes = np.append(leaf_sizes, i)


        pred_y = learner.query(test_x)
        rmse_out = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])

        rmse_records_out = np.append(rmse_records_out, rmse_out)


        #     # # evaluate in sample
        # pred_y = learner.query(train_x)  # get the predictions
        #
        #
        # rmse_in = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
        # rmse_records_in = np.append(rmse_records_in, rmse_in)
        # leaf_sizes = np.append(leaf_sizes, i)
        # print("In sample results")
        # print(f"RMSE: {rmse_in}")
        # print(rmse_records_in)

        # c = np.corrcoef(pred_y, y=train_y)
        # print(f"corr: {c[0,1]}")

        # evaluate out of sample
        # pred_y = learner.query(test_x)  # get the predictions
        #
        # rmse_out = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
        # rmse_records_out = np.append(rmse_records_out, rmse_out)

    print(rmse_records_in.shape)
    print(rmse_records_out.shape)

    plt.plot(leaf_sizes, rmse_records_in, label = "insample")
    plt.plot(leaf_sizes, rmse_records_out, label = "out of sample")
    plt.legend()
    plt.xlim(100, 0)
    plt.xlabel('leaf size')
    plt.ylabel('rmse')
    plt.show()



    '''
    Experiment 2
    '''


'''
mean rmse
    for i in range(1, 100):
        # print_five()
        learner = dtl.DTLearner(leaf_size = i)

        learner.add_evidence(train_x, train_y)  # train it
        rmse_in = 0
        for j in range(10):
            pred_y = learner.query(train_x)
            rmse_in += math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
        mean_rmse_in = rmse_in / 10
        rmse_records_in = np.append(rmse_records_in, rmse_in)
        leaf_sizes = np.append(leaf_sizes, i)

        rmse_out = 0
        for j in range(10):
            pred_y = learner.query(test_x)
            rmse_out += math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
        mean_rmse_out= rmse_out / 10
        rmse_records_out = np.append(rmse_records_out, rmse_out)
'''