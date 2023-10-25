import numpy as np
import os

'''
GLM on toy data
'''

if __name__ == '__main__':

    num_samples = 100
    num_trials  = 1
    
    # Create toy data
    X = np.random.randn(num_trials, num_samples)
    Y = X + np.random.randn(num_trials, num_samples)

    # Run GLM
    B = np.linalg.inv(X.dot(X.T)).dot(X).dot(Y.T)

    import pylab as plt
    
    plt.figure()
    plt.scatter(X.T, Y)
    plt.plot(X.T, B*X.T, 'r')
    plt.show()