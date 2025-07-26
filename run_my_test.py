import numpy as np

np.random.seed(42)

print(np.random.randn(2, 3))

import numpy as np
np.random.seed(42)

data1 = np.array([2,3,4])
data2 = np.array([2,3,4])
data3 = np.vstack((data1,data2))
print(data3)
