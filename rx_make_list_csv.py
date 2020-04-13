import os
import pandas as pd

FOLDER = "data/csv/"
OUTPUT_LIST = "temp/list_1.csv"

content = os.listdir(FOLDER)
for index in range(len(content)):
    content[index]=FOLDER+content[index]


content = pd.DataFrame(content)
content.to_csv(OUTPUT_LIST, index=False, header=False)