# This script is shared with permission of our TAs for CS6601 ML4T Fall 2024
# it should help you compare the performance of DTLearner and LinRegLearner

import numpy as np
import matplotlib.pyplot as plt
from DTLearner import DTLearner 
from LinRegLearner import LinRegLearner  
import random as random #this is not needed if you rely on Numpy's random
import gen_data  

def calculate_rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_true - y_pred) ** 2))

def evaluate_learners(num_iterations, data_gen_func, func_name):
    rmse_dt = []
    rmse_lr = []

    for i in range(num_iterations):
        np.random.seed(i)
        random.seed(i) #this is not needed if you rely on Numpy's random
        
        # Generate data
        X, y = data_gen_func(i)  # Use the provided data generation function
        
        # Split the data
        split_index = int(0.6 * len(X))
        X_train, X_test = X[:split_index], X[split_index:]
        y_train, y_test = y[:split_index], y[split_index:]
        
        # Train DTLearner
        deterministic_learner = DTLearner()
        deterministic_learner.add_evidence(X_train, y_train)
        
        # Train LinRegLearner
        linreg_learner = LinRegLearner()
        linreg_learner.add_evidence(X_train, y_train)
        
        # Test DTLearner
        y_pred_dt = deterministic_learner.query(X_test)
        rmse_dt.append(calculate_rmse(y_test, y_pred_dt))
        
        # Test LinRegLearner
        y_pred_lr = linreg_learner.query(X_test)
        rmse_lr.append(calculate_rmse(y_test, y_pred_lr))
        
        #keep percentage of which one has lower rmse
        dt_better = sum([1 for i in range(len(rmse_dt)) if rmse_dt[i] < rmse_lr[i]]) / len(rmse_dt)
        lr_better = sum([1 for i in range(len(rmse_lr)) if rmse_lr[i] < rmse_dt[i]]) / len(rmse_lr)
        percent_deter_better = dt_better / (dt_better + lr_better)
        percent_lin_better = lr_better / (dt_better + lr_better)        
        
        

    # Plot the results (scatter plot)
    # plt.scatter(range(num_iterations), rmse_dt, label=f'DTLearner {percent_deter_better:.1%}', alpha=0.5, s=3)
    # plt.scatter(range(num_iterations), rmse_lr, label=f'LinRegLearner {percent_lin_better:.1%}', alpha=0.5, s=3)
    
    # Plot the results (line plot)
    plt.plot(range(num_iterations), rmse_dt, label=f'DTLearner {percent_deter_better:.1%}', alpha=0.5)
    plt.plot(range(num_iterations), rmse_lr, label=f'LinRegLearner {percent_lin_better:.1%}', alpha=0.5)
    #make x axis integer
    # plt.xticks(range(0, num_iterations, 10))
    plt.xlim(0, num_iterations)
    plt.ylim(0)
    
    plt.xlabel('Iteration Number')
    plt.ylabel('RMSE')
    plt.legend()
    plt.title(f'RMSE of DTLearner and LinRegLearner over Iterations ({func_name})')
    
    
    plt.text(
        0.5, .15,               # Position in the plot (x, y in data coordinates)
        'benhizak@gatech.edu', # Watermark text
        fontsize=40,             # Font size
        color='gray',            # Text color
        alpha=0.5,               # Transparency level
        ha='center',             # Horizontal alignment
        va='center',             # Vertical alignment
        rotation=5,             # Rotation of the text (in degrees)
        transform=plt.gcf().transFigure  # Use figure coordinates for placement
    )
    plt.savefig(f'{func_name}.png')
    plt.close()
    
    
    #create another graph that shows the percentage of time each learner is better
    plt.bar(['DTLearner', 'LinRegLearner'], [dt_better, lr_better])
    plt.ylim(0, 1)
    plt.ylabel('Percentage of Time Better')
    plt.title(f'Percentage of Time Each Learner is Better ({func_name})')
    plt.savefig(f'{func_name}_percent.png')
    plt.close()
    
    
def test_seed_consistency(data_gen_func, seed, num_tests):
    results = [data_gen_func(seed) for _ in range(num_tests)]
    for i in range(1, num_tests):
        assert np.array_equal(results[0][0], results[i][0]), "X values are not consistent"
        assert np.array_equal(results[0][1], results[i][1]), "Y values are not consistent"
    print(f"Seed consistency test passed for {data_gen_func.__name__}\t\txxwith seed {seed}")

if __name__ == "__main__":
    num_iterations = 50
    evaluate_learners(num_iterations, gen_data.best_4_lin_reg, 'best_4_lin_reg')
    evaluate_learners(num_iterations, gen_data.best_4_dt, 'best_4_dt')
    NUM_TESTS_SEED = 3
    # Test seed consistency
    for i in range(20):
        seed = np.random.randint(1, 1000000)
        test_seed_consistency(gen_data.best_4_lin_reg, seed, NUM_TESTS_SEED)
        test_seed_consistency(gen_data.best_4_dt, seed, NUM_TESTS_SEED)