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
        # print(merged_data)
        # print(data_y)


        def dtAlgo(data):

            if data.shape[0] == 1: # "1" SHOULD ACTUALLY BE LEAF SIZE I THINK
                # print('base case 1')
                #need to handele leaf size
                return np.array([[-1, data[0, -1], None, None]])
            elif (data[:, -1] == data[0, -1]).all():
                # print('base case 2: all target data is the same')

                return np.array([[-1, data[0, -1], None, None]])
            else:

                #######line 4: pick best metric

                vals = np.corrcoef(data.T)

                vals = abs(vals[-1].T)

                #EDGE CASE: 2 OR MORE FEATURES SAME CORRELATION, MAKE SURE IT IS HANDLED
                best_feature_index = np.unravel_index(vals[0:-1].argmax(), vals.shape)


                # # #determine split val

                split_val = np.median(data[:, best_feature_index])

                # #recurse left
                rows, cols = np.where(data[:, best_feature_index] <= split_val)
                left_split = data[rows, :]

                left_tree = dtAlgo(left_split)

                #recurse right
                rows, cols = np.where(data[:, best_feature_index] > split_val)

                right_split = data[rows, :]
                print(right_split)
                right_tree = dtAlgo(right_split)

                #build root

                root = np.array([[best_feature_index[0], split_val, 1, left_split.shape[0] + 1]])

                return np.concatenate((root, left_tree, right_tree))



                #conc left, right,
        self.tree = dtAlgo(merged_data)

        return self.tree
    # def dtAlgo(self, data):
    #     if data.shape[0] == 1:
    #         return [0, data[0, -1], None, None]

        # if data.y
    def query(self, data_x):
        #data_x is just training data, you don't get predictions (aka data_y
        # merged_data = np.concatenate((data_x, data_y), axis=1)

        matrix = self.tree
        print(matrix)
        '''
        for each row of data in data x -> run the search algo on a single row
        '''


        def search(data):
            #data is just a row of data such that it is [x1, x2, x3, .. xn]

            print('running search')
            leaf_not_reached = True
            index = 0
            # feature, split_val, left, right = matrix[index]

            while leaf_not_reached:
                feature, split_val, left, right = matrix[index]
                if feature == -1:
                    leaf_not_reached = True
                    return split_val
                    # return prediction -> what is prediction?
                    '''
                    when you reach a leaf node, you return the split val?
                    
                    Return split val of that level
                    '''



                # print(feature, split_val, left, right)
                curr_val = data[int(feature)]

                if curr_val <= split_val:
                    index = index + left

                else:
                    index = index + right #my indexing is off here





                # print(index)

                #just to terminate
                leaf_not_reached = False

        search(data_x[0])


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



    y_train = np.array([[4],[5], [6], [5],[3], [8], [7],[6]])

    x_test = np.array([
        [.7,.45, 10],
    ])

    learner = DTLearner()
    learner.add_evidence(x_train, y_train)
    learner.query(x_test)


# lin reg code
# self.model_coefs, residuals, rank, s = np.linalg.lstsq(
#     new_data_x, data_y, rcond=None
# )


'''
Understanding query:

0. now you have a full tree built so you can pass in a X-feature (not x value but a vector named X)
1. From the tree, you have to unpack the values (feature column to check, val to split on, left node relative position such that current node row + left node row, right node relative positioning)
2. go down until you hit a leaf node where feature column == -1 or left/rigt == None


Questions:
1. is the input of DTLearner supposed to be a matrix?

2. how to process input of dtlearner
a. for each row, process it and see which node it lands on. 
b. each row should land on a leaf node

3. what is the input of dtlearner
a. x and y test so basically the same type of data we get as when we train the model

4. what does y really mean?
a. depends on your test data, ie flowers might tell you which flower it really ends up being
b. given a set of animal features, you could figure out the exact animal it is 
c. given cancer cell features, you could figure out the exact type of cancer it is (classificaiton via regrassion/numbers in this project)

5. how to use the tree? Store it in the learner properties?

6. what is DTlearner supposed to return?
a. a vector of y values?



Q:
1. confused about leaf size matter? I assume we are only use leaf_size = 1
my answer: leaf size is when you reach this leaf size (n = 1, only 1 sample) then you terminate and make it into a terminal leaf
if n = 3, 3 samples then you create 
2. y predictions is a matrix of n rows, 1 column
3. x input is not just 1 row of data but could be multiple rows of data nad you are expected to return prediction for each row
4. If so, can numpy do these for multiple rows of data or we would have to process these 1 at a time
5. any hint on the terminal/edge case case?
a. 1 edge case: recursion errors / at very low leaf sizes -> in the pseudocode, professor balch lists 2 exist conditons
1. split <= left_size and 2. data.y == same. any other ones? I would consider what would happen 
if say all the features are the and all the same rows have the same feature but the target variables are different. 
whats gonna happen to find a correlation, find median of feature 
"I believe it is theoretically possible to encounter a case in which the prescribed method of calculating SplitVal would cause infinite recursio"

My thoughts: 
----------------
i think he was saying if all values split the same side, what do you do?

-------------------------

-> recursively split of if all 4 rows go left and 0 rows go right

-> average in okay in recursive case


New questions:
will row split evenly? 
My right tree is not indexing right for some reason
Reason 1: 0 or 1 indexing is off
Reason 2: my recurive build tree for right split is wrong

'''

