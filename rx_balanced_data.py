import pandas as pd
import random

TRAIN_LIST = "data/list/train.csv"
TEST_LIST = "data/list/test.csv"
TOTAL_ENTRY = 1400
TRAIN_ENTRY = 1200
SEED = 17

data_10 = pd.read_csv("data/list/all_10.csv")
data_11 = pd.read_csv("data/list/all_11.csv")
data_12 = pd.read_csv("data/list/all_12.csv")
data_13 = pd.read_csv("data/list/all_13.csv")
data_14 = pd.read_csv("data/list/all_14.csv")
data_15 = pd.read_csv("data/list/all_15.csv")
data_16 = pd.read_csv("data/list/all_16.csv")
data_17 = pd.read_csv("data/list/all_17.csv")
data_18 = pd.read_csv("data/list/all_18.csv")
data_19 = pd.read_csv("data/list/all_19.csv")
data_20 = pd.read_csv("data/list/all_20.csv")

data_10 = data_10.sample(n = TOTAL_ENTRY, random_state=SEED)
data_11 = data_11.sample(n = TOTAL_ENTRY, random_state=SEED)
data_12 = data_12.sample(n = TOTAL_ENTRY, random_state=SEED)
data_13 = data_13.sample(n = TOTAL_ENTRY, random_state=SEED)
data_14 = data_14.sample(n = TOTAL_ENTRY, random_state=SEED)
data_15 = data_15.sample(n = TOTAL_ENTRY, random_state=SEED)
data_16 = data_16.sample(n = TOTAL_ENTRY, random_state=SEED)
data_17 = data_17.sample(n = TOTAL_ENTRY, random_state=SEED)
data_18 = data_18.sample(n = TOTAL_ENTRY, random_state=SEED)
data_19 = data_19.sample(n = TOTAL_ENTRY, random_state=SEED)
data_20 = data_20.sample(n = TOTAL_ENTRY, random_state=SEED)

train = pd.DataFrame([], columns=["image"])
train = train.append(data_10[0:TRAIN_ENTRY], ignore_index = True)
train = train.append(data_11[0:TRAIN_ENTRY], ignore_index = True)
train = train.append(data_12[0:TRAIN_ENTRY], ignore_index = True)
train = train.append(data_13[0:TRAIN_ENTRY], ignore_index = True)
train = train.append(data_14[0:TRAIN_ENTRY], ignore_index = True)
train = train.append(data_15[0:TRAIN_ENTRY], ignore_index = True)
train = train.append(data_16[0:TRAIN_ENTRY], ignore_index = True)
train = train.append(data_17[0:TRAIN_ENTRY], ignore_index = True)
train = train.append(data_18[0:TRAIN_ENTRY], ignore_index = True)
train = train.append(data_19[0:TRAIN_ENTRY], ignore_index = True)
train = train.append(data_20[0:TRAIN_ENTRY], ignore_index = True)

test = pd.DataFrame([], columns=["image"])
test = test.append(data_10[TRAIN_ENTRY:TOTAL_ENTRY], ignore_index = True)
test = test.append(data_11[TRAIN_ENTRY:TOTAL_ENTRY], ignore_index = True)
test = test.append(data_12[TRAIN_ENTRY:TOTAL_ENTRY], ignore_index = True)
test = test.append(data_13[TRAIN_ENTRY:TOTAL_ENTRY], ignore_index = True)
test = test.append(data_14[TRAIN_ENTRY:TOTAL_ENTRY], ignore_index = True)
test = test.append(data_15[TRAIN_ENTRY:TOTAL_ENTRY], ignore_index = True)
test = test.append(data_16[TRAIN_ENTRY:TOTAL_ENTRY], ignore_index = True)
test = test.append(data_17[TRAIN_ENTRY:TOTAL_ENTRY], ignore_index = True)
test = test.append(data_18[TRAIN_ENTRY:TOTAL_ENTRY], ignore_index = True)
test = test.append(data_19[TRAIN_ENTRY:TOTAL_ENTRY], ignore_index = True)
test = test.append(data_20[TRAIN_ENTRY:TOTAL_ENTRY], ignore_index = True)

train.to_csv(TRAIN_LIST, index=False)
test.to_csv(TEST_LIST, index=False)
