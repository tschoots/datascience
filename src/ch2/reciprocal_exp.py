import numpy as np
np.random.seed(0)

import time


def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        #output[i] = 1.0 / values[i]
        output[i] = np.divide(1.0 , values[i])
        #output[i] = 1
    return output

def test():
    L = [i for i in range(100)]

def main():
    values = np.random.randint(1, 10, size=5000000)
    start = time.time()
    output = compute_reciprocals(values)
    end = time.time()
    print("execution time compute_reciprocal : %r" %( end - start ))
    start = time.time()
    output = 1.0 / values
    end = time.time()
    print("np bewerking : %r" % (end - start))
    print(values)
    print("reciprocal :")
    print(output)

    # another perf measure
    x = np.arange(9).reshape((3,3))
    start = time.time()
    2 ** x
    end = time.time()
    print("2 ** x : %r" % (end - start))
    start = time.time()
    np.power(2, x)
    end = time.time()
    print("np.power(2,x) : %r" %(end - start))



if __name__ == "__main__":
    main()