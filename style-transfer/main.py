import torch
import numpy as np
import torch.nn as nn
import torchvision
import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('--lr', type=float, default=1e-3)
parser.add_argument('--step', type=int, default=100)


class VggNet(nn.Module):
    def __init__(self):
        super(VggNet, self).__init__()

    def forward(self, x):
        pass


def image_formatter(image, size, ):
    pass


def train_image():
    pass


if __name__ == "__main__":
    pass