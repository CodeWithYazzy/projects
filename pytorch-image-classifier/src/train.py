import torch, torchvision, torchvision.transforms as T
from model import SimpleCNN
# Minimal demo — loads CIFAR-10, 1 epoch, prints shapes
transform = T.Compose([T.ToTensor(), T.Normalize((0.5,),(0.5,))])
ds = torchvision.datasets.CIFAR10(root="./data", train=True, download=True, transform=transform)
dl = torch.utils.data.DataLoader(ds, batch_size=64, shuffle=True)
model = SimpleCNN()
x, y = next(iter(dl))
print(f"Batch {x.shape} {y.shape}, model {model(x[:2]).shape}")
print("Training loop ready — see README for full run.")
