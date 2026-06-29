# Data

This folder contains dataset metadata, CSV label files, train/validation/test splits, and sample data references for the Fish Eye Freshness Classifier project.

The full image dataset is not included in this repository. The dataset should be downloaded separately and organized locally before running training or evaluation.

---

## Dataset Overview

This project uses the Freshness of Fish Eyes (FFE) dataset.

The dataset contains fish eye images labelled into three freshness categories:

| Class | Storage Days |
|---|---:|
| Highly Fresh | Days 1–2 |
| Fresh | Days 3–4 |
| Not Fresh | Days 5–6 |

The full dataset contains 4,392 images across eight fish species.

---

## Expected Folder Structure

The project expects images to be organized by class folder.

Example:

```text
data/
└── raw/
    ├── Highly Fresh/
    ├── Fresh/
    └── Not Fresh/
```

Depending on the script version, the root folder may also be referred to as:

```text
data/kaggle/
```

Make sure the path used in the scripts matches the location of your local dataset.

---

## CSV Files

The following CSV files may be included for reproducibility:

| File | Description |
|---|---|
| `train_split.csv` | Training set image paths and labels |
| `val_split.csv` | Validation set image paths and labels |
| `test_split.csv` | Test set image paths and labels |
| `test_predictions.csv` | Predictions from the custom CNN model |
| `resnet_test_predictions.csv` | Predictions from the ResNet18 model |
| `training_history.csv` | Training metrics for the custom CNN |
| `training_history_resnet.csv` | Training metrics for the ResNet18 model |

These files are useful for reproducing reported results and visualizations without rerunning all experiments.

---

## Label Encoding

The final project uses three freshness classes:

| Class | Label |
|---|---:|
| Highly Fresh | 0 |
| Fresh | 1 |
| Not Fresh | 2 |

Check that label generation scripts match this encoding before training.

---

## Creating Labels and Splits

Generate labels:

```bash
python scripts/make_labels.py
```

Generate train/validation/test splits:

```bash
python scripts/split_data.py
```

Check that the generated CSV files point to valid local image paths.

---

## Important Notes

Large raw image datasets should not be committed to GitHub.

Recommended `.gitignore` entries:

```text
data/raw/
data/kaggle/
*.pyc
__pycache__/
```

Keep small CSV files and metadata if they help reproduce the project results.

---

## Dataset Limitation

The “Fresh” class is visually transitional between “Highly Fresh” and “Not Fresh,” making it the most difficult class to classify. This class overlap was reflected in the final confusion matrix and remains a major area for future improvement.