# This script is shared with permission of our TAs for CS6601 ML4T Fall 2024
# it should help you compare the performance of DTLearner and LinRegLearner
# feel free change this script as you see fit
# the scrip will generate two images best_4_dt.png best_4_lin_reg.png 


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

    # Plot the results
    plt.plot(range(num_iterations), rmse_dt, label='DTLearner')
    plt.plot(range(num_iterations), rmse_lr, label='LinRegLearner')
    #make x axis integer
    plt.xticks(range(0, num_iterations, 10))
    
    plt.xlabel('Iteration Number')
    plt.ylabel('RMSE')
    plt.legend()
    plt.title(f'RMSE of DTLearner and LinRegLearner over Iterations ({func_name})')
    
    
    plt.text(
        0.5, .15,               # Position in the plot (x, y in data coordinates)
        'your_email@gatech.edu', # Watermark text
        fontsize=40,             # Font size
        color='gray',            # Text color
        alpha=0.5,               # Transparency level
        ha='center',             # Horizontal alignment
        va='center',             # Vertical alignment
        rotation=5,             # Rotation of the text (in degrees)
        transform=plt.gcf().transFigure  # Use figure coordinates for placement
    )
    # plt.savefig(f'{func_name}.png')
    plt.show()
    plt.close()

if __name__ == "__main__":
    num_iterations = 100
    evaluate_learners(num_iterations, gen_data.best_4_lin_reg, 'best_4_lin_reg')
    evaluate_learners(num_iterations, gen_data.best_4_dt, 'best_4_dt')