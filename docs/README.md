# Fish Eye Freshness Documentation

This folder contains the final report and supporting documentation for the Fish Eye Freshness Classifier project.

The project investigates whether fish freshness can be classified from fish eye images using convolutional neural networks and transfer learning.

---

## Documentation Index

| File | Description |
|---|---|
| `4al3_final_project.pdf` | Final project report describing the motivation, related work, dataset, preprocessing, model architecture, training strategy, evaluation, Grad-CAM analysis, and conclusions. |

---

## Project Summary

The goal of this project is to classify fish freshness from images of fish eyes.

The three target classes are:

- Highly Fresh
- Fresh
- Not Fresh

The final approach uses a ResNet18 model pretrained on ImageNet and fine-tuned for three-class freshness classification.

---

## Key Results

| Model | Test Accuracy |
|---|---:|
| Majority Baseline | 40.2% |
| Custom CNN | 67.4% |
| ResNet18 | 80.4% |

The final ResNet18 model significantly outperformed the custom CNN baseline and achieved stronger class balance across the three freshness categories.

---

## Important Findings

- Fish eye images contain useful visual cues for freshness classification.
- The custom CNN baseline sometimes focused on background features rather than the fish eye.
- ResNet18 transfer learning improved both accuracy and attention localization.
- Grad-CAM showed that the ResNet18 model focused more strongly on the pupil and cornea.
- The intermediate “Fresh” class remained the most difficult because it visually overlaps with both “Highly Fresh” and “Not Fresh.”

---

## Report Contents

The final report includes:

- Introduction and motivation
- Related work
- Dataset description
- Data splits and label setup
- Preprocessing and augmentation
- Custom CNN baseline
- ResNet18 transfer learning approach
- Training configuration
- Evaluation metrics
- Confusion matrix analysis
- Confidence and calibration analysis
- Grad-CAM visualizations
- Reflection and future improvements

---

## Notes

The PDF report is included to preserve the final project formatting. Any images, figures, or plots extracted from the report can be added to this folder or to an `images/` subfolder if needed.