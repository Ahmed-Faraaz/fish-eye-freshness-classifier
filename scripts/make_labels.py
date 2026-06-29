from pathlib import Path
import pandas as pd
import re 
from IPython.display import display

DATA_ROOT = Path("data/kaggle")

def build_labels(row_path: Path):

    parent = row_path.parent.name.lower()

    if "Highly Fresh" in parent:
        return 1, "Not Fresh"
    else:
        return 0, "fresh"
    
def scan_image():

    rows = []

    for image_path in DATA_ROOT.rglob("*"):

        label, label_name = build_labels(image_path)
        rows.append({
            "path": str(image_path.resolve()),
            "label": label,
            "label_name": label_name,
        })

    df = pd.DataFrame(rows)

    return df

if __name__ =="__main__":
    df = scan_image()
    display(df)
    df.to_csv("data/kaggle_fish_labels.csv", index = False)
