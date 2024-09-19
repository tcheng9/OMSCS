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
        self.tree = None
        pass  # move along, these aren't the drones you're looking for

    def author(self):
        """
        :return: The GT username of the student
        :rtype: str
        """
        return "tcheng99"  # replace tb34 with your Georgia Tech username

    def study_group(self):

        return 'tcheng99'


    def add_evidence(self, data_x, data_y):
        """
        Add training data to learner

        :param data_x: A set of feature values used to train the learner
        :type data_x: numpy.ndarray
        :param data_y: The value we are attempting to predict given the X data
        :type data_y: numpy.ndarray
        """

        # data_y = np.array([data_y])

        merged_data = np.concatenate((data_x, data_y), axis = 1)
        # print(merged_data)


        def dtAlgo(data):
            # if data.shape[0] == 0:
            #     return np.array([])
            if data.shape[0] == 1: # "1" SHOULD ACTUALLY BE LEAF SIZE I THINK

                #need to handele leaf size
                return np.array([[-1, data[0, -1], None, None]])
            elif (data[:, -1] == data[0, -1]).all():


                return np.array([[-1, data[0, -1], None, None]])
            else:

                #######line 4: pick best metric

                vals = np.corrcoef(data)
                # print(vals)
                vals =(vals[-1].T)
                print(vals)
                #EDGE CASE: 2 OR MORE FEATURES SAME CORRELATION, MAKE SURE IT IS HANDLED
                best_feature_index = np.unravel_index(vals[0:-1].argmax(), vals.shape)

                # return ('here')
                # # #determine split val

                split_val = np.median(data[:, best_feature_index])

                # #recurse left
                rows, cols = np.where(data[:, best_feature_index] <= split_val)
                left_split = data[rows, :]

                rows, cols = np.where(data[:, best_feature_index] > split_val)
                right_split = data[rows, :]
                # if left_split.shape[0] == 0 or right_split.shape[0] == 0:
                #     print('placeholder')
                    # print('inf recursion case')
                    # print('data is', )
                    # print(data)
                    #
                    # print('left split is', )
                    # print(left_split)
                    # print('mean is')
                    # print(np.mean(data[:, -1]))

                    # np.mean(data[:, -1])
                    # print(np.array([[-1, np.mean(data[:, -1]), None, None]]))
                    # return np.array([[-1, np.mean(data[:, -1]), None, None]])


                # np.array([[-1, np.mean(data[:, -1]), None, None]])

                left_tree = dtAlgo(left_split)


                #recurse right


                right_tree = dtAlgo(right_split)


                #build root

                root = np.array([[best_feature_index[0], split_val, 1, left_split.shape[0] + 1]])

                return np.concatenate((root, left_tree, right_tree))



                #conc left, right,
        # return dtAlgo(merged_data)
        self.tree = dtAlgo(merged_data)
        print(self.tree)
        return self.tree
        # return -1
    def query(self, data_x):
        #data_x is just training data, you don't get predictions (aka data_y
        # merged_data = np.concatenate((data_x, data_y), axis=1)

        matrix = self.tree

        '''
        for each row of data in data x -> run the search algo on a single row
        '''


        def search(data):
            # print('tree shape', self.tree.shape)
            # print(self.tree.shape)
            #data is just a row of data such that it is [x1, x2, x3, .. xn]


            leaf_not_reached = True
            index = 0
            # feature, split_val, left, right = matrix[index]
            # arr = []
            while leaf_not_reached:
                feature, split_val, left, right = matrix[int(index)]
                if feature == -1:

                    leaf_not_reached = True

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
                    index = index + right #my indexing is off here





                #
                # #just to terminate
                # leaf_not_reached = False
        res = np.array([[],])
        for r in data_x:

            pred = search(r)

            if not pred:
                print('missing')
            pred = np.array([[pred],])
            # print('prediction is', pred)

            res = np.concatenate((res, pred), axis = 1)

        res = res.reshape(-1, 1)

        return res



if __name__ == "__main__":
    print('placehlder')
    #case 1 - general case
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

    y_train = np.array([[4], [5], [6], [5], [6], [3], [4], [5]])
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
    #     [.7,.45, 10],
    #     [.6, .75, 9],
    #     [.3, .5, 9.5],
    #
    # ])
    #
    learner = DTLearner()
    learner.add_evidence(x_train, y_train)
    # print(learner.tree)

    # res = learner.query(x_test)
    # print('res')
    # print(res)

# lin reg code
# self.model_coefs, residuals, rank, s = np.linalg.lstsq(
#     new_data_x, data_y, rcond=None
# )
