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
import random

class RTLearner(object):
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
        self.tree = None
        self.leaf_size = 1
        pass  # move along, these aren't the drones you're looking for

    def author(self):
        """
        :return: The GT username of the student
        :rtype: str
        """
        return "tcheng99"  # replace tb34 with your Georgia Tech username



    def add_evidence(self, data_x, data_y):


        # random.seed(10)
        # print(data_y)
        # print(data_x, data_y)
        # data_y = data_y.reshape(-1, 1)
        # print('here')
        def build_tree(data_x, data_y):

            # print(data_y)

            if data_x.shape[0] == self.leaf_size:
                # print('base case 1')
                return np.array([[-1, data_y[0], None, None]])
            elif (data_y[:] == data_y[0]).all():
                # print('base case 2')
                return np.array([[-1, data_y[0], None, None]])
            else:
                #######line 4: pick random feature

                random_index = random.randint(0, data_x.shape[1]-1) #aka random feature/column

                # #determine split val
                random_row = random.randint(0, data_x.shape[0]-1)
                random_val1 = data_x[random_row, random_index]


                random_row = random.randint(0, data_x.shape[0] - 1)
                random_val2 = data_x[random_row, random_index]



                split_val = (random_val1 + random_val2) / 2
                # print('random col is', random_index)
                # print(split_val)

                left_split_x = data_x[np.where(data_x[:, random_index] <= split_val)]
                left_split_y = data_y[np.where(data_x[:, random_index] <= split_val)]

                right_split_x = data_x[np.where(data_x[:, random_index] > split_val)]
                right_split_y = data_y[np.where(data_x[:, random_index] > split_val)]

                if left_split_x.shape[0] == 0 or right_split_x.shape[0] == 0:
                    print('here')
                    return np.array([[-1, np.mean(data_y[:]), None, None]])
                left_tree = build_tree(left_split_x, left_split_y)

                # # recurse right

                right_tree = build_tree(right_split_x, right_split_y)
                # #
                # # # build root
                # #
                root = np.array([[random_index, split_val, 1, left_split_x.shape[0] + 1]])
                #
                return np.concatenate((root, left_tree, right_tree))

        #
        #
        tree = build_tree(data_x, data_y)
        print(tree)
        self.tree = tree
        return tree


    def study_group(self):
        return 'tcheng99'

    def query(self, data_x):
        # data is just a row of data such that it is [x1, x2, x3, .. xn]

        #
        matrix = self.tree
        leaf_not_reached = True
        index = 0

        arr = np.array([])

        def search(data):

            leaf_not_reached = True
            index = 0
            while leaf_not_reached:
                feature, split_val, left, right = matrix[int(index)]
                if feature == -1:
                    # print('end')
                    leaf_not_reached = True
                    # print(split_val) #split val is the prediction at this point
                    return split_val
                    # return prediction -> what is prediction?
                    '''
                    when you reach a leaf node, you return the split val?
    
                    Return split val of that level
                    '''

                curr_val = data[int(feature)]

                if curr_val <= split_val:
                    index = index + left

                else:

                    index = index + right  # my indexing is off here

                #
                # #just to terminate
                # leaf_not_reached = False

        res = np.array([])
        # print(data_x)
        for r in data_x:
            pred = search(r)
            res = np.append(res, pred)
            print(pred)
            # res = np.concatenate((res, pred), axis=1)

        print(res.shape)
        # print('res is', res)
        return res



if __name__ == "__main__":

    # class test case
    # x_train = np.array([
    #     [.885, .330, 9.1],
    #     [.725, .39, 10.9],
    #     [.560, .5, 9.4],
    #     [.735, .570, 9.8],
    #     [.610, .630, 8.4],
    #     [.260, .630, 11.8],
    #     [.5, .68, 10.5],
    #     [.320, .780, 10]
    #
    # ])
    #
    # y_train = np.array([[4], [5], [6], [5], [3], [8], [7], [6]])


    #base case 1
    # x_train = np.array([
    #     [.885, .330, 9.1]
    # ])
    #
    # y_train = np.array([100])
    #
    # #base case 2
    # x_train = np.array([
    #     [.885, .330, 9.1],
    #     [.885, .330, 9.1],
    #     [.885, .330, 9.1],
    # ])
    #
    # y_train = np.array([[100],  [100], [100]])

    #General case

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


    y_train = np.array([4, 5, 6, 5, 6, 3, 4, 5])

    x_test = np.array([
        [.885, .330, 9.1],
        [.725, .39, 10.9],
        [.560, .5, 9.4],
        [.735, .570, 9.8],
        [.610, .630, 8.4],
        [.260, .630, 11.8],
        [.5, .68, 10.5],
        [.320, .780, 10]

    ])

    learner = RTLearner()
    learner.add_evidence(x_train, y_train)
    # learner.query(x_test)
