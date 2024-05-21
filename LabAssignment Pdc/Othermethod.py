#Muhammad Soban Rasheed
#Danish Nasar
#Khubaib ur rehman

import random
import multiprocessing as mp
import time

# Define matrix and vector sizes
matrix_size = 800
vector_size = 800

# Function to perform the matrix-vector product
def vector_matrix_product(args):
    # Unpack the tuple (A_row, B)
    A_row, B = args
    # Calculate the dot product without NumPy
    dot_product = sum(A_row[j] * B[j] for j in range(vector_size))
    return dot_product

def main():
    # Initialize matrix A and vector B with random values
    A = [[random.random() for _ in range(vector_size)] for _ in range(matrix_size)]
    B = [random.random() for _ in range(vector_size)]
    
    # Initialize result vector C
    C = [0] * matrix_size
    
    # List of multiprocessing methods to be used
    methods = ['Apply', 'Apply_Async', 'Map', 'Map_Async']
    
    # Perform the calculations using each method and measure execution time
    for method in methods:
        start_time = time.time()
        
        if method == 'Apply':
            with mp.Pool(processes=4) as pool:
                for i in range(matrix_size):
                    C[i] = pool.apply(vector_matrix_product, args=((A[i], B),))
        
        elif method == 'Apply_Async':
            with mp.Pool(processes=4) as pool:
                results = [pool.apply_async(vector_matrix_product, args=((A[i], B),)) for i in range(matrix_size)]
                C = [result.get() for result in results]
        
        elif method == 'Map':
            with mp.Pool(processes=4) as pool:
                C = pool.map(vector_matrix_product, [(A[i], B) for i in range(matrix_size)])
        
        elif method == 'Map_Async':
            with mp.Pool(processes=4) as pool:
                results = pool.map_async(vector_matrix_product, [(A[i], B) for i in range(matrix_size)])
                C = results.get()
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"Method: {method}, Execution Time: {execution_time:.6f} seconds")

if __name__ == '__main__':
    main()
