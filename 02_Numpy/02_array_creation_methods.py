import numpy as np

# Arrays Creation using Numpy Arrays Methods


# ----------------------------------

# Np.Zeros or Zeros Matrix

# 1D
bias_vector = np.zeros(5)

# 2D
black_image_canvas = np.zeros((4,4))

print(bias_vector)
print(black_image_canvas)
print("------------")

# ----------------------------------

# Np.Ones or Ones Matrix

# 1D
weight_initialization = np.ones(3)

# 2D
multiplier_matrix = np.ones((3,3))

print(weight_initialization)
print(multiplier_matrix)
print("------------")

# ----------------------------------

# Np.Full or Custom Number Matrix

grey_image = np.full((5,5), 128)

print(grey_image)
print("------------")

# ----------------------------------

# Np. Eye or Identity Matrix

one_hot_matrix = np.eye(4)

print(one_hot_matrix)
print("------------")

# ----------------------------------

# Np.Arrange and Np.Linspace or Sequences

epochs_checkpoints = np.arange(10,52,2)

probability_thresholds = np.linspace(0,1,10)

print(epochs_checkpoints)
print(probability_thresholds)
print("------------")