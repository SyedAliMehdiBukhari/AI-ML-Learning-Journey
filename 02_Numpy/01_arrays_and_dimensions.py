import numpy as np

# Creating a 1D array

house_prices = np.array([250000, 300000, 150000])

print(house_prices.ndim)
print(house_prices.shape)
print(house_prices.dtype)
print(house_prices.size)

# Creating a 2D array

house_features = np.array([[1,3,1500], [2,4,2000], [3,2,900]])

print(house_features.ndim)
print(house_features.shape)
print(house_features.dtype)
print(house_features.size)