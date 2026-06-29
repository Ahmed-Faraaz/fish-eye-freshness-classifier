from torch.utils.data import DataLoader
from dataset import FishFreshnessDataset, train_transform, eval_transform

train_ds = FishFreshnessDataset("data/kaggle_fish_train.csv", transform=train_transform)
val_ds   = FishFreshnessDataset("data/kaggle_fish_val.csv",   transform=eval_transform)
test_ds  = FishFreshnessDataset("data/kaggle_fish_test.csv",  transform=eval_transform)

train_loader = DataLoader(train_ds, batch_size=32, shuffle=True,  num_workers=0)
val_loader   = DataLoader(val_ds,   batch_size=32, shuffle=False, num_workers=0)
test_loader  = DataLoader(test_ds,  batch_size=32, shuffle=False, num_workers=0)

# quick sanity check
if __name__ == "__main__":
    imgs, labels = next(iter(train_loader))
    print("Batch shape:", imgs.shape)     # [B, 3, 224, 224]
    print("Labels:", labels[:8])
