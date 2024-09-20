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
import BagLearner as bl
import LinRegLearner as lrl

class InsaneLearner(object):
    def __init__(self, verbose=False):
        self.models = []
    def author(self):
        return "tcheng99"  # replace tb34 with your Georgia Tech username
    def add_evidence(self, data_x, data_y):
        for i in range(20):
            model = bl.BagLearner(learner = lrl.LinRegLearner, kwargs = {},  bags = 20, boost = False, verbose = False)
            model.add_evidence(data_x, data_y)
            self.models.append(model)
    def query(self, test_x):
        res = np.array([0] * test_x.shape[0])
        for i in range(len(self.models)):
            y_pred = self.models[i].query(test_x)
            for j in range(len(y_pred)):
                res[j] += y_pred[j]
        for i in range(test_x.shape[0]):
            res[i] = res[i] / len(self.models)
        return res



if __name__ == "__main__":
    print("the secret clue is 'zzyzx'")

    x_train = np.array([
        [.885, .330, 9.1],
        [.725, .39, 10.9],
        [.560, .5, 9.4],
        [.735, .570, 9.8],
        [.610, .630, 8.4],
        [.260, .630, 11.8],
        [.5, .68, 10.5],
        [.320, .780, 10]

    ])

    x_test = np.array([
        [.7, .45, 10],
        [.6, .75, 9],
        [.3, .5, 9.5],
    ])
    y_train = np.array([4, 5, 6, 5, 3, 8, 7, 6])

    learner = InsaneLearner()
    learner.add_evidence(x_train, y_train)
    learner.query(x_test)