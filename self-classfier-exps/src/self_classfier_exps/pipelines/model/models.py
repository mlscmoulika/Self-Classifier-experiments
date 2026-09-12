import torch
import torch.nn as nn
import torchvision.models as models
import torch.nn.functional as F

class SelfClassifier(nn.Module):
    def __init__(self, mode="pretrain"):
        super().__init__()
        self.mode = mode
        self.backbone = models.resnet18(weights=None)
        num_features = self.backbone.fc.in_features
        self.backbone.fc = nn.Identity()

        self.projection_head = nn.Sequential(
            nn.Linear(num_features, 4096),
            nn.BatchNorm1d(4096),
            nn.LeakyReLU(),
            nn.Linear(4096, 128),
        )

        if self.mode == "pretrain":
            self.head_1 = nn.Linear(128, 64, bias=False)
            self.head_2 = nn.Linear(128, 128, bias=False)
            self.head_3 = nn.Linear(128, 256, bias=False)
            self.head_4 = nn.Linear(128, 512, bias=False)
            
        elif self.mode == "linear_eval":
            self.linear_classifier = nn.Linear(num_features, 10) 
    def forward(self, x):
        features = self.backbone(x)
        if self.mode == "pretrain":
            projected_features = self.projection_head(features)
            norm_projected_features = F.normalize(projected_features, p=2, dim=1)
            out_1 = self.head_1(norm_projected_features)
            out_2 = self.head_2(norm_projected_features)
            out_3 = self.head_3(norm_projected_features)
            out_4 = self.head_4(norm_projected_features)
            return projected_features, out_1, out_2, out_3, out_4
        elif self.mode == "linear_eval":
            logits = self.linear_classifier(features)
            return logits                                                                                                                   