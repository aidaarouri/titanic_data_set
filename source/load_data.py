import pandas as pd
import sys
def load_data():

    train_df = pd.read_csv("data/train.csv")
    test_df = pd.read_csv('data/test.csv')

    result = pd.concat([train_df, test_df])
    return result

sys.modules[__name__] = load_data



