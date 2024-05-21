import numpy as np
from multiprocessing import Pool
import time

# Function to perform matrix-vector multiplication
def mat_vec_mult(args):
    A, B, i = args
    return np.dot(A[i], B)

if __name__ == '__main__':
    # Generating random matrix A and vector B
    A = np.random.rand(200, 200)
    B = np.random.rand(200)

    num_processes = 4
    pool = Pool(processes=num_processes)
    
    # Creating inputs for multiprocessing
    inputs = [(A, B, i) for i in range(200)]
    
    start_time = time.time()
    # Performing matrix-vector multiplication using multiprocessing
    results = pool.map(mat_vec_mult, inputs)
    end_time = time.time()
    
    print("Multiplication Execution Time:", end_time - start_time)