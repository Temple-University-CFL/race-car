import pandas as pd
from av_parse_data import ParseData

LIST_FILE = "data/list/all_10.csv"
RUN_LIST = "data/list/all_10_run.csv"

data = pd.read_csv(LIST_FILE)
parsedata = ParseData()

file = []
for index in range(len(data)):
    _,_,mot = parsedata.parse_data(data["image"][index])
    if mot != 15:
        file.append(data["image"][index])

pd.DataFrame(file, columns=["image"]).to_csv(RUN_LIST, index=False)