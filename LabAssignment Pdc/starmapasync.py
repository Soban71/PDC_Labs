import random
import asyncio
from multiprocessing import Pool
import time

# Function to perform matrix-vector multiplication
def mat_vec_mult(args):
    A, B, i = args
    result = sum(A[i][j] * B[j] for j in range(len(B)))
    return result

async def main():
    # Generating random matrix A and vector B
    A = [[random.random() for _ in range(200)] for _ in range(200)]
    B = [random.random() for _ in range(200)]

    num_processes = 4
    pool = Pool(processes=num_processes)
    
    # Creating inputs for multiprocessing
    inputs = [(A, B, i) for i in range(200)]
    
    start_time = time.time()
    # Performing matrix-vector multiplication using multiprocessing asynchronously
    loop = asyncio.get_event_loop()
    results = await asyncio.gather(*(loop.run_in_executor(None, mat_vec_mult, args) for args in inputs))
    end_time = time.time()
    
    print("Multiplication Execution Time:", end_time - start_time)

if __name__ == '__main__':
    asyncio.run(main())
