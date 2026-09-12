import torch
from torchvision import transforms, datasets

def cifar10_dataset(root):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    trainset = datasets.CIFAR10(root=root, train=True, download=True, transform=transform)
    testset = datasets.CIFAR10(root=root, train=False, download=True, transform=transform)
    return trainset, testset

def identity_fxn(df):
    return df


