import os
from PIL import Image
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt

def get_image_paths_recursive(root, valid_exts=('.jpg', '.jpeg', '.png', '.ppm')):
    paths = []
    for dirpath, _, filenames in os.walk(root):
        for f in filenames:
            if f.lower().endswith(valid_exts):
                paths.append(os.path.join(dirpath, f))
    return sorted(paths)

class BSDSCannyDataset(Dataset):
    def __init__(self, img_dir, label_dir, transform=None):
        self.transform = transform

        self.label_paths = get_image_paths_recursive(label_dir)
        self.img_paths = []

        for label_path in self.label_paths:
            basename = os.path.basename(label_path)
            # 이미지 경로를 찾을 때 label과 같은 이름의 이미지만 포함
            matched = None
            for dirpath, _, filenames in os.walk(img_dir):
                for f in filenames:
                    if f == basename:
                        matched = os.path.join(dirpath, f)
                        break
                if matched:
                    break
            if matched:
                self.img_paths.append(matched)
            else:
                print(f"Warning: No matching image found for label {basename}")

        assert len(self.img_paths) == len(self.label_paths), f"Mismatch: {len(self.img_paths)} images, {len(self.label_paths)} labels"

    def __len__(self):
        return len(self.img_paths)

    def __getitem__(self, idx):
        img = Image.open(self.img_paths[idx]).convert('RGB')
        label = Image.open(self.label_paths[idx]).convert('L')
        if self.transform:
            img = self.transform(img)
            label = self.transform(label)
        return img, label


class SimpleUNet(nn.Module):
    def __init__(self):
        super(SimpleUNet, self).__init__()
        self.enc1 = nn.Sequential(nn.Conv2d(3, 64, 3, padding=1), nn.ReLU(), nn.Conv2d(64, 64, 3, padding=1), nn.ReLU())
        self.pool = nn.MaxPool2d(2, 2)
        self.dec1 = nn.Sequential(nn.Conv2d(64, 64, 3, padding=1), nn.ReLU(), nn.Conv2d(64, 1, 1))

    def forward(self, x):
        x1 = self.enc1(x)
        x2 = self.pool(x1)
        x3 = F.interpolate(x2, scale_factor=2, mode='bilinear', align_corners=False)
        out = self.dec1(x3)
        return out


train_img_dir = "hed/HED-BSDS/train"
train_gt_dir = "hed/HED-BSDS-CannyGT/train"
val_img_dir = "hed/HED-BSDS/test"
val_gt_dir = "hed/HED-BSDS-CannyGT/test"

# ----- Transform & Loader -----
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor()
])
train_dataset = BSDSCannyDataset(train_img_dir, train_gt_dir, transform)
val_dataset = BSDSCannyDataset(val_img_dir, val_gt_dir, transform)
train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=4)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = SimpleUNet().to(device)
criterion = nn.BCEWithLogitsLoss(pos_weight=torch.tensor([10.0]).to(device))
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)


train_losses, val_losses = [], []

for epoch in range(10):
    model.train()
    running_loss = 0.0
    for images, labels in train_loader:
        images = images.to(device)
        labels = labels.to(device)

        preds = model(images)
        loss = criterion(preds, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        running_loss += loss.item()

    train_losses.append(running_loss / len(train_loader))


    model.eval()
    val_loss = 0.0
    with torch.no_grad():
        for images, labels in val_loader:
            images = images.to(device)
            labels = labels.to(device)
            preds = model(images)
            val_loss += criterion(preds, labels).item()
    val_losses.append(val_loss / len(val_loader))

    print(f"Epoch {epoch+1}, Train Loss: {train_losses[-1]:.4f}, Val Loss: {val_losses[-1]:.4f}")


plt.plot(train_losses, label='Train Loss')
plt.plot(val_losses, label='Val Loss')
plt.legend()
plt.title("Loss Curve")
plt.savefig("loss_curve.png")
plt.show()


torch.save(model.state_dict(), "model.pth")