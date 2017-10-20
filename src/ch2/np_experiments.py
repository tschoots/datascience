import numpy as np
np.random.seed(0)  # seed for reproducibility

def main():
    print("hallo")

    x1 = np.random.randint(10, size=6)  # one dimensional array
    x2 = np.random.randint(10, size=(3,4))  # two dimensional array
    # x3 = np.random.randint(10, size=(3500,450,4500)) # three dimensional array which will take 56.7 GB out of RAM!
    x3 = np.random.randint(10, size=(3, 4, 5))  # three dimensional array

    print(x3)
    print("x3 ndim: " , x3.ndim)
    print("x3 shape: " , x3.shape)
    print("x3 size: ", x3.size)
    print("x3 dtype: ", x3.dtype)
    print("x3 itemsize : ", x3.itemsize, "bytes")
    print("x3 nbytes : ", x3.nbytes/1000000000, "GBytes")
    print("x3 nbytes : ", x3.nbytes , "bytes")

if __name__ == "__main__":
    main()