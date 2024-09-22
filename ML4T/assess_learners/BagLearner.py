""""""
"""  		  	   		 	   		  		  		    	 		 		   		 		  
A simple wrapper for linear regression.  (c) 2015 Tucker Balch  		  	   		 	   		  		  		    	 		 		   		 		  

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

import numpy as np
import DTLearner as dtl
import RTLearner as rtl
import LinRegLearner as lrl

class BagLearner(object):


    def __init__(self, learner, kwargs = {"argument1":1, "argument2":2}, bags = 20, boost = False, verbose=False):
        """
        Constructor method
        """
        self.learner = learner #select a specific model to use
        self.kwargs = kwargs #parameters per model (ie 1 model uses 1 leaf_size, 2nd model uses 10 leaf_size
        self.bags =bags #number of models to create
        self.boost = boost #don't use
        self.verbose = verbose #optional to use
        self.models = []
        pass  # move along, these aren't the drones you're looking for

    def author(self):
        """
        :return: The GT username of the student
        :rtype: str
        """
        return "tcheng99"  # replace tb34 with your Georgia Tech username

    def study_group(self):
        return 'tcheng99'


    def resample(self, data_x, data_y):
        subsample_x = np.empty((0, data_x.shape[1]))
        subsample_y = np.array([])
        resample = int(0.6 * data_x.shape[0])
        for i in range(resample):
            random_row = np.random.randint(0, data_x.shape[0])

            # print('random index is', random_row)

            subsample_x = np.vstack((subsample_x, data_x[random_row, :]))
            subsample_y = np.append(subsample_y, data_y[random_row])

        return subsample_x, subsample_y
    def add_evidence(self, data_x, data_y):
        learners = []


        for i in range(0, self.bags):

            # sample_x, sample_y = self.resample(data_x, data_y)
            learners.append(self.learner(**self.kwargs))


        for i in range(0, self.bags):
            sample_x, sample_y = self.resample(data_x, data_y)
            learners[i].add_evidence(sample_x, sample_y)


        self.models = learners



        """
        Add training data to learner

        :param data_x: A set of feature values used to train the learner
        :type data_x: numpy.ndarray
        :param data_y: The value we are attempting to predict given the X data
        :type data_y: numpy.ndarray
        """


    def query(self, test_x):

        """
        Estimate a set of test points given the model we built.

        :param points: A numpy array with each row corresponding to a specific query.
        :type points: numpy.ndarray
        :return: The predicted result of the input data according to the trained model
        :rtype: numpy.ndarray
        """
        res = np.array([float(0)] * test_x.shape[0])

        for i in range(len(self.models)):
            y_pred = self.models[i].query(test_x)
            # print(y_pred.shape)
            for j in range(len(y_pred)):
                # print(y_pred[j])
                res[j] += y_pred[j]


        for i in range(test_x.shape[0]):
            # print(res[i])
            # print(test_x.shape[0])
            res[i] = res[i] / self.bags

        return res





if __name__ == "__main__":
    print("the secret clue is 'zzyzx'")
    # class test case
    x_train = np.array([
        [.006508992, .000703323, .027263206],
        [.008070571, .008364512, .010298404],
        [.011703446, .019054811, .010298404],
        [.002294509, .011703446, .019054811],
        [.00540756, .008294571, .029936576],
        [.022378302, .011999815, .001498313],
        [.011166484, .002812079, .025962189],
        [0.010573187, 0.013050445, 0.0048923]
    ])



    y_train = np.array([
        .000841483,
        0.00213008,
        -0.017031881,
        0.023405287,
        0.008160491,
        -0.010673606,
        0.000841483,
        0.008160491])
    # ## infinite recursion test case
    # # x_train = np.array([
    # #     [.885,.330, 9.1],
    # #     [.725, .39, 10],
    # #     [.560, .5, 10],
    # #     [.735, .570,10],
    # #
    # #
    # # ])
    #
    #
    # # y_train = np.array([[4],[5], [6], [5]])
    #
    # x_test = np.array([
    #     [.7, .45, 10],
    #     [.6, .75, 9],
    #     [.3, .5, 9.5],
    # ])


    x_test = np.array([
        [0.002929655, 0.006462161, -0.008567381],
        [0.011719598, 0.02094488, -0.001478936],
        [0.015786402, 0.020041017, 0.021217576],

    ])



    bagger  = BagLearner(learner = dtl.DTLearner, kwargs = {"leaf_size":1}, bags = 10, boost = False, verbose = False)
    bagger.add_evidence(x_train, y_train)
    res = bagger.query(x_test)
