# Fish Eye Freshness Classifier

This project uses computer vision and deep learning to classify fish freshness from images of fish eyes.

The goal is to replace subjective freshness checks, such as visual inspection, smell, and texture, with a more objective image-based classification system. Fish eye appearance, including brightness, glossiness, colour variation, pupil clarity, and corneal clouding, is strongly related to freshness and can be used as a visual indicator of quality.

---

## Project Overview

The model classifies fish eye images into three freshness categories:

| Class | Storage Days |
|---|---:|
| Highly Fresh | Days 1–2 |
| Fresh | Days 3–4 |
| Not Fresh | Days 5–6 |

The final model uses a **ResNet18 transfer learning** approach and improves substantially over the initial custom CNN baseline.

---

## Dataset

This project uses the **Freshness of Fish Eyes (FFE)** dataset.

The dataset contains **4,392 fish eye images** across eight fish species, labelled into three freshness levels:

| Freshness Class | Samples |
|---|---:|
| Highly Fresh | 1,764 |
| Fresh | 1,320 |
| Not Fresh | 1,306 |

The dataset was split into training, validation, and test sets using a stratified split to preserve class balance across the splits.

---

## Model Approach

Two model approaches were explored:

### 1. Custom CNN Baseline

The initial model used a lightweight convolutional neural network trained from scratch. This model achieved approximately **67.4% test accuracy**.

While it performed better than the majority-class baseline, Grad-CAM analysis showed that it sometimes focused on irrelevant background details rather than the fish eye itself.

### 2. ResNet18 Transfer Learning

The final model uses **ResNet18 pretrained on ImageNet**.

The ResNet18 model was adapted by:

- Freezing early convolutional layers
- Fine-tuning higher-level layers
- Replacing the final classification head for three freshness classes
- Using ImageNet normalization
- Applying geometric data augmentation
- Using label smoothing to improve generalization
- Applying Grad-CAM to verify model attention

---

## Results

The final ResNet18 model achieved:

| Model | Test Accuracy |
|---|---:|
| Majority Baseline | 40.2% |
| Custom CNN | 67.4% |
| ResNet18 | 80.4% |

Per-class ResNet18 performance:

| Class | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Highly Fresh | 0.875 | 0.868 | 0.871 |
| Fresh | 0.737 | 0.722 | 0.729 |
| Not Fresh | 0.777 | 0.801 | 0.789 |

The “Fresh” class remained the most challenging because it represents a transition state between highly fresh and not fresh.

---

## Explainability

Grad-CAM was used to inspect model attention.

The custom CNN often focused on background regions such as trays, scales, or surrounding image texture. The ResNet18 model showed improved attention on the biologically relevant fish eye region, especially the pupil and cornea.

This helped confirm that the ResNet18 model was learning meaningful freshness-related visual features instead of relying on background artifacts.

---

## Repository Structure

```text
fish-eye-freshness-classifier/
├── artifacts/                  # Training outputs, plots, reports, and model checkpoints
├── data/                       # CSV splits, labels, and dataset instructions
├── docs/                       # Final report and supporting documentation
├── notebooks/                  # Jupyter notebooks for experiments and analysis
├── scripts/                    # Dataset preparation and utility scripts
├── src/                        # Reusable dataset/model/training code
├── tests/                      # Optional debugging and loader tests
├── README.md
└── requirements.txt
```

---

## How to Run

### 1. Create a Virtual Environment

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

On macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If dependencies are missing, install the core packages:

```bash
pip install torch torchvision pandas scikit-learn matplotlib pillow notebook
```

---

### 3. Prepare the Dataset

The project expects images to be organized by class folder.

Example:

```text
data/
└── raw/
    ├── Highly Fresh/
    ├── Fresh/
    └── Not Fresh/
```

Generate labels:

```bash
python scripts/make_labels.py
```

Generate train/validation/test splits:

```bash
python scripts/split_data.py
```

---

### 4. Check Data Loaders

Run a quick sanity check to confirm that images and labels are loading correctly:

```bash
python scripts/debug_loaders.py
```

Expected output should include a batch shape similar to:

```text
Batch shape: torch.Size([32, 3, 224, 224])
```

---

### 5. Train or Explore the Model

The main experimentation notebook is:

```text
notebooks/fish_freshness.ipynb
```

Training and performance visualization can also be reviewed in:

```text
notebooks/FishFreshness_Training_Performance.ipynb
```

---

### 6. Load a Trained Model

If using the saved model checkpoint, load it using the matching model architecture before calling `load_state_dict`.

Example:

```python
model = FreshnessClass()
state_dict = torch.load("artifacts/freshness_cnn_final.pt", map_location="cpu")
model.load_state_dict(state_dict)
model.eval()
```

For the ResNet18 model, make sure the architecture matches the saved checkpoint before loading the weights.

---

## Future Improvements

- Convert notebook training code into reusable training scripts
- Add a simple inference script for single-image prediction
- Add a Streamlit or FastAPI demo for image upload and classification
- Use GitHub Releases or Git LFS for model checkpoints
- Improve handling of the intermediate “Fresh” class using ordinal regression
- Expand Grad-CAM visualizations for more test samples
- Add stronger documentation for dataset setup and model loading

---

## Contributors

- Faraaz Ahmed
- Manav Bal