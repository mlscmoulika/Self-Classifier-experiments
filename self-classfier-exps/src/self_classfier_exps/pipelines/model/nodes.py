from torchvision.models import models as models

def self_classifier_main():
    model = models.resnet18(weights=None)
    num_features = model.fc.in_features
    model.fc = torch.nn.Sequential(
        torch.nn.Linear(num_features, 4096),
        torch.nn.BatchNorm1d(4096),
        torch.nn.LeakyReLU(),
        torch.nn.Linear(4096, 128),
        
    )
    return model


def identify_fxn(df):
    return df