import torch
import cv2
import numpy as np


class CNN_Model(torch.nn.Module):
    def __init__(self):
        super(CNN_Model, self).__init__()
        # Convolution 1 , input_shape=(3,224,224)
        self.cnn1 = torch.nn.Conv2d(3, 16, kernel_size=5, stride=1)
        self.relu1 = torch.nn.ReLU(inplace=True)
        # Max pool 1
        self.maxpool1 = torch.nn.MaxPool2d(kernel_size=2)
        # Convolution 2
        self.cnn2 = torch.nn.Conv2d(16, 8, kernel_size=11, stride=1)
        self.relu2 = torch.nn.ReLU(inplace=True)
        # Max pool 2
        self.maxpool2 = torch.nn.MaxPool2d(kernel_size=2)
        # Fully connected 1 ,#input_shape=(8*50*50)
        self.fc = torch.nn.Linear(8 * 50 * 50, 2)

    def forward(self, x):
        out = self.cnn1(x)
        out = self.relu1(out)
        out = self.maxpool1(out)
        out = self.cnn2(out)
        out = self.relu2(out)
        out = self.maxpool2(out)
        out = out.view(out.size(0), -1)
        out = self.fc(out)

        return out


class CNN:
    def __init__(self, model_path):
        self.model = torch.load(model_path)

    def detect(self, img):
        # adjust channels and size
        img = cv2.resize(img, (224, 224))
        img = np.einsum('ijk->kij', img)
        img = img.astype("float32")
        input = torch.tensor(np.array([img]))

        # calculate result
        self.model.eval()
        with torch.no_grad():
            output = self.model(input)
        label = output.data.max(dim=1, keepdim=True)[1][0]
        value = output.data.numpy()[0]

        if label == 0:
            name = "Smark"
        else:
            name = "Smark"

        return name, value
