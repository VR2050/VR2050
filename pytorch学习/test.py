import torch 
import numpy as np 
a=torch.randn(4,3,requires_grad=True)
b=torch.randn(4,3,requires_grad=True)
y=a+b
print(y.sum())
print(y)
