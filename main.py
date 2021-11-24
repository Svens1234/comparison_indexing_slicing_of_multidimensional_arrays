import numpy as np

two_dim_arr =np.arange(12).reshape(3,4)
print(two_dim_arr)
print(two_dim_arr[1][1])
print(two_dim_arr[1,1])
print(two_dim_arr[2][1])
print(two_dim_arr[2,1])
print(two_dim_arr[0:2,0:2])
print(two_dim_arr[:2,:2])
print(two_dim_arr[:2,2:4])
print(two_dim_arr[:2,2:])
print(two_dim_arr[two_dim_arr>4])
