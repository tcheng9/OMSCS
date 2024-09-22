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
def print_five():
    print(5)

def mae_calc(exp_y, true_y):
    mae = np.sum(abs(exp_y - true_y) / true_y.shape[0])

    return mae
def resample(data_x, data_y):

    subsample_x = np.empty((0, data_x.shape[1]))
    subsample_y = np.array([])
    resample = int(0.6 * data_x.shape[0])
    for z in range(resample):
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
    np.random.seed(903967530)
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

    '''
    SHUFFLE THE DATA 1 time
    '''
    train_x, train_y = resample(train_x, train_y)
    test_x, test_y = resample(test_x, test_y)

    print(f"{test_x.shape}")
    print(f"{test_y.shape}")
    #
    # '''
    # Insane learner test
    # '''
    #
    # # for i in range(len(leaf_size)):
    #
    # learner = il.InsaneLearner()
    # learner.add_evidence(train_x, train_y)  # train it
    #
    #
    # pred_y = learner.query(train_x)
    # rmse_in = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
    #
    # print(rmse_in)
    #
    #     # out of sample calc
    #
    # pred_y = learner.query(test_x)
    # rmse_out = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
    # print(rmse_out)
    #

    '''
    
    Experiment 1
    
    '''
    # leaf_sizes = []
    # rmse_records_in = []
    # rmse_records_out = []
    #
    # print('running exp 1 - dt learner')
    # # create a learner and train it
    # # learner = lrl.LinRegLearner(verbose=True)  # create a LinRegLearner
    #
    # # for i in range(len(leaf_size)):
    # for i in range(1, 80):
    #     learner = dtl.DTLearner(leaf_size = i)
    #     learner.add_evidence(train_x, train_y)  # train it
    #
    #
    #     #insample calcs
    #     pred_y = learner.query(train_x)
    #     rmse_in = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
    #
    #
    #     rmse_records_in.append(rmse_in)
    #     leaf_sizes.append(i)
    #
    #     #out of sample calc
    #
    #     pred_y = learner.query(test_x)
    #     rmse_out = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
    #     rmse_records_out.append(rmse_out)



    # plt.plot(leaf_sizes, rmse_records_in, label = "insample")
    # plt.plot(leaf_sizes, rmse_records_out, label = "out of sample")
    # plt.legend()
    # plt.title('exp 1 - dt learner')
    #
    # plt.text(100, 0.008, 'tcheng99@gatech.edu', fontsize=40, color='gray', rotation=10)
    # plt.xlim(80, 0)
    # plt.xlabel('leaf size')
    # plt.ylabel('rmse')
    # # plt.show()
    # plt.savefig('exp1.png')
    # plt.close()

    # '''
    # Experiment 2
    # '''


    print('running exp 2 - bagging ')


    #
    # leaf_sizes = np.array([])
    # rmse_records_in = np.array([])
    # rmse_records_out = np.array([])
    #
    # learners = []
    # for k in range(80):
    #
    #     learner = bl.BagLearner(learner = dtl.DTLearner, kwargs = {"leaf_size":k}, bags = 20, boost = False, verbose = False)
    #     learner.add_evidence(train_x, train_y)  # train it
    #     learners.append(learner)
    #
    # for i in range(80):
    #     learner = learners[i]
    #     pred_y = learner.query(train_x)
    #     rmse_in = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
    #
    #     rmse_records_in = np.append(rmse_records_in, rmse_in)
    #     leaf_sizes = np.append(leaf_sizes, i)
    #
    #     pred_y = learner.query(test_x)
    #     rmse_out = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
    #
    #     rmse_records_out = np.append(rmse_records_out, rmse_out)
    # print(rmse_records_in)
    # print('---')
    # print(rmse_records_out)
    # print(leaf_sizes)
    # print(rmse_records_in)
    # plt.plot(leaf_sizes, rmse_records_in, label="insample")
    # plt.plot(leaf_sizes, rmse_records_out, label="out of sample")
    # plt.text(100, 0.0120, 'tcheng99@gatech.edu', fontsize=40, color='gray', rotation = 0)
    # plt.text(100, 0.0080, 'tcheng99@gatech.edu', fontsize=40, color='gray', rotation= 0)
    # plt.legend()
    # plt.title('exp 2 - bagging algo')
    # plt.xlim(100, 0)
    # plt.xlabel('leaf size')
    # plt.ylabel('rmse')
    # # plt.show()
    # plt.savefig('exp2.png')


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
    # leaf_sizes = np.empty((1, 80))
    # build_times = np.empty((2, 80), dtype = float)
    # learners = np.empty((2, 80), dtype = object) #row 1 = DT, row 2 = RT
    #
    # # model inits
    # for i in range(80):
    #     #leaf sie
    #
    #     leaf_sizes[0, i] = i
    #     # DT learner setup
    #     learner = dtl.DTLearner(leaf_size=i)
    #     start_time = time.time()
    #     learner.add_evidence(train_x, train_y)
    #     end_time = time.time()
    #     learners[0, i] = learner
    #     # print('dt tree time to build is', (end_time - start_time))
    #     time_diff = end_time - start_time
    #     build_times[0, i] = time_diff
    #     # print(learners)
    #     # print(build_times)
    #     #RT learner setup
    #
    #     learner = rtl.RTLearner(leaf_size=i)
    #     start_time = time.time()
    #     learner.add_evidence(train_x, train_y)
    #     end_time = time.time()
    #     learners[1, i] = learner
    #     # print('dt tree time to build is', (end_time - start_time))
    #     time_diff = end_time - start_time
    #     build_times[1, i] = time_diff
    # # print(leaf_sizes)
    # # print(learners)
    # # print(build_times)
    #
    # #Training models
    #
    # plt.plot(leaf_sizes[0, :], build_times[0, :], label = 'dtlearner')
    # plt.plot(leaf_sizes[0, :], build_times[1, :], label='rtlearner')
    # plt.legend()
    # plt.title('exp 3 - time to train')
    # plt.xlabel('leaf sizes')
    # plt.ylabel('time to train')
    # plt.show()


    '''
    experiment 3b - mean absolute error
    '''

    # np metod
    leaf_sizes = np.empty((1, 80))
    maes = np.empty((2, 80), dtype=float)
    learners = np.empty((2, 80), dtype=object)  # row 1 = DT, row 2 = RT

    # model inits
    for i in range(80):
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
    print('test_y shape is', test_y.shape)
    for i in range(80):
        y_pred = learners[0, i].query(test_x)
        mae = np.sum(np.absolute((test_y, y_pred))) / test_y.shape[0]
        print(mae)
        maes[0, i] = mae

        # #DTlearner mae
        # y_pred = learners[0, i].query(test_x)
        # mae = mae_calc(y_pred, test_y)
        # maes[0, i] = mae
        #
        # #RTlearner mae
        # y_pred = learners[1, i].query(test_x)
        # mae = mae_calc(y_pred, test_y)
        # maes[1, i] = mae

    plt.plot(leaf_sizes[0, :], maes[0, :], label = 'dt out mean absolute error')
    # plt.plot(leaf_sizes[0, :], maes[1, :], label='rt out mean absolute error')
    plt.show()