import torch
from torch.testing._internal.common_utils import TestCase
from torch.testing._internal.optests import opcheck
import unittest
import extension_cpp
from torch import Tensor
from typing import Tuple
import torch.nn.functional as F
import torch.nn as nn

print(torch.initial_seed())

# size = 32
# a1 = torch.randn(size, device='cuda')
# a2 = torch.randn(size, device='cuda')
# out = extension_cpp.ops.mymuladd(a1,a2,3.0)
# print(out)

m = 33
n = 34 
k = 35 
b1 = torch.randn((m,k),device='cuda')
b2 = torch.randn((k,n),device='cuda')
c1  = extension_cpp.ops.mysgemm(b1,b2,1.0,0.0)
print(c1)
print(b1@b2)