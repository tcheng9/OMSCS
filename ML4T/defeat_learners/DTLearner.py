""""""  		  	   		 	   		  		  		    	 		 		   		 		  
"""  		  	   		 	   		  		  		    	 		 		   		 		  
A simple wrapper for linear regression.  (c) 2015 Tucker Balch  		  	   		 	   		  		  		    	 		 		   		 		  
Note, this is NOT a correct DTLearner; Replace with your own implementation.  		  	   		 	   		  		  		    	 		 		   		 		  
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
  		  	   		 	   		  		  		    	 		 		   		 		  
Student Name: Tucker Balch (replace with your name)  		  	   		 	   		  		  		    	 		 		   		 		  
GT User ID: tb34 (replace with your User ID)  		  	   		 	   		  		  		    	 		 		   		 		  
GT ID: 900897987 (replace with your GT ID)  		  	   		 	   		  		  		    	 		 		   		 		  
"""  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import warnings  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import numpy as np  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
class DTLearner(object):  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    This is a decision tree learner object that is implemented incorrectly. You should replace this DTLearner with  		  	   		 	   		  		  		    	 		 		   		 		  
    your own correct DTLearner from Project 3.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    :param leaf_size: The maximum number of samples to be aggregated at a leaf, defaults to 1.  		  	   		 	   		  		  		    	 		 		   		 		  
    :type leaf_size: int  		  	   		 	   		  		  		    	 		 		   		 		  
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		 	   		  		  		    	 		 		   		 		  
        If verbose = False your code should not generate ANY output. When we test your code, verbose will be False.  		  	   		 	   		  		  		    	 		 		   		 		  
    :type verbose: bool  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    def __init__(self, leaf_size=1, verbose=False):  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        Constructor method  		  	   		 	   		  		  		    	 		 		   		 		  
        """
        self.leaf_size = leaf_size
        self.model = None
        pass  # move along, these aren't the drones you're looking for  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    def author(self):  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        :return: The GT username of the student  		  	   		 	   		  		  		    	 		 		   		 		  
        :rtype: str  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        return "tcheng99"  # replace tb34 with your Georgia Tech username

    def pick_best_feature(self, data_x, data_y):
        corr = np.corrcoef(data_x, data_y, rowvar=False)
        vals = np.absolute(corr[0:-1, -1])
        best_index = np.argmax(vals)
        return best_index
    def dtAlgo(self,data_x, data_y):

        if data_x.shape[0] <= self.leaf_size:  # "1" SHOULD ACTUALLY BE LEAF SIZE I THINK
            # need to handele leaf size

            return np.array([[-1, data_y[0], None, None]])
        elif (data_y[:] == data_y[0]).all():

            return np.array([[-1, data_y[0], None, None]])
        else:
            #######line 4: pick best metric

            i = self.pick_best_feature(data_x, data_y)

            split_val = np.median(data_x[:, i])

            left_split_x = data_x[data_x[:, i] <= split_val]
            left_split_y = data_y[data_x[:, i] <= split_val]

            right_split_x = data_x[data_x[:, i] > split_val]
            right_split_y = data_y[data_x[:, i] > split_val]

            # if left_split_x.shape[0] == 0:
            #     return np.array([[-1, right_split_y.mean(), -1 , -1]])
            if right_split_x.shape[0] == 0:
                return np.array([[-1, left_split_y.mean(), -1, -1]])

            left_tree = self.dtAlgo(left_split_x, left_split_y)

            right_tree = self.dtAlgo(right_split_x, right_split_y)

            root = np.array([[i, split_val, 1, left_tree.shape[0] + 1]])

            return np.concatenate((root, left_tree, right_tree))
    def add_evidence(self, data_x, data_y):  		  	   		 	   		  		  		    	 		 		   		 		  
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        Add training data to learner  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        :param data_x: A set of feature values used to train the learner  		  	   		 	   		  		  		    	 		 		   		 		  
        :type data_x: numpy.ndarray  		  	   		 	   		  		  		    	 		 		   		 		  
        :param data_y: The value we are attempting to predict given the X data  		  	   		 	   		  		  		    	 		 		   		 		  
        :type data_y: numpy.ndarray  		  	   		 	   		  		  		    	 		 		   		 		  
        """

        tree = self.dtAlgo(data_x, data_y)
        self.model = tree

        return tree

    def search(self, data):
        matrix = self.model

        row_index = 0

        while True:

            row = self.model[row_index, :]

            feature = int(row[0])
            split_val = row[1]

            if feature == -1:
                return row[1]
            if data[feature] <= split_val:
                new_row = row_index + int(row[2])

            else:
                new_row = row_index + int(row[3])

            row_index = new_row
            # row = self.model[int(node), :]
    def query(self, train_x):
        """  		  	   		 	   		  		  		    	 		 		   		 		  
        Estimate a set of test points given the model we built.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        :param points: A numpy array with each row corresponding to a specific query.  		  	   		 	   		  		  		    	 		 		   		 		  
        :type points: numpy.ndarray  		  	   		 	   		  		  		    	 		 		   		 		  
        :return: The predicted result of the input data according to the trained model  		  	   		 	   		  		  		    	 		 		   		 		  
        :rtype: numpy.ndarray  		  	   		 	   		  		  		    	 		 		   		 		  
        """
        res = np.array([])
        for r in train_x:
            pred = self.search(r)

            res = np.append(res, pred)

        return res
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
if __name__ == "__main__":

#     #case 1 - general case
    # x_train = np.array([[1, 3, 4], [5, 3, 1], [2, 3, 1]])
    # y_train = np.array([[5], [5], [7]])

    #base case 1 - 1 row
    # x_train = np.array([[1,2,3],])
    # y_train = np.array([[2],])

    #base case 2 - all y is same
    # x_train = np.array([[1, 3, 4], [5, 3, 1], [2, 3, 1]])
    # y_train = np.array([[5], [5], [5]])


    # class test case
    x_train = np.array([
        [.885,.330, 9.1],
        [.725, .39, 10.9],
        [.560, .5, 9.4],
        [.735, .570, 9.8],
        [.610, .630, 8.4],
        [.260, .630, 11.8],
        [.5, .68, 10.5],
        [.320, .780, 10]

    ])

    y_train = np.array([4, 5, 6, 5, 3,8,7,6])
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
    x_test = np.array([
        [.7,.45, 10],
        [.6, .75, 9],
        [.3, .5, 9.5],
        [.7, .45, 10],
        [.6, .75, 9],
        [.3, .5, 9.5],
    ])

    learner = DTLearner()
    tree = learner.add_evidence(x_train, y_train)


    res = learner.query(x_test)
    print(res)
