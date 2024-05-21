#Muhammad Soban Rasheed
#Danish Nasar
#Khubaib ur rehman


import random
import time

# Function to perform matrix-vector multiplication for a specific row
def mat_vec_mult(A, B, i):
    dot_product = sum(A[i][j] * B[j] for j in range(len(B)))
    return dot_product

def main():
    # Generating random matrix A and vector B
    A = [[random.random() for _ in range(800)] for _ in range(800)]
    B = [random.random() for _ in range(800)]
    
    # Warm-up phase to ensure any initial overhead is avoided
    for i in range(10):
        mat_vec_mult(A, B, i)
    
    # Start measuring time
    start_time = time.perf_counter()  # Using time.perf_counter() for precision
    
    # Perform matrix-vector multiplication sequentially
    for i in range(800):
        mat_vec_mult(A, B, i)
    
    # End measuring time
    end_time = time.perf_counter()  # Using time.perf_counter() for precision
    
    # Calculate execution time
    execution_time = end_time - start_time
    
    # Print execution time
    print(f"Serial Execution Time: {execution_time:.8f} seconds")

if __name__ == '__main__':
    main()
