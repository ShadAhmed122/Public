import matplotlib as plt
import numpy as np
from sklearn import datasets, linear_model
a =datasets.load_diabetes()
print(a.keys())
# dict_keys(['data', 'target', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])
print(a.data)
