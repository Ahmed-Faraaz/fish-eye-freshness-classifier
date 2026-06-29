import pandas as pd
from sklearn.model_selection import train_test_split

DF_PATH = "data/kaggle_fish_labels.csv"

if __name__ == "__main__":

    df = pd.read_csv(DF_PATH)

    train_val, test = train_test_split(df, test_size = 0.2, stratify = df["label"], random_state= 42)

    train, val = train_test_split(train_val, test_size=0.2, stratify=train_val["label"], random_state=42)
    
    train.to_csv("data/kaggle_fish_train.csv")
    val.to_csv("data/kaggle_fish_val.csv")
    test.to_csv("data/kaggle_fish_test.csv")

    print(f"Split - Train: {len(train)}, Val: {len(val)}, Test: {len(test)}")