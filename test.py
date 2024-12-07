import torch
print(torch.__version__)
print(torch.cuda.is_available())  # Should be False on macOS without GPU
print(torch.backends.mps.is_available())  # Should be True on Apple Silicon