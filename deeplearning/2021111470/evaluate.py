import os
import torch
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, f1_score, jaccard_score
from torchvision import transforms


class SimpleUNet(torch.nn.Module):
    def __init__(self):
        super(SimpleUNet, self).__init__()
        self.enc1 = torch.nn.Sequential(
            torch.nn.Conv2d(3, 64, 3, padding=1), torch.nn.ReLU(),
            torch.nn.Conv2d(64, 64, 3, padding=1), torch.nn.ReLU()
        )
        self.pool = torch.nn.MaxPool2d(2, 2)
        self.dec1 = torch.nn.Sequential(
            torch.nn.Conv2d(64, 64, 3, padding=1), torch.nn.ReLU(),
            torch.nn.Conv2d(64, 1, 1)
        )

    def forward(self, x):
        x1 = self.enc1(x)
        x2 = self.pool(x1)
        x3 = torch.nn.functional.interpolate(x2, scale_factor=2, mode='bilinear', align_corners=False)
        out = self.dec1(x3)
        return out


transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor()
])


def evaluate_predictions(preds, gts, threshold=0.3):
    preds_bin = (preds > threshold).astype(np.uint8)
    gts_bin = (gts > threshold).astype(np.uint8)
    flat_pred = preds_bin.flatten()
    flat_gt = gts_bin.flatten()
    acc = accuracy_score(flat_gt, flat_pred)
    iou = jaccard_score(flat_gt, flat_pred, zero_division=1)
    f1 = f1_score(flat_gt, flat_pred, zero_division=1)
    return acc, iou, f1


test_img_dir = "hed/HED-BSDS/test"
canny_gt_dir = "hed/HED-BSDS-CannyGT/test"
bsds_gt_dir = "hed/HED-BSDS/test"


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = SimpleUNet().to(device)
model.load_state_dict(torch.load("model.pth", map_location=device))
model.eval()


pred_list, canny_list, bsds_list = [], [], []
os.makedirs("vis_full", exist_ok=True)

for i, fname in enumerate(sorted(os.listdir(canny_gt_dir))):
    img_path = os.path.join(test_img_dir, fname)
    canny_path = os.path.join(canny_gt_dir, fname)
    bsds_path = os.path.join(bsds_gt_dir, fname)

    if not (os.path.exists(img_path) and os.path.exists(canny_path) and os.path.exists(bsds_path)):
        continue

    image = Image.open(img_path).convert('RGB')
    canny_gt = Image.open(canny_path).convert('L')
    bsds_gt = Image.open(bsds_path).convert('L')

    input_tensor = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        pred = torch.sigmoid(model(input_tensor)).squeeze().cpu().numpy()
    canny = transform(canny_gt).squeeze().numpy()
    bsds = transform(bsds_gt).squeeze().numpy()
    print(f"[{fname}] pred>0.3: {np.sum(pred > 0.3)}, canny>0.3: {np.sum(canny > 0.3)}, bsds>0.3: {np.sum(bsds > 0.3)}")

    pred_list.append(pred)
    canny_list.append(canny)
    bsds_list.append(bsds)

    if i < 3:
        fig, axs = plt.subplots(1, 4, figsize=(12, 3))
        axs[0].imshow(image)
        axs[0].set_title("Input Image")
        axs[1].imshow(canny, cmap='gray')
        axs[1].set_title("Canny GT")
        axs[2].imshow(pred, cmap='gray')
        axs[2].set_title("Prediction")
        axs[3].imshow(bsds, cmap='gray')
        axs[3].set_title("BSDS GT")
        for ax in axs:
            ax.axis('off')
        plt.tight_layout()
        plt.savefig(f"vis_full/result_{i}.png")
        plt.close()


pred_array = np.array(pred_list)
canny_array = np.array(canny_list)
bsds_array = np.array(bsds_list)

acc1, iou1, f1_1 = evaluate_predictions(pred_array, canny_array)
acc2, iou2, f1_2 = evaluate_predictions(pred_array, bsds_array)


print("\n📊 Evaluation Results:")
print(f"[Canny GT]  Accuracy: {acc1:.4f}, IoU: {iou1:.4f}, F1: {f1_1:.4f}")
print(f"[BSDS GT]   Accuracy: {acc2:.4f}, IoU: {iou2:.4f}, F1: {f1_2:.4f}")
print("🖼 이미지 비교 결과는 vis_full/ 폴더에 저장됨.")