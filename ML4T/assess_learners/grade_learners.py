"""MC3-P1: Assess learners - grading script.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
Usage:  		  	   		 	   		  		  		    	 		 		   		 		  
- Switch to a student feedback directory first (will write "points.txt" and "comments.txt" in pwd).  		  	   		 	   		  		  		    	 		 		   		 		  
- Run this script with both ml4t/ and student solution in PYTHONPATH, e.g.:  		  	   		 	   		  		  		    	 		 		   		 		  
    PYTHONPATH=ml4t:MC3-P1/jdoe7 python ml4t/mc3_p1_grading/grade_learners.py  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
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
  		  	   		 	   		  		  		    	 		 		   		 		  
import math  		  	   		 	   		  		  		    	 		 		   		 		  
import os  		  	   		 	   		  		  		    	 		 		   		 		  
import random  		  	   		 	   		  		  		    	 		 		   		 		  
import string  		  	   		 	   		  		  		    	 		 		   		 		  
import sys  		  	   		 	   		  		  		    	 		 		   		 		  
import time  		  	   		 	   		  		  		    	 		 		   		 		  
import traceback as tb  		  	   		 	   		  		  		    	 		 		   		 		  
from collections import namedtuple  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import numpy as np  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
import pandas as pd  		  	   		 	   		  		  		    	 		 		   		 		  
import pytest  		  	   		 	   		  		  		    	 		 		   		 		  
import util  		  	   		 	   		  		  		    	 		 		   		 		  
from grading.grading import (  		  	   		 	   		  		  		    	 		 		   		 		  
    GradeResult,  		  	   		 	   		  		  		    	 		 		   		 		  
    IncorrectOutput,  		  	   		 	   		  		  		    	 		 		   		 		  
    grader,  		  	   		 	   		  		  		    	 		 		   		 		  
    run_with_timeout,  		  	   		 	   		  		  		    	 		 		   		 		  
    time_limit,  		  	   		 	   		  		  		    	 		 		   		 		  
)  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
# Grading parameters  		  	   		 	   		  		  		    	 		 		   		 		  
# rmse_margins = dict(KNNLearner=1.10, BagLearner=1.10)  # 1.XX = +XX% margin of RMS error  		  	   		 	   		  		  		    	 		 		   		 		  
# points_per_test_case = dict(KNNLearner=3.0, BagLearner=2.0)  # points per test case for each group  		  	   		 	   		  		  		    	 		 		   		 		  
# seconds_per_test_case = 10  # execution time limit  		  	   		 	   		  		  		    	 		 		   		 		  
# seconds_per_test_case = 6  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
# More grading parameters (picked up by module-level grading fixtures)  		  	   		 	   		  		  		    	 		 		   		 		  
max_points = 50.0  # 3.0*5 + 3.0*5 + 2.0*10 = 50  		  	   		 	   		  		  		    	 		 		   		 		  
html_pre_block = (  		  	   		 	   		  		  		    	 		 		   		 		  
    True  # surround comments with HTML <pre> tag (for T-Square comments field)  		  	   		 	   		  		  		    	 		 		   		 		  
)  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
# Test cases  		  	   		 	   		  		  		    	 		 		   		 		  
LearningTestCase = namedtuple(  		  	   		 	   		  		  		    	 		 		   		 		  
    "LearningTestCase", ["description", "group", "datafile", "seed", "outputs"]  		  	   		 	   		  		  		    	 		 		   		 		  
)  		  	   		 	   		  		  		    	 		 		   		 		  
learning_test_cases = [
    ########################
    # DTLearner test cases #
    ########################
    LearningTestCase(
        description="Test Case 01: Deterministic Tree",
        group="DTLearner",
        datafile="Istanbul.csv",
        seed=1481090001,
        outputs=dict(
            insample_corr_min=0.95,
            outsample_corr_min=0.15,
            insample_corr_max=0.95,
        ),
    ),
    LearningTestCase(
        description="Test Case 02: Deterministic Tree",
        group="DTLearner",
        datafile="Istanbul.csv",
        seed=1481090002,
        outputs=dict(
            insample_corr_min=0.95,
            outsample_corr_min=0.15,
            insample_corr_max=0.95,
        ),
    ),
    LearningTestCase(
        description="Test Case 03: Deterministic Tree",
        group="DTLearner",
        datafile="Istanbul.csv",
        seed=1481090003,
        outputs=dict(
            insample_corr_min=0.95,
            outsample_corr_min=0.15,
            insample_corr_max=0.95,
        ),
    ),
    LearningTestCase(
        description="Test Case 04: Deterministic Tree",
        group="DTLearner",
        datafile="Istanbul.csv",
        seed=1481090004,
        outputs=dict(
            insample_corr_min=0.95,
            outsample_corr_min=0.15,
            insample_corr_max=0.95,
        ),
    ),
    # ########################
    # # RTLearner test cases #
    # ########################
    LearningTestCase(
        description="Test Case 01: Random Tree",
        group="RTLearner",
        datafile="Istanbul.csv",
        seed=1481090001,
        outputs=dict(
            insample_corr_min=0.95,
            outsample_corr_min=0.15,
            insample_corr_max=0.95,
        ),
    ),
    LearningTestCase(
        description="Test Case 02: Random Tree",
        group="RTLearner",
        datafile="Istanbul.csv",
        seed=1481090002,
        outputs=dict(
            insample_corr_min=0.95,
            outsample_corr_min=0.15,
            insample_corr_max=0.95,
        ),
    ),
    LearningTestCase(
        description="Test Case 03: Random Tree",
        group="RTLearner",
        datafile="Istanbul.csv",
        seed=1481090003,
        outputs=dict(
            insample_corr_min=0.95,
            outsample_corr_min=0.15,
            insample_corr_max=0.95,
        ),
    ),
    LearningTestCase(
        description="Test Case 04: Random Tree",
        group="RTLearner",
        datafile="Istanbul.csv",
        seed=1481090004,
        outputs=dict(
            insample_corr_min=0.95,
            outsample_corr_min=0.15,
            insample_corr_max=0.95,
        ),
    ),
    # ######################
    # # Bagging test cases #
    # ######################
    LearningTestCase(
        description="Test Case 01: Bagging",
        group="BagLearner",
        datafile="Istanbul.csv",
        seed=1481090001,
        outputs=None,
    ),
    LearningTestCase(
        description="Test Case 02: Bagging",
        group="BagLearner",
        datafile="Istanbul.csv",
        seed=1481090002,
        outputs=None,
    ),
    LearningTestCase(
        description="Test Case 03: Bagging",
        group="BagLearner",
        datafile="Istanbul.csv",
        seed=1481090003,
        outputs=None,
    ),
    LearningTestCase(
        description="Test Case 04: Bagging",
        group="BagLearner",
        datafile="Istanbul.csv",
        seed=1481090004,
        outputs=None,
    ),
    LearningTestCase(
        description="Test Case 05: Bagging",
        group="BagLearner",
        datafile="Istanbul.csv",
        seed=1481090005,
        outputs=None,
    ),
    LearningTestCase(
        description="Test Case 06: Bagging",
        group="BagLearner",
        datafile="Istanbul.csv",
        seed=1481090006,
        outputs=None,
    ),
    LearningTestCase(
        description="Test Case 07: Bagging",
        group="BagLearner",
        datafile="Istanbul.csv",
        seed=1481090007,
        outputs=None,
    ),
    LearningTestCase(
        description="Test Case 08: Bagging",
        group="BagLearner",
        datafile="Istanbul.csv",
        seed=1481090008,
        outputs=None,
    ),
    # ##############################
    # # RandomName + InsaneLearner #
    # ##############################
    # LearningTestCase(
    #     description="InsaneLearner Test Case",
    #     group="InsaneLearner",
    #     datafile="simple.csv",
    #     seed=1498076428,
    #     outputs=None,
    # ),
    # LearningTestCase(
    #     description="Random Classname Test Case",
    #     group="RandomName",
    #     datafile="simple.csv",
    #     seed=1498076428,
    #     outputs=None,
    # ),
]  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
# Test functon(s)  		  	   		 	   		  		  		    	 		 		   		 		  
@pytest.mark.parametrize(  		  	   		 	   		  		  		    	 		 		   		 		  
    "description,group,datafile,seed,outputs", learning_test_cases  		  	   		 	   		  		  		    	 		 		   		 		  
)  		  	   		 	   		  		  		    	 		 		   		 		  
def test_learners(description, group, datafile, seed, outputs, grader):  		  	   		 	   		  		  		    	 		 		   		 		  
    """Test ML models returns correct predictions.  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    Requires test description, test case group, inputs, expected outputs, and a grader fixture.  		  	   		 	   		  		  		    	 		 		   		 		  
    """  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
    points_earned = 0.0  # initialize points for this test case  		  	   		 	   		  		  		    	 		 		   		 		  
    try:  		  	   		 	   		  		  		    	 		 		   		 		  
        learner_class = None  		  	   		 	   		  		  		    	 		 		   		 		  
        kwargs = {"verbose": False}  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        # (BPH) Copied from grade_strategy_qlearning.py  		  	   		 	   		  		  		    	 		 		   		 		  
        # Set fixed seed for repetability  		  	   		 	   		  		  		    	 		 		   		 		  
        np.random.seed(seed)  		  	   		 	   		  		  		    	 		 		   		 		  
        random.seed(seed)  		  	   		 	   		  		  		    	 		 		   		 		  
        # remove ability to seed either np.random or python random  		  	   		 	   		  		  		    	 		 		   		 		  
        tmp_numpy_seed = np.random.seed  		  	   		 	   		  		  		    	 		 		   		 		  
        tmp_random_seed = random.seed  		  	   		 	   		  		  		    	 		 		   		 		  
        np.random.seed = fake_seed  		  	   		 	   		  		  		    	 		 		   		 		  
        random.seed = fake_rseed  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        # Try to import KNNLearner (only once)  		  	   		 	   		  		  		    	 		 		   		 		  
        # if not 'KNNLearner' in globals():  		  	   		 	   		  		  		    	 		 		   		 		  
        #     from KNNLearner import KNNLearner  		  	   		 	   		  		  		    	 		 		   		 		  
        if not "RTLearner" in globals():  		  	   		 	   		  		  		    	 		 		   		 		  
            from RTLearner import RTLearner  		  	   		 	   		  		  		    	 		 		   		 		  
        if not "DTLearner" in globals():  		  	   		 	   		  		  		    	 		 		   		 		  
            from DTLearner import DTLearner
        if (  		  	   		 	   		  		  		    	 		 		   		 		  
            (group == "BagLearner")  		  	   		 	   		  		  		    	 		 		   		 		  
            or (group == "InsaneLearner")  		  	   		 	   		  		  		    	 		 		   		 		  
            or (group == "RandomName")  		  	   		 	   		  		  		    	 		 		   		 		  
            and (not "BagLearner" in globals())  		  	   		 	   		  		  		    	 		 		   		 		  
        ):  		  	   		 	   		  		  		    	 		 		   		 		  
            from BagLearner import BagLearner  		  	   		 	   		  		  		    	 		 		   		 		  
        # put seeds back for the moment  		  	   		 	   		  		  		    	 		 		   		 		  
        np.random.seed = tmp_numpy_seed  		  	   		 	   		  		  		    	 		 		   		 		  
        random.seed = tmp_random_seed  		  	   		 	   		  		  		    	 		 		   		 		  
        # Tweak kwargs  		  	   		 	   		  		  		    	 		 		   		 		  
        # kwargs.update(inputs.get('kwargs', {}))  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        # Read separate training and testing data files  		  	   		 	   		  		  		    	 		 		   		 		  
        # with open(inputs['train_file']) as f:  		  	   		 	   		  		  		    	 		 		   		 		  
        # data_partitions=list()  		  	   		 	   		  		  		    	 		 		   		 		  
        test_x, test_y, train_x, train_y = None, None, None, None  		  	   		 	   		  		  		    	 		 		   		 		  
        permutation = None  		  	   		 	   		  		  		    	 		 		   		 		  
        author = None  		  	   		 	   		  		  		    	 		 		   		 		  
        with util.get_learner_data_file(datafile) as f:  		  	   		 	   		  		  		    	 		 		   		 		  
            alldata = np.genfromtxt(f, delimiter=",")  		  	   		 	   		  		  		    	 		 		   		 		  
            # Skip the date column and header row if we're working on Istanbul data  		  	   		 	   		  		  		    	 		 		   		 		  
            if datafile == "Istanbul.csv":  		  	   		 	   		  		  		    	 		 		   		 		  
                alldata = alldata[1:, 1:]  		  	   		 	   		  		  		    	 		 		   		 		  
            datasize = alldata.shape[0]  		  	   		 	   		  		  		    	 		 		   		 		  
            cutoff = int(datasize * 0.6)  		  	   		 	   		  		  		    	 		 		   		 		  
            permutation = np.random.permutation(alldata.shape[0])  		  	   		 	   		  		  		    	 		 		   		 		  
            col_permutation = np.random.permutation(alldata.shape[1] - 1)  		  	   		 	   		  		  		    	 		 		   		 		  
            train_data = alldata[permutation[:cutoff], :]  		  	   		 	   		  		  		    	 		 		   		 		  
            # train_x = train_data[:,:-1]
            train_x = train_data[:, col_permutation]
            train_y = train_data[:, -1]  		  	   		 	   		  		  		    	 		 		   		 		  
            test_data = alldata[permutation[cutoff:], :]  		  	   		 	   		  		  		    	 		 		   		 		  
            # test_x = test_data[:,:-1]
            test_x = test_data[:, col_permutation]
            test_y = test_data[:, -1]  		  	   		 	   		  		  		    	 		 		   		 		  
        msgs = []  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        if (group == "RTLearner") or (group == "DTLearner"):  		  	   		 	   		  		  		    	 		 		   		 		  
            clss_name = RTLearner if group == "RTLearner" else DTLearner  		  	   		 	   		  		  		    	 		 		   		 		  
            tree_sptc = 3 if group == "RTLearner" else 10  		  	   		 	   		  		  		    	 		 		   		 		  
            corr_in, corr_out, corr_in_50 = None, None, None  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
            def oneleaf():  		  	   		 	   		  		  		    	 		 		   		 		  
                np.random.seed(seed)  		  	   		 	   		  		  		    	 		 		   		 		  
                random.seed(seed)  		  	   		 	   		  		  		    	 		 		   		 		  
                np.random.seed = fake_seed  		  	   		 	   		  		  		    	 		 		   		 		  
                random.seed = fake_rseed  		  	   		 	   		  		  		    	 		 		   		 		  
                learner = clss_name(leaf_size=1, verbose=False)
                # print(train_x.shape)
                # print(train_y.shape)
                # print('tree is', learner)

                learner.add_evidence(train_x, train_y)
                # print('tree built')
                insample = learner.query(train_x)
                # print('train x is', train_x[0])
                # print('train y is', train_y[0])
                # print('test-x')
                # print(test_x)
                outsample = learner.query(test_x)

                np.random.seed = tmp_numpy_seed  		  	   		 	   		  		  		    	 		 		   		 		  
                random.seed = tmp_random_seed  		  	   		 	   		  		  		    	 		 		   		 		  
                author_rv = None  		  	   		 	   		  		  		    	 		 		   		 		  
                try:  		  	   		 	   		  		  		    	 		 		   		 		  
                    author_rv = learner.author()  		  	   		 	   		  		  		    	 		 		   		 		  
                except:  		  	   		 	   		  		  		    	 		 		   		 		  
                    pass  		  	   		 	   		  		  		    	 		 		   		 		  
                return insample, outsample, author_rv  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
            def fiftyleaves():  		  	   		 	   		  		  		    	 		 		   		 		  
                np.random.seed(seed)  		  	   		 	   		  		  		    	 		 		   		 		  
                random.seed(seed)  		  	   		 	   		  		  		    	 		 		   		 		  
                np.random.seed = fake_seed  		  	   		 	   		  		  		    	 		 		   		 		  
                random.seed = fake_rseed  		  	   		 	   		  		  		    	 		 		   		 		  
                learner = clss_name(leaf_size=50, verbose=False)  		  	   		 	   		  		  		    	 		 		   		 		  
                learner.add_evidence(train_x, train_y)  		  	   		 	   		  		  		    	 		 		   		 		  
                np.random.seed = tmp_numpy_seed  		  	   		 	   		  		  		    	 		 		   		 		  
                random.seed = tmp_random_seed  		  	   		 	   		  		  		    	 		 		   		 		  
                return learner.query(train_x)  		  	   		 	   		  		  		    	 		 		   		 		  

            pred_y_in, pred_y_out, author = run_with_timeout(

                oneleaf, tree_sptc, (), {}
            )
            # print(pred_y_in)
            # print(pred_y_out)
            # print(pred_y_in.shape)
            # print(train_y.shape)
            # # train_y = train_y.reshape(-1, 1)
            # print(pred_y_in.shape)
            # print(train_y.shape)
            pred_y_in_50 = run_with_timeout(fiftyleaves, tree_sptc, (), {})
            # print(pred_y_in.shape)
            # print(np.corrcoef(pred_y_in, y=train_y))
            #
            # print(np.corrcoef(pred_y_out, y=test_y))
            corr_in = np.corrcoef(pred_y_in, y=train_y)[0, 1]  		  	   		 	   		  		  		    	 		 		   		 		  
            corr_out = np.corrcoef(pred_y_out, y=test_y)[0, 1]  		  	   		 	   		  		  		    	 		 		   		 		  
            corr_in_50 = np.corrcoef(pred_y_in_50, y=train_y)[0, 1]  		  	   		 	   		  		  		    	 		 		   		 		  
            incorrect = False  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
            if corr_in < outputs["insample_corr_min"] or np.isnan(corr_in):
                print('corr in', corr_in)
                incorrect = True  		  	   		 	   		  		  		    	 		 		   		 		  
                msgs.append(  		  	   		 	   		  		  		    	 		 		   		 		  
                    "    In-sample with leaf_size=1 correlation less than"  		  	   		 	   		  		  		    	 		 		   		 		  
                    " allowed: got {} expected {}".format(  		  	   		 	   		  		  		    	 		 		   		 		  
                        corr_in, outputs["insample_corr_min"]  		  	   		 	   		  		  		    	 		 		   		 		  
                    )  		  	   		 	   		  		  		    	 		 		   		 		  
                )  		  	   		 	   		  		  		    	 		 		   		 		  
            else:  		  	   		 	   		  		  		    	 		 		   		 		  
                points_earned += 1.0  		  	   		 	   		  		  		    	 		 		   		 		  
            if corr_out < outputs["outsample_corr_min"] or np.isnan(corr_out):  		  	   		 	   		  		  		    	 		 		   		 		  
                incorrect = True  		  	   		 	   		  		  		    	 		 		   		 		  
                msgs.append(  		  	   		 	   		  		  		    	 		 		   		 		  
                    "    Out-of-sample correlation less than allowed: got {}"  		  	   		 	   		  		  		    	 		 		   		 		  
                    " expected {}".format(  		  	   		 	   		  		  		    	 		 		   		 		  
                        corr_out, outputs["outsample_corr_min"]  		  	   		 	   		  		  		    	 		 		   		 		  
                    )  		  	   		 	   		  		  		    	 		 		   		 		  
                )  		  	   		 	   		  		  		    	 		 		   		 		  
            else:  		  	   		 	   		  		  		    	 		 		   		 		  
                points_earned += 1.0  		  	   		 	   		  		  		    	 		 		   		 		  
            if corr_in_50 > outputs["insample_corr_max"] or np.isnan(  		  	   		 	   		  		  		    	 		 		   		 		  
                corr_in_50  		  	   		 	   		  		  		    	 		 		   		 		  
            ):  		  	   		 	   		  		  		    	 		 		   		 		  
                incorrect = True  		  	   		 	   		  		  		    	 		 		   		 		  
                msgs.append(  		  	   		 	   		  		  		    	 		 		   		 		  
                    "    In-sample correlation with leaf_size=50 greater than"  		  	   		 	   		  		  		    	 		 		   		 		  
                    " allowed: got {} expected {}".format(  		  	   		 	   		  		  		    	 		 		   		 		  
                        corr_in_50, outputs["insample_corr_max"]  		  	   		 	   		  		  		    	 		 		   		 		  
                    )  		  	   		 	   		  		  		    	 		 		   		 		  
                )  		  	   		 	   		  		  		    	 		 		   		 		  
            else:  		  	   		 	   		  		  		    	 		 		   		 		  
                points_earned += 1.0  		  	   		 	   		  		  		    	 		 		   		 		  
            # Check author string  		  	   		 	   		  		  		    	 		 		   		 		  
            if (author is None) or (author == "tb34"):  		  	   		 	   		  		  		    	 		 		   		 		  
                incorrect = True  		  	   		 	   		  		  		    	 		 		   		 		  
                msgs.append("    Invalid author: {}".format(author))  		  	   		 	   		  		  		    	 		 		   		 		  
                points_earned += -2.0  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        elif group == "BagLearner":  		  	   		 	   		  		  		    	 		 		   		 		  
            corr1, corr20 = None, None  		  	   		 	   		  		  		    	 		 		   		 		  
            bag_sptc = 10  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
            def onebag():  		  	   		 	   		  		  		    	 		 		   		 		  
                np.random.seed(seed)  		  	   		 	   		  		  		    	 		 		   		 		  
                random.seed(seed)  		  	   		 	   		  		  		    	 		 		   		 		  
                np.random.seed = fake_seed  		  	   		 	   		  		  		    	 		 		   		 		  
                random.seed = fake_rseed  		  	   		 	   		  		  		    	 		 		   		 		  
                learner1 = BagLearner(  		  	   		 	   		  		  		    	 		 		   		 		  
                    learner=RTLearner,  		  	   		 	   		  		  		    	 		 		   		 		  
                    kwargs={"leaf_size": 1},  		  	   		 	   		  		  		    	 		 		   		 		  
                    bags=1,  		  	   		 	   		  		  		    	 		 		   		 		  
                    boost=False,  		  	   		 	   		  		  		    	 		 		   		 		  
                    verbose=False,  		  	   		 	   		  		  		    	 		 		   		 		  
                )  		  	   		 	   		  		  		    	 		 		   		 		  
                learner1.add_evidence(train_x, train_y)  		  	   		 	   		  		  		    	 		 		   		 		  
                q_rv = learner1.query(test_x)  		  	   		 	   		  		  		    	 		 		   		 		  
                a_rv = learner1.author()  		  	   		 	   		  		  		    	 		 		   		 		  
                np.random.seed = tmp_numpy_seed  		  	   		 	   		  		  		    	 		 		   		 		  
                random.seed = tmp_random_seed  		  	   		 	   		  		  		    	 		 		   		 		  
                return q_rv, a_rv  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
            def twentybags():  		  	   		 	   		  		  		    	 		 		   		 		  
                np.random.seed(seed)  		  	   		 	   		  		  		    	 		 		   		 		  
                random.seed(seed)  		  	   		 	   		  		  		    	 		 		   		 		  
                np.random.seed = fake_seed  		  	   		 	   		  		  		    	 		 		   		 		  
                random.seed = fake_rseed  		  	   		 	   		  		  		    	 		 		   		 		  
                learner20 = BagLearner(  		  	   		 	   		  		  		    	 		 		   		 		  
                    learner=RTLearner,  		  	   		 	   		  		  		    	 		 		   		 		  
                    kwargs={"leaf_size": 1},  		  	   		 	   		  		  		    	 		 		   		 		  
                    bags=20,  		  	   		 	   		  		  		    	 		 		   		 		  
                    boost=False,  		  	   		 	   		  		  		    	 		 		   		 		  
                    verbose=False,  		  	   		 	   		  		  		    	 		 		   		 		  
                )  		  	   		 	   		  		  		    	 		 		   		 		  
                learner20.add_evidence(train_x, train_y)  		  	   		 	   		  		  		    	 		 		   		 		  
                q_rv = learner20.query(test_x)  		  	   		 	   		  		  		    	 		 		   		 		  
                np.random.seed = tmp_numpy_seed  		  	   		 	   		  		  		    	 		 		   		 		  
                random.seed = tmp_random_seed  		  	   		 	   		  		  		    	 		 		   		 		  
                return q_rv  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
            pred_y_1, author = run_with_timeout(  		  	   		 	   		  		  		    	 		 		   		 		  
                onebag, bag_sptc, pos_args=(), keyword_args={}  		  	   		 	   		  		  		    	 		 		   		 		  
            )  		  	   		 	   		  		  		    	 		 		   		 		  
            pred_y_20 = run_with_timeout(twentybags, bag_sptc, (), {})  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
            corr1 = np.corrcoef(pred_y_1, test_y)[0, 1]  		  	   		 	   		  		  		    	 		 		   		 		  
            corr20 = np.corrcoef(pred_y_20, test_y)[0, 1]  		  	   		 	   		  		  		    	 		 		   		 		  
            incorrect = False  		  	   		 	   		  		  		    	 		 		   		 		  
            # msgs = []  		  	   		 	   		  		  		    	 		 		   		 		  
            if corr20 <= corr1:  		  	   		 	   		  		  		    	 		 		   		 		  
                incorrect = True  		  	   		 	   		  		  		    	 		 		   		 		  
                msgs.append(  		  	   		 	   		  		  		    	 		 		   		 		  
                    "    Out-of-sample correlation for 20 bags is not greater"  		  	   		 	   		  		  		    	 		 		   		 		  
                    " than for 1 bag. 20 bags:{}, 1 bag:{}".format(  		  	   		 	   		  		  		    	 		 		   		 		  
                        corr20, corr1  		  	   		 	   		  		  		    	 		 		   		 		  
                    )  		  	   		 	   		  		  		    	 		 		   		 		  
                )  		  	   		 	   		  		  		    	 		 		   		 		  
            else:  		  	   		 	   		  		  		    	 		 		   		 		  
                points_earned += 2.0  		  	   		 	   		  		  		    	 		 		   		 		  
            # Check author string  		  	   		 	   		  		  		    	 		 		   		 		  
            if (author is None) or (author == "tb34"):  		  	   		 	   		  		  		    	 		 		   		 		  
                incorrect = True  		  	   		 	   		  		  		    	 		 		   		 		  
                msgs.append("    Invalid author: {}".format(author))  		  	   		 	   		  		  		    	 		 		   		 		  
                points_earned += -1.0  		  	   		 	   		  		  		    	 		 		   		 		  
        elif group == "InsaneLearner":  		  	   		 	   		  		  		    	 		 		   		 		  
            try:  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
                def insane():  		  	   		 	   		  		  		    	 		 		   		 		  
                    import InsaneLearner as it  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
                    learner = it.InsaneLearner(verbose=False)  		  	   		 	   		  		  		    	 		 		   		 		  
                    learner.add_evidence(train_x, train_y)  		  	   		 	   		  		  		    	 		 		   		 		  
                    y = learner.query(test_x)  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
                run_with_timeout(insane, 10, pos_args=(), keyword_args={})  		  	   		 	   		  		  		    	 		 		   		 		  
                incorrect = False  		  	   		 	   		  		  		    	 		 		   		 		  
            except Exception as e:  		  	   		 	   		  		  		    	 		 		   		 		  
                incorrect = True  		  	   		 	   		  		  		    	 		 		   		 		  
                msgs.append(  		  	   		 	   		  		  		    	 		 		   		 		  
                    "    Exception calling InsaneLearner: {}".format(e)  		  	   		 	   		  		  		    	 		 		   		 		  
                )  		  	   		 	   		  		  		    	 		 		   		 		  
                points_earned = -10  		  	   		 	   		  		  		    	 		 		   		 		  
        elif group == "RandomName":  		  	   		 	   		  		  		    	 		 		   		 		  
            try:  		  	   		 	   		  		  		    	 		 		   		 		  
                il_name, il_code = gen_class()  		  	   		 	   		  		  		    	 		 		   		 		  
                exec(il_code) in globals(), locals()  		  	   		 	   		  		  		    	 		 		   		 		  
                il_cobj = eval(il_name)  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
                def rnd_name():  		  	   		 	   		  		  		    	 		 		   		 		  
                    np.random.seed(seed)  		  	   		 	   		  		  		    	 		 		   		 		  
                    random.seed(seed)  		  	   		 	   		  		  		    	 		 		   		 		  
                    np.random.seed = fake_seed  		  	   		 	   		  		  		    	 		 		   		 		  
                    random.seed = fake_rseed  		  	   		 	   		  		  		    	 		 		   		 		  
                    learner = BagLearner(  		  	   		 	   		  		  		    	 		 		   		 		  
                        learner=il_cobj,  		  	   		 	   		  		  		    	 		 		   		 		  
                        kwargs={"verbose": False},  		  	   		 	   		  		  		    	 		 		   		 		  
                        bags=20,  		  	   		 	   		  		  		    	 		 		   		 		  
                        boost=False,  		  	   		 	   		  		  		    	 		 		   		 		  
                        verbose=False,  		  	   		 	   		  		  		    	 		 		   		 		  
                    )  		  	   		 	   		  		  		    	 		 		   		 		  
                    learner.add_evidence(train_x, train_y)  		  	   		 	   		  		  		    	 		 		   		 		  
                    y = learner.query(test_x)  		  	   		 	   		  		  		    	 		 		   		 		  
                    np.random.seed = tmp_numpy_seed  		  	   		 	   		  		  		    	 		 		   		 		  
                    random.seed = tmp_random_seed  		  	   		 	   		  		  		    	 		 		   		 		  
                    return (  		  	   		 	   		  		  		    	 		 		   		 		  
                        il_cobj.init_callcount_dict,  		  	   		 	   		  		  		    	 		 		   		 		  
                        il_cobj.add_callcount_dict,  		  	   		 	   		  		  		    	 		 		   		 		  
                        il_cobj.query_callcount_dict,  		  	   		 	   		  		  		    	 		 		   		 		  
                    )  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
                iccd, accd, qccd = run_with_timeout(  		  	   		 	   		  		  		    	 		 		   		 		  
                    rnd_name, 10, pos_args=(), keyword_args={}  		  	   		 	   		  		  		    	 		 		   		 		  
                )  		  	   		 	   		  		  		    	 		 		   		 		  
                incorrect = False  		  	   		 	   		  		  		    	 		 		   		 		  
                if (len(iccd) != 20) or (any([v != 1 for v in iccd.values()])):  		  	   		 	   		  		  		    	 		 		   		 		  
                    incorrect = True  		  	   		 	   		  		  		    	 		 		   		 		  
                    msgs.append(  		  	   		 	   		  		  		    	 		 		   		 		  
                        "    Unexpected number of calls to __init__, sum={}"  		  	   		 	   		  		  		    	 		 		   		 		  
                        " (should be 20), max={} (should be 1), min={} (should"  		  	   		 	   		  		  		    	 		 		   		 		  
                        " be 1)".format(  		  	   		 	   		  		  		    	 		 		   		 		  
                            len(iccd), max(iccd.values()), min(iccd.values())  		  	   		 	   		  		  		    	 		 		   		 		  
                        )  		  	   		 	   		  		  		    	 		 		   		 		  
                    )  		  	   		 	   		  		  		    	 		 		   		 		  
                    points_earned = -10  		  	   		 	   		  		  		    	 		 		   		 		  
                if (len(accd) != 20) or (any([v != 1 for v in accd.values()])):  		  	   		 	   		  		  		    	 		 		   		 		  
                    incorrect = True  		  	   		 	   		  		  		    	 		 		   		 		  
                    msgs.append(  		  	   		 	   		  		  		    	 		 		   		 		  
                        "    Unexpected number of calls to add_evidence sum={}"  		  	   		 	   		  		  		    	 		 		   		 		  
                        " (should be 20), max={} (should be 1), min={} (should"  		  	   		 	   		  		  		    	 		 		   		 		  
                        " be 1)".format(  		  	   		 	   		  		  		    	 		 		   		 		  
                            len(accd), max(accd.values()), min(accd.values())  		  	   		 	   		  		  		    	 		 		   		 		  
                        )  		  	   		 	   		  		  		    	 		 		   		 		  
                    )  		  	   		 	   		  		  		    	 		 		   		 		  
                    points_earned = -10  		  	   		 	   		  		  		    	 		 		   		 		  
                if (len(qccd) != 20) or (any([v != 1 for v in qccd.values()])):  		  	   		 	   		  		  		    	 		 		   		 		  
                    incorrect = True  		  	   		 	   		  		  		    	 		 		   		 		  
                    msgs.append(  		  	   		 	   		  		  		    	 		 		   		 		  
                        "    Unexpected number of calls to query, sum={}"  		  	   		 	   		  		  		    	 		 		   		 		  
                        " (should be 20), max={} (should be 1), min={} (should"  		  	   		 	   		  		  		    	 		 		   		 		  
                        " be 1)".format(  		  	   		 	   		  		  		    	 		 		   		 		  
                            len(qccd), max(qccd.values()), min(qccd.values())  		  	   		 	   		  		  		    	 		 		   		 		  
                        )  		  	   		 	   		  		  		    	 		 		   		 		  
                    )  		  	   		 	   		  		  		    	 		 		   		 		  
                    points_earned = -10  		  	   		 	   		  		  		    	 		 		   		 		  
            except Exception as e:  		  	   		 	   		  		  		    	 		 		   		 		  
                incorrect = True  		  	   		 	   		  		  		    	 		 		   		 		  
                msgs.append("   Exception calling BagLearner: {}".format(e))  		  	   		 	   		  		  		    	 		 		   		 		  
                points_earned = -10  		  	   		 	   		  		  		    	 		 		   		 		  
        if incorrect:  		  	   		 	   		  		  		    	 		 		   		 		  
            inputs_str = "    data file: {}\n    permutation: {}".format(  		  	   		 	   		  		  		    	 		 		   		 		  
                datafile, permutation  		  	   		 	   		  		  		    	 		 		   		 		  
            )  		  	   		 	   		  		  		    	 		 		   		 		  
            raise IncorrectOutput(  		  	   		 	   		  		  		    	 		 		   		 		  
                "Test failed on one or more output criteria.\n  Inputs:\n{}\n "  		  	   		 	   		  		  		    	 		 		   		 		  
                " Failures:\n{}".format(inputs_str, "\n".join(msgs))  		  	   		 	   		  		  		    	 		 		   		 		  
            )  		  	   		 	   		  		  		    	 		 		   		 		  
    except Exception as e:  		  	   		 	   		  		  		    	 		 		   		 		  
        # Test result: failed  		  	   		 	   		  		  		    	 		 		   		 		  
        msg = "Description: {} (group: {})\n".format(description, group)  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        # Generate a filtered stacktrace, only showing erroneous lines in student file(s)  		  	   		 	   		  		  		    	 		 		   		 		  
        tb_list = tb.extract_tb(sys.exc_info()[2])  		  	   		 	   		  		  		    	 		 		   		 		  
        for i in range(len(tb_list)):  		  	   		 	   		  		  		    	 		 		   		 		  
            row = tb_list[i]  		  	   		 	   		  		  		    	 		 		   		 		  
            tb_list[i] = (  		  	   		 	   		  		  		    	 		 		   		 		  
                os.path.basename(row[0]),  		  	   		 	   		  		  		    	 		 		   		 		  
                row[1],  		  	   		 	   		  		  		    	 		 		   		 		  
                row[2],  		  	   		 	   		  		  		    	 		 		   		 		  
                row[3],  		  	   		 	   		  		  		    	 		 		   		 		  
            )  # show only filename instead of long absolute path  		  	   		 	   		  		  		    	 		 		   		 		  
        tb_list = [  		  	   		 	   		  		  		    	 		 		   		 		  
            row  		  	   		 	   		  		  		    	 		 		   		 		  
            for row in tb_list  		  	   		 	   		  		  		    	 		 		   		 		  
            if (row[0] == "RTLearner.py") or (row[0] == "BagLearner.py")  		  	   		 	   		  		  		    	 		 		   		 		  
        ]  		  	   		 	   		  		  		    	 		 		   		 		  
        if tb_list:  		  	   		 	   		  		  		    	 		 		   		 		  
            msg += "Traceback:\n"  		  	   		 	   		  		  		    	 		 		   		 		  
            msg += "".join(tb.format_list(tb_list))  # contains newlines  		  	   		 	   		  		  		    	 		 		   		 		  
        msg += "{}: {}".format(e.__class__.__name__, str(e))  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
        # Report failure result to grader, with stacktrace  		  	   		 	   		  		  		    	 		 		   		 		  
        grader.add_result(  		  	   		 	   		  		  		    	 		 		   		 		  
            GradeResult(outcome="failed", points=points_earned, msg=msg)  		  	   		 	   		  		  		    	 		 		   		 		  
        )  		  	   		 	   		  		  		    	 		 		   		 		  
        raise  		  	   		 	   		  		  		    	 		 		   		 		  
    else:  		  	   		 	   		  		  		    	 		 		   		 		  
        # Test result: passed (no exceptions)  		  	   		 	   		  		  		    	 		 		   		 		  
        grader.add_result(  		  	   		 	   		  		  		    	 		 		   		 		  
            GradeResult(outcome="passed", points=points_earned, msg=None)  		  	   		 	   		  		  		    	 		 		   		 		  
        )  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
def gen_class():  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def = "class {}(object):\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += "    foo=4\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += "    init_callcount_dict=dict()\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += "    add_callcount_dict=dict()\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += "    query_callcount_dict=dict()\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += "    def __init__(self,**kwargs):\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += "        self.ctor_args = kwargs\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += (  		  	   		 	   		  		  		    	 		 		   		 		  
        "        self.init_callcount_dict[str(self)] ="  		  	   		 	   		  		  		    	 		 		   		 		  
        " self.init_callcount_dict.get(str(self),0)+1\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    )  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += (  		  	   		 	   		  		  		    	 		 		   		 		  
        "        if ('verbose' in self.ctor_args) and"  		  	   		 	   		  		  		    	 		 		   		 		  
        " (self.ctor_args['verbose']==True):\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    )  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += "            print('creating class')\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += "    def add_evidence(self,train_x,train_y):\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += "        self.train_x = train_x\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += "        self.train_y = train_y\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += (  		  	   		 	   		  		  		    	 		 		   		 		  
        "        self.add_callcount_dict[str(self)] ="  		  	   		 	   		  		  		    	 		 		   		 		  
        " self.add_callcount_dict.get(str(self),0)+1\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    )  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += (  		  	   		 	   		  		  		    	 		 		   		 		  
        "        if ('verbose' in self.ctor_args) and"  		  	   		 	   		  		  		    	 		 		   		 		  
        " (self.ctor_args['verbose']==True):\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    )  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += "            print('add_evidence()')\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += "    def query(self,test_x):\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += "        rv = np.zeros(len(test_x))\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += "        rv[:] = self.train_y.mean()\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += (  		  	   		 	   		  		  		    	 		 		   		 		  
        "        self.query_callcount_dict[str(self)] ="  		  	   		 	   		  		  		    	 		 		   		 		  
        " self.query_callcount_dict.get(str(self),0)+1\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    )  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += (  		  	   		 	   		  		  		    	 		 		   		 		  
        "        if ('verbose' in self.ctor_args) and"  		  	   		 	   		  		  		    	 		 		   		 		  
        " (self.ctor_args['verbose']==True):\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    )  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += "            print('query()')\n"  		  	   		 	   		  		  		    	 		 		   		 		  
    c_def += "        return rv"  		  	   		 	   		  		  		    	 		 		   		 		  
    c_name = "".join(  		  	   		 	   		  		  		    	 		 		   		 		  
        np.random.permutation(np.array(tuple(string.ascii_letters)))[  		  	   		 	   		  		  		    	 		 		   		 		  
            :10  		  	   		 	   		  		  		    	 		 		   		 		  
        ].tolist()  		  	   		 	   		  		  		    	 		 		   		 		  
    )  		  	   		 	   		  		  		    	 		 		   		 		  
    return c_name, c_def.format(c_name)  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
def fake_seed(*args):  		  	   		 	   		  		  		    	 		 		   		 		  
    pass  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
def fake_rseed(*args):  		  	   		 	   		  		  		    	 		 		   		 		  
    pass  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
  		  	   		 	   		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		 	   		  		  		    	 		 		   		 		  
    pytest.main(["-s", __file__])  		  	   		 	   		  		  		    	 		 		   		 		  
