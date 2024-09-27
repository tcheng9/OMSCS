""""""  		  	   		 	   		  		  		    	 		 		   		 		  
"""  		  	   		 	   		  		  		    	 		 		   		 		  
template for generating data to fool learners (c) 2016 Tucker Balch  		  	   		 	   		  		  		    	 		 		   		 		  
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
GT User ID: tcheng99 (replace with your User ID)  		  	   		 	   		  		  		    	 		 		   		 		  
GT ID: 903967530 (replace with your GT ID)  		  	   		 	   		  		  		    	 		 		   		 		  
"""  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import math  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import numpy as np

import matplotlib.pyplot as plt

  		  	   		 	   		  		  		    	 		 		   		 		  
# this function should return a dataset (X and Y) that will work  		  	   		 	   		  		  		    	 		 		   		 		  
# better for linear regression than decision trees  		  	   		 	   		  		  		    	 		 		   		 		  
def best_4_lin_reg(seed=1489683273):  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    Returns data that performs significantly better with LinRegLearner than DTLearner.  		  	   		 	   		  		  		    	 		 		   		 		  
    The data set should include from 2 to 10 columns in X, and one column in Y.  		  	   		 	   		  		  		    	 		 		   		 		  
    The data should contain from 10 (minimum) to 1000 (maximum) rows.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    :param seed: The random seed for your data generation.  		  	   		 	   		  		  		    	 		 		   		 		  
    :type seed: int  		  	   		 	   		  		  		    	 		 		   		 		  
    :return: Returns data that performs significantly better with LinRegLearner than DTLearner.  		  	   		 	   		  		  		    	 		 		   		 		  
    :rtype: numpy.ndarray  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    np.random.seed(seed)  		  	   		 	   		  		  		    	 		 		   		 		  
    x = np.zeros((100, 2))
    # y = np.zeros(((100, 1)))
    y = np.random.random(size=(100,)) * 200 - 100
    # Here's is an example of creating a Y from randomly generated  		  	   		 	   		  		  		    	 		 		   		 		  
    # X with multiple columns

    # x[:, 0] = np.random.random(size=(100,)) * 100
    # # y = x[:,0] + np.sin(x[:,1]) + x[:,2]**2 + x[:,3]**3
    # y = np.random.random(size=(100,)) * 1000

    for i in range(100):
        x[i, 0] = np.random.random() * 100
        x[i, 1] = np.random.random() * 100
        y[i] = 5*x[i, 0] + 2*x[i, 1]
    return x, y  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
def best_4_dt(seed=1489683273):  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    Returns data that performs significantly better with DTLearner than LinRegLearner.  		  	   		 	   		  		  		    	 		 		   		 		  
    The data set should include from 2 to 10 columns in X, and one column in Y.  		  	   		 	   		  		  		    	 		 		   		 		  
    The data should contain from 10 (minimum) to 1000 (maximum) rows.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    :param seed: The random seed for your data generation.  		  	   		 	   		  		  		    	 		 		   		 		  
    :type seed: int  		  	   		 	   		  		  		    	 		 		   		 		  
    :return: Returns data that performs significantly better with DTLearner than LinRegLearner.  		  	   		 	   		  		  		    	 		 		   		 		  
    :rtype: numpy.ndarray  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    np.random.seed(seed)  		  	   		 	   		  		  		    	 		 		   		 		  
    x = np.zeros((300, 4))
    y = np.random.random(size=(300,)) * 200 - 100

    for i in range(300):
        x[i, 0] = np.random.random() * 100
        x[i, 1] = 5 * np.random.random() * 100
        x[i, 2] = -2 * np.random.random() * 100
        x[i, 3] = 10 * np.random.random() * 100
        # #
        if i <= 100:
            x[i, 0] = np.random.random() * 1
            x[i, 1] = 5 * np.random.random() * 1
            x[i, 2] = 2 * np.random.random() * 1
            x[i, 3] = 10 * np.random.random() * 1

            y[i] = math.log(x[i, 0]) + math.log(x[i,1]) + math.log(x[i, 2])
        elif (i > 100 and i <= 200):
            x[i, 0] = np.random.random() * 50
            x[i, 1] = 5 * np.random.random() * 50
            x[i, 2] = -2 * np.random.random() * 50
            x[i, 3] = 10 * np.random.random() * 50
            y[i] = 1/-1* pow(x[i, 0],2 ) + 1/4*x[i,1] + 1/pow(x[i, 2], 2)
        else:
            x[i, 0] = np.random.random() * 500
            x[i, 1] = 5 * np.random.random() * 500
            x[i, 2] = -2 * np.random.random() * 500
            x[i, 3] = 10 * np.random.random() * 500
            y[i] = pow(x[i, 0], 3) + 10*x[i,1] + pow(x[i, 2], 3)
        # x[i, 0] = pow(x[i, 0], 2)
        # x[i, 1] = pow(x[i, 1] , 4)
        # x[i, 2] = pow(x[i, 1], 6)
        # y[i] = x[i, 0] * x[i, 1] * x[i, 2]



    return x, y  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
def author():  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		 	   		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
    return "tcheng99"  # Change this to your user ID

def study_group(self):

    return 'tcheng99'
  		  	   		 	   		  		  		    	 		 		   		 		  
# if __name__ == "__main__":
    # x,y = best_4_lin_reg(0)
    # # print(x.shape)
    # # print(y.shape)
    # # print(x)
    # # print(y)
    # plt.plot(x[:, 0],y)
    # plt.show()


    # x,y = best_4_dt(0)
    # # print(x)
    # print(x)
    # plt.plot(x, y)
    # plt.show()