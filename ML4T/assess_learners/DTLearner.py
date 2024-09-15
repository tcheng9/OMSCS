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


class DTLearner(object):
    """
    This is a Linear Regression Learner. It is implemented correctly.

    :param verbose: If “verbose” is True, your code can print out information for debugging.
        If verbose = False your code should not generate ANY output. When we test your code, verbose will be False.
    :type verbose: bool
    """

    def __init__(self, leaf_size = 1, verbose=False):
        """
        Constructor method
        """
        self.leaf_size = 1
        pass  # move along, these aren't the drones you're looking for

    def author(self):
        """
        :return: The GT username of the student
        :rtype: str
        """
        return "tcheng99"  # replace tb34 with your Georgia Tech username

    def study_group(self):
        # print('tcheng99')
        return 'tcheng99'
    def pick_best(self, data_x, data_y):
        vals = np.corrcoef(data_x, y=data_y.T)
        return vals[-1].T

    def add_evidence(self, data_x, data_y):
        """
        Add training data to learner

        :param data_x: A set of feature values used to train the learner
        :type data_x: numpy.ndarray
        :param data_y: The value we are attempting to predict given the X data
        :type data_y: numpy.ndarray
        """

        merged_data = np.concatenate((data_x, data_y) , axis = 1)
        print(merged_data)
        # print(data_y)


        def dtAlgo(data):

            if data.shape[0] == 1:
                print('base case 1')
                print([-1, data[0, -1], None, None])
                return [-1, data[0, -1], None, None]
            elif (data[:, -1] == data[0, -1]).all():
                print('base case 2: all target data is the same')
                return [-1, data[0, -1], None, None]
            else:

                # # print('case: general ')
                # print(data_x)
                # print(data_y)
                #######line 4: pick best metric

                vals = np.corrcoef(data.T)
                # print('correlation matrix', '\n',  vals)
                #
                vals = vals[-1].T
                # print('correlatons with y', '\n', vals)

                #https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-120.php#:~:text=argmax()%20function%20returns%20the,original%20shape%20of%20the%20array.
                best_feature_index = np.unravel_index(vals[0:-1].argmax(), vals.shape)
                # print('max index for best factor')
                # print(best_feature_index)


                # # #determine split val

                split_val = np.median(data[:, best_feature_index])

                # #recurse left
                rows, cols = np.where(data[:, best_feature_index] <= split_val)
                left_split = data[rows, :]
                left_tree = dtAlgo(left_split)

                #recurse right
                rows, cols = np.where(data[:, best_feature_index] > split_val)
                right_split = data[rows, :]

                right_tree = dtAlgo(right_split)

                #build root

                root = [best_feature_index, split_val, 1, left_tree.shape[1] + 1]

                return np.concatenate((root, left_tree, right_tree))



                #conc left, right,
        dtAlgo(merged_data)

    # def dtAlgo(self, data):
    #     if data.shape[0] == 1:
    #         return [0, data[0, -1], None, None]

        # if data.y
    def query(self, points):
        """
        Estimate a set of test points given the model we built.

        :param points: A numpy array with each row corresponding to a specific query.
        :type points: numpy.ndarray
        :return: The predicted result of the input data according to the trained model
        :rtype: numpy.ndarray
        """
        return (self.model_coefs[:-1] * points).sum(axis=1) + self.model_coefs[
            -1
        ]


if __name__ == "__main__":
    #case 1 - general case
    # x_train = np.array([[1, 3, 4], [5, 3, 1], [2, 3, 1]])
    # y_train = np.array([[5], [5], [7]])

    #base case 1 - 1 row
    # x_train = np.array([[1,2,3],])
    # y_train = np.array([[2],])

    #base case 2 - all y is same
    # x_train = np.array([[1, 3, 4], [5, 3, 1], [2, 3, 1]])
    # y_train = np.array([[5], [5], [5]])
    # print(arr.shape)

    #class test case
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



    y_train = np.array([[4],[5], [6], [5],[3], [8], [7],[6]
    ])


    learner = DTLearner()
    learner.add_evidence(x_train, y_train)



# lin reg code
# self.model_coefs, residuals, rank, s = np.linalg.lstsq(
#     new_data_x, data_y, rcond=None
# )
