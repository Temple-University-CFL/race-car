import pandas as pd
import random

CSV_LIST_FILE = "data/set_merge_csv.csv"

ALL_LIST = "data/list/all.csv"
TRAIN_LIST = "data/list/train.csv"
TEST_LIST = "data/list/test.csv"

SEED = 17
RATIO = 0.8

data = pd.read_csv(CSV_LIST_FILE)

content = []

for index in range(len(data)):
    content.extend(pd.read_csv(data["list"][index])["image"])

random.seed(SEED)
random.shuffle(content)

all_data = pd.DataFrame(content, columns=["image"])
train_data = pd.DataFrame(content[0:int(len(content)*RATIO)], columns=["image"])
test_data = pd.DataFrame(content[int(len(content)*RATIO):-1], columns=["image"])

all_data.to_csv(ALL_LIST, index=False)
train_data.to_csv(TRAIN_LIST, index=False)
test_data.to_csv(TEST_LIST, index=False)