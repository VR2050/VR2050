import torch 
import time 
import cv2
import numpy as np
X=np.array([x for x in range(30)])
X=torch.from_numpy(X)
print(X,X.shape)
model=torch.nn.Linear(1,1)  