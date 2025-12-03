This notebook trains a CNN to classify fish eye images into three freshness classes using the FFE Fish Eye dataset. 

DATASET
This model makes use of the FFE Fish Eye dataset which is publicly available for download via: https://data.mendeley.com/datasets/xzyx7pbr3w/1
Direct download link: https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/xzyx7pbr3w-1.zip 

ENVIRONMENT
- Python 3.11.9
- PyTorch, Torchvision, scikit-learn, matplotlib, pandas, numpy


TL;DR RESULTS (current):
- Test Accuracy: 67.4%
- Majority Baseline: 40.2% (always predict "Highly Fresh")
- Per-class (Test):
  - Highly Fresh — Recall: 88.3%, Precision: 63.8%, F1: 0.74
  - Fresh — Recall: 52.6%, Precision: 67.5%, F1: 0.59
  - Not Fresh — Recall: 52.6%, Precision: 76.3%, F1: 0.62

PROJECT STRUCTURE AND EXECUTION

Project/
	-> /FishFreshness_training_Performance.ipynb
	-> /artifacts
		-> /best_model_state_dict.pt
		-> /training_history.csv
	-> /data
		-> /mendely
			-> Chanos Chanos - Fresh
			-> Chanos Chanos - Highly Fresh
			-> ...
	-> /images
		-> Plots.png

To run ensure the jupyter notbook is on the same level as the data folder and artifacts folder. Open notebook and select run all. 
The notebook is pre-run. For evaluation on trained model run the cells under section "EVALUATION USING TRAINED MODEL"

WARNING: If the "run all" button is selected model training will be reperformed. 

EVALUATION
We report:
- Overall accuracy
- Per-class precision/recall/F1
- Confusion matrix
- Confidence calibration histogram (probability of the true class for correct vs incorrect predictions)


	
