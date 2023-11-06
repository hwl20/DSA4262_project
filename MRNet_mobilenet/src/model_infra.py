import torch
from model import MRNet

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = MRNet().to(device)
print(model)