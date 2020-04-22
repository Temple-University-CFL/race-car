import pandas as pd
import random

TRAIN_LIST = "data/list/train.csv"
TEST_LIST = "data/list/test.csv"
DEV_LIST = "data/list/dev.csv"
TRAIN_ENTRY = 3200
TEST_ENTRY = 3450
TOTAL_ENTRY = 3700
SEED = 717

data_10 = pd.read_csv("data/list/all_10_run.csv")
data_11 = pd.read_csv("data/list/all_11_run.csv")
data_12 = pd.read_csv("data/list/all_12_run.csv")
data_13 = pd.read_csv("data/list/all_13_run.csv")
data_14 = pd.read_csv("data/list/all_14_run.csv")
data_15 = pd.read_csv("data/list/all_15_run.csv")
data_16 = pd.read_csv("data/list/all_16_run.csv")
data_17 = pd.read_csv("data/list/all_17_run.csv")
data_18 = pd.read_csv("data/list/all_18_run.csv")
data_19 = pd.read_csv("data/list/all_19_run.csv")
data_20 = pd.read_csv("data/list/all_20_run.csv")

data_10 = data_10.sample(n = 1300, random_state=SEED)
data_11 = data_11.sample(n = 1700, random_state=SEED)
data_12 = data_12.sample(n = TOTAL_ENTRY, random_state=SEED)
data_13 = data_13.sample(n = TOTAL_ENTRY, random_state=SEED)
data_14 = data_14.sample(n = TOTAL_ENTRY, random_state=SEED)
data_15 = data_15.sample(n = TOTAL_ENTRY, random_state=SEED)
data_16 = data_16.sample(n = TOTAL_ENTRY, random_state=SEED)
data_17 = data_17.sample(n = TOTAL_ENTRY, random_state=SEED)
data_18 = data_18.sample(n = TOTAL_ENTRY, random_state=SEED)
data_19 = data_19.sample(n = 1700, random_state=SEED)
data_20 = data_20.sample(n = 1300, random_state=SEED)

train = pd.DataFrame([], columns=["image"])
train = train.append(data_10[0:1100], ignore_index = True)
train = train.append(data_11[0:1500], ignore_index = True)
train = train.append(data_12[0:TRAIN_ENTRY], ignore_index = True)
train = train.append(data_13[0:TRAIN_ENTRY], ignore_index = True)
train = train.append(data_14[0:TRAIN_ENTRY], ignore_index = True)
train = train.append(data_15[0:TRAIN_ENTRY], ignore_index = True)
train = train.append(data_16[0:TRAIN_ENTRY], ignore_index = True)
train = train.append(data_17[0:TRAIN_ENTRY], ignore_index = True)
train = train.append(data_18[0:TRAIN_ENTRY], ignore_index = True)
train = train.append(data_19[0:1500], ignore_index = True)
train = train.append(data_20[0:1100], ignore_index = True)

test = pd.DataFrame([], columns=["image"])
test = test.append(data_10[1100:1200], ignore_index = True)
test = test.append(data_11[1500:1600], ignore_index = True)
test = test.append(data_12[TRAIN_ENTRY:TEST_ENTRY], ignore_index = True)
test = test.append(data_13[TRAIN_ENTRY:TEST_ENTRY], ignore_index = True)
test = test.append(data_14[TRAIN_ENTRY:TEST_ENTRY], ignore_index = True)
test = test.append(data_15[TRAIN_ENTRY:TEST_ENTRY], ignore_index = True)
test = test.append(data_16[TRAIN_ENTRY:TEST_ENTRY], ignore_index = True)
test = test.append(data_17[TRAIN_ENTRY:TEST_ENTRY], ignore_index = True)
test = test.append(data_18[TRAIN_ENTRY:TEST_ENTRY], ignore_index = True)
test = test.append(data_19[1500:1600], ignore_index = True)
test = test.append(data_20[1100:1200], ignore_index = True)

dev = pd.DataFrame([], columns=["image"])
dev = test.append(data_10[1200:1300], ignore_index = True)
dev = test.append(data_11[1600:1700], ignore_index = True)
dev = test.append(data_12[TEST_ENTRY:TOTAL_ENTRY], ignore_index = True)
dev = test.append(data_13[TEST_ENTRY:TOTAL_ENTRY], ignore_index = True)
dev = test.append(data_14[TEST_ENTRY:TOTAL_ENTRY], ignore_index = True)
dev = test.append(data_15[TEST_ENTRY:TOTAL_ENTRY], ignore_index = True)
dev = test.append(data_16[TEST_ENTRY:TOTAL_ENTRY], ignore_index = True)
dev = test.append(data_17[TEST_ENTRY:TOTAL_ENTRY], ignore_index = True)
dev = test.append(data_18[TEST_ENTRY:TOTAL_ENTRY], ignore_index = True)
dev = test.append(data_19[1600:1700], ignore_index = True)
dev = test.append(data_20[1200:1300], ignore_index = True)

train.to_csv(TRAIN_LIST, index=False)
test.to_csv(TEST_LIST, index=False)
dev.to_csv(DEV_LIST, index=False)
